# Билбиотека для работы с VK ID на Python3

Библиотека на основе https://github.com/sshumikhin/unofficial-vk-id-python-sdk
переработанная для использования в синхронном режиме. Используется requests вместо aiohttp

Установка зависимостей:
```
pip install pydantic requests
```

## Пример использования для реализации авторизации через VK ID в Django
*в настройках разрешений приложения VK нужно включить Номер телефона*
- view для редиректа на страницу авторизации vk
```
import json
import urllib
import redis
import logging

from django.conf import settings
from django.http import HttpResponseRedirect

from vk_id import configure_app as vk_id_app_configure
from vk_id import get_app_configuration, Scopes, generate_pkce


def get_vk_auth_form(request):
    app = get_app_configuration()
    if not app:
        vk_id_app_configure(
            app_name='some app name',
            client_id=settings.VK_APP_ID,
            client_secret=settings.VK_APP_SECRET_KEY,
            client_access_key=settings.VK_APP_SERVICE_KEY,
            redirect_url=settings.CURRENT_HOST + '/vk_auth/callback/',
            success_url=settings.CURRENT_HOST
        )
        app = get_app_configuration()
    pkce = generate_pkce(scopes=[Scopes.PHONE.value])

    payload = {
        'response_type': 'code',
        'client_id': int(app.client_id),
        'scope': pkce.scopes,
        'redirect_uri': getattr(app.trusted_uris, 'redirect_url'),
        'code_challenge': pkce.code_challenge,
        'code_challenge_method': 'S256',
        'code_verifier": pkce.code_verifier'
        'state': pkce.state
    }
    redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, password=settings.REDIS_PASS)
    redis_client.set(pkce.state, json.dumps(payload))
    del payload['code_verifier']
    return HttpResponseRedirect('https://id.vk.com/authorize?' + urllib.parse.urlencode(payload))
```

- view для обработки callback от VK
```
import json
import redis

from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model, login

from vk_id import configure_app as vk_id_app_configure, exchange_code
from vk_id.dataclasses.user import User as VKUser
from vk_id import get_app_configuration, get_user_public_info


def get_code_state_device_id(request):
    success_url = '/auth/?error=1'
    state = request.GET.get("state", False)
    code = request.GET.get("code", False)
    device_id = request.GET.get("device_id", False)
    if not(state and code and device_id):
        return HttpResponseRedirect(success_url)
    app = get_app_configuration()
    if not app:
        vk_id_app_configure(
            app_name='some app name',
            client_id=settings.VK_APP_ID,
            client_secret=settings.VK_APP_SECRET_KEY,
            client_access_key=settings.VK_APP_SERVICE_KEY,
            redirect_url=settings.CURRENT_HOST + '/vk_auth/callback/',
            success_url=settings.CURRENT_HOST
        )
    redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, password=settings.REDIS_PASS)
    state_data = redis_client.get(state)
    if state_data:
        state_data = json.loads(state_data)
    else:
        return HttpResponseRedirect(success_url)
    tokens = exchange_code(
            code_verifier=state_data["code_verifier"],
            redirect_uri_tag="redirect_url",
            code=code,
            device_id=device_id,
            state=state
    )
    try:
        vk_response = get_user_public_info(access_token=tokens.access_token)
    except AttributeError:
        return HttpResponseRedirect(success_url)
    if isinstance(vk_response, VKUser):
        # Поиск пользователя в локальной базе по номеру телефона, либо создание нового
        try:
            user = get_user_model().objects.get(phone=vk_response.phone)
        except get_user_model().DoesNotExist:
            user = get_user_model().objects.create(
                phone=vk_response.phone,
                vk_user_id=vk_response.user_id,
                name=f'{vk_response.last_name} {vk_response.first_name}'.strip()
            )
        login(request, user)
        return HttpResponseRedirect(user.get_profile_url())
    return HttpResponseRedirect(success_url)

```

Если пользователь не найден в БД - будет создан новый.

в settings.py необходимо указать:
- **VK_APP_ID** - id приложения VK
- **VK_APP_SECRET_KEY** - защищённый ключ приложения VK
- **VK_APP_SERVICE_KEY** - сервисный ключ приложения VK

для сохранения state и code_verifier здесь используется redis, но можно использовать любой другой механизм для сохранения данных между запросам 
