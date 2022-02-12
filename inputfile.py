import os
from pathlib import Path


FILE_INPUT = "input.wav"
FILE_LOCATION = os.path.abspath(FILE_INPUT)
FILE_DIR = str(Path(FILE_LOCATION).parent)
audio_wav = Path(str(FILE_DIR+'/'+FILE_INPUT).split(".mp3")[0])

print("File input: ",FILE_INPUT)
