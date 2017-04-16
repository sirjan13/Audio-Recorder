import requests
from record_demo import *

APP_ACCESS_TOKEN = 'P637HVIWSHN73DKHIB2SPGVTKLVRZWSI'

base_url = 'https://api.wit.ai/speech'


def convert_speech_to_text(file_path):
    user_input = int(raw_input("Do You want to :- \n 1)Record new clip \n 2)Use Previous Recording \n -  "))
    if user_input == 1:
        print "Recording..."
        data = record_my_audio()
        print "Done."
        save_my_recording(file_path,data[1], data[0], data[2])
    print "Converting...."
    audio = read_audio(file_path)
    headers = {'authorization': 'Bearer ' + APP_ACCESS_TOKEN,
               'Content-Type': 'audio/wav'}
    data_response = requests.post(base_url, headers=headers, data=audio).json()
    return 'You Said :  ' + data_response['_text']

choice = get_user_input()

if choice == 1:
    data = record_my_audio()
    file_name = 'my_recording.wav'
    save_my_recording(file_name, data[1], data[0], data[2])
elif choice == 2:
    file_name = "my_recording.wav"
    if os.path.exists(file_name):
        play_sound(file_name)
    else:
        print "\nThere is no Audio Recorded Yet. "
else:
    text = convert_speech_to_text('my_recording.wav')
    print text


