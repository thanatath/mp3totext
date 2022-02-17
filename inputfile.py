import os
from pathlib import Path

FILE_INPUT = 'Null.wav'


while True:
    file_name = input("Input your wave file name (ex. input.wav) : ")
    file_name = os.path.abspath(file_name)
    if os.path.isfile(file_name):
        FILE_INPUT = file_name
        break
    else:
        print(os.path.abspath(file_name)," File not found !")

FILE_LOCATION = os.path.abspath(FILE_INPUT)
FILE_DIR = str(Path(FILE_LOCATION).parent)
audio_wav = Path(str(FILE_INPUT).split(".mp3")[0])

print("File input: ",FILE_INPUT)
