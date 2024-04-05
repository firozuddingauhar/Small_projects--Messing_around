# pip install googletrans==3.1.0a0
from googletrans import Translator
translator = Translator()
text = input("Text: ")
translation = translator.translate(text, dest='hi')
print(translation.text)