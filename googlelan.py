from googletrans import Translator

import googletrans

translator = Translator()
result = translator.translate('how are you' , src='en',dest='ja')
print(result)
print(googletrans.LANGUAGES)

#https://github.com/Afrah333333/language-processor.git