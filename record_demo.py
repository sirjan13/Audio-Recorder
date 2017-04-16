import pyaudio
import wave
import os.path


def play_sound(path_to_file):

    print "Now Playing....."
    chunk = 1024
    f = wave.open(path_to_file)
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)

    data = f.readframes(chunk)

    for i in range(len(data)):
        stream.write(data)
        data = f.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()


def record_my_audio():
    time_duration = int(raw_input('Enter the time duration for your speech clip :-  '))
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = time_duration
    print "Recording..."

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()
    print "Finished Recording\n"
    return_data = [frames, stream, audio]
    return return_data

def save_my_recording(destination_filename, stream, frames, audio):
    channels = stream._channels
    rate = stream._rate
    format = stream._format

    wave_File = wave.open(destination_filename, 'wb')
    wave_File.setnchannels(channels)
    wave_File.setsampwidth(audio.get_sample_size(format))
    wave_File.setframerate(rate)
    wave_File.writeframes(b''.join(frames))
    wave_File.close()


def read_audio(file_path):
    # function to read audio(wav) file
    with open(file_path, 'rb') as f:
        audio = f.read()
    return audio


def get_user_input():
    print "Hello , Record and Play your Audio Here \n\n"
    print "What do you want to do :\n 1) Record and Listen to audio\n 2) Hear Previously saved video\n 3) Convert Audio To Text\n"
    entered_value = int(raw_input("Enter 1 , 2 or 3 -->  "))
    if entered_value in [1, 2, 3]:
        return entered_value
    else:
        print "It seems you entered the Wrong Choice .Try Again. \n"
        return get_user_input()

