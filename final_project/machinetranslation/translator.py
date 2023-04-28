import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
import os

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

languages = language_translator.list_languages().get_result()

SOURCE_LANG = 'en'
TARGET_LANG = 'fr'

def englishToFrench(english_text):
    translation_result = language_translator.translate(
    text=english_text,
    source=SOURCE_LANG,
    target=TARGET_LANG
    ).get_result()
    french_text = translation_result['translations'][0]['translation']
    return french_text


def frenchToEnglish(french_text):
    translation_result = language_translator.translate(
    text=french_text,
    source=SOURCE_LANG,
    target=TARGET_LANG
    ).get_result()
    english_text = translation_result['translations'][0]['translation']
    return english_text


