from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas import json_normalize
from ibm_watson import LanguageTranslatorV3

url_s2t = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/a50c08e6-d879-4d50-bf73-29a3dfc8a296"
apikey_s2t = "7H_eOrdFMaM5CLXBMbtsG3J2EVCdxzNf1P_bHKrfQr3T"

authenticator = IAMAuthenticator(apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)

filename = 'PolynomialRegressionandPipelines.mp3'

with open(filename, mode='rb') as wav:
    response = s2t.recognize(audio=wav, content_type = 'audio/mp3')

#print(json_normalize(response.result['results'], "alternatives"))
#print(response.get_result())
#print(response.result)
#if response.get_result() == response.result:
    #print('YES!!!!!')
#else:
    #print('AHUDHFIHIHIQHI')
#print(json_normalize(response.result['results'], "alternatives"))
recognized_text = response.result['results'][0]['alternatives'][0]['transcript']

url_lt='https://api.kr-seo.language-translator.watson.cloud.ibm.com/instances/00f526b6-84df-4616-b3f3-d70aeb483dda'
apikey_lt='WvYgw6A-67iyCx-TvSFzXcRUPtT094v1DBCq6xgXxOZ7'
version_lt = '2018-05-01'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt, authenticator=authenticator)
language_translator.set_service_url(url_lt)

#print(json_normalize(language_translator.list_identifiable_languages().get_result(), "languages"))
#print(language_translator.list_identifiable_languages().get_result())
#print(language_translator.list_identifiable_languages())
#print(json_normalize(language_translator.list_identifiable_languages().result, "languages"))
#print(language_translator.list_identifiable_languages().result)
#print(type(language_translator.list_identifiable_languages()))
#print(type(language_translator.list_identifiable_languages().get_result()))

translation_response = language_translator.translate(text=recognized_text, model_id='en-es')
translation = translation_response.get_result()
spanish_translation = translation['translations'][0]['translation']

#translation_ex = language_translator.translate(text=recognized_text, model_id='en-es').get_result()
#spanish_translation_ex = translation_ex['translations'][0]['translation'] 
#위의 세 줄 코드랑 같은 역할 (여기서는 그냥 바로 response 받고 .get_result 까지 붙여버림)

print(spanish_translation) 
translation_new = language_translator.translate(text=spanish_translation, model_id='es-en').get_result()
#print(translation_new)
english_translation = translation_new['translations'][0]['translation']
#print(english_translation)