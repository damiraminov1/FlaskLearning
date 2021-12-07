import requests
from flask import current_app
from flask_babel import _


def translate(text, source_language, dest_language):
    if 'YANDEX_TRANSLATOR_KEY' not in current_app.config or not current_app.config['YANDEX_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    api_url = 'https://translate.api.cloud.yandex.net/translate/v2/translate'
    r = requests.post(
        api_url,
        headers={
            'Authorization': 'Api-Key ' + current_app.config['YANDEX_TRANSLATOR_KEY']
        },
        json={
            'sourceLanguageCode': source_language,
            'targetLanguageCode': dest_language,
            'texts': text
        })
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return r.json()['translations'][0]['text']
