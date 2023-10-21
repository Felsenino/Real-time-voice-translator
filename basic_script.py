import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import gtts.lang as lang
from playsound import playsound
from os import remove

save_audio = str(input("\nDo you want to save the file to your computer? (Y/n) ")).lower()

if save_audio == "y":
    file_name = str(input("\nChoose a name for your audio file: "))

input_language_message = '\nInsert the input language code here (or type "languages" to get the full codes list): '
output_language_message = '\nInsert the output language code here (or type "languages" to get the full codes list): '

languages = lang.tts_langs()

#show languages codes if requested
def show_languages():
    for code, language in languages.items():
        print(f"{code}: {language}")

input_language_code = str(input(input_language_message))
if input_language_code == "languages":
    show_languages()
    input_language_code = str(input(input_language_message))

output_language_code = str(input(output_language_message))
if output_language_code == "languages":
    show_languages()
    output_language_code = str(input(output_language_message))

#audio recorder
recorder = sr.Recognizer()

with sr.Microphone() as source:
    print("\nI'm listening...")
    audio_record = recorder.listen(source, timeout=2)
    
#audio to text
try:
    text = recorder.recognize_google(audio_record, language=input_language_code)
    print("\nYour text: ", text)

    #text translator
    translator = Translator()

    translated_text = translator.translate(text, dest=output_language_code)
    print("\nTranslated text: ", translated_text.text)

except sr.UnknownValueError:
    print("\nSpeech Recognition could not understand audio")
except sr.RequestError as e:
    print("\nCould not request results from Speech Recognition; {0}".format(e))

#translated text to speech
tts = gTTS(translated_text.text, lang=output_language_code)

if save_audio == "n":
    tts.save("temp.mp3")
    playsound("temp.mp3")
    remove("temp.mp3")
else:
    tts.save(f"{file_name}.mp3")
    playsound(f"{file_name}.mp3")