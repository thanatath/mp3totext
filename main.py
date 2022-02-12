import os
from inputfile import FILE_INPUT, FILE_LOCATION, FILE_DIR, audio_wav
#import mp3towav
import split_file
from split_file import *
import speech_recognition as sr


for x in range(1,counter):
    AUDIO_FILE = (FILE_DIR+"/tmp/chunk%d.wav" % (x,)) 
    
    # use the audio file as the audio source 
    
    r = sr.Recognizer() 
    
    with sr.AudioFile(AUDIO_FILE) as source: 
        #reads the audio file. Here we use record instead of 
        #listen 
        audio = r.record(source)   
    
    
    try:
        result = r.recognize_google(audio,language='th_TH')
    except sr.UnknownValueError:
        print("Error in Chunk File. continue other chunk !")
        continue
    
    try:
        with open(FILE_DIR+"/"+FILE_INPUT.split('.wav')[0]+".txt","a",encoding="utf-8") as f:
            f.write(result+ '\n') 
        print("%d. audio file is done from %d" % (x,counter)) 
    
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
    
    except sr.RequestError as e: 
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 


for i in range(1,counter):
    if os.path.exists(FILE_DIR+"/tmp/chunk%d.wav" % (i,)):
        os.remove(FILE_DIR+"/tmp/chunk%d.wav" % (i,))
    else:
        print("The file does not exist")
print("Files are deleted.")
print("Process completed.")
