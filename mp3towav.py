from pydub import AudioSegment
from inputfile import FILE_INPUT, FILE_LOCATION, FILE_DIR, audio_wav
sound = AudioSegment.from_mp3(FILE_LOCATION)
sound.export(audio_wav)



