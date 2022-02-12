import os
from pathlib import Path


FILE_INPUT = "2022-01-27 10-46-22.wav"
FILE_LOCATION = os.path.abspath(FILE_INPUT)
FILE_DIR = str(Path(FILE_LOCATION).parent)
audio_wav = Path(str(FILE_DIR+'/'+FILE_INPUT).split(".mp3")[0])

print("File input: ",FILE_INPUT)
