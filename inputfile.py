import os
from pathlib import Path

print("Wav to text")

FILE_INPUT = input("Input your wave file name (ex. input.wav) :")
FILE_LOCATION = os.path.abspath(FILE_INPUT)
FILE_DIR = str(Path(FILE_LOCATION).parent)
audio_wav = Path(str(FILE_DIR+'/'+FILE_INPUT).split(".mp3")[0])

print("File input: ",FILE_INPUT)
