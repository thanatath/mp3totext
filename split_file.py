# Import necessary libraries 
from pydub import AudioSegment 
from pathlib import Path
from inputfile import FILE_INPUT, FILE_LOCATION, FILE_DIR, audio_wav
import os
print("File directory : ",FILE_DIR)
# Input audio file to be sliced 


audio = AudioSegment.from_wav(audio_wav)
 
# Length of the audiofile in milliseconds 
n = len(audio) 
  
# Variable to count the number of sliced chunks 
counter = 1
  
# Interval length at which to slice the audio file. 

interval = 60 * 1000
  
# Length of audio to overlap.  

overlap = 1.5 * 1000
  
# Initialize start and end seconds to 0 
start = 0
end = 0
  
# Flag to keep track of end of file. 
# When audio reaches its end, flag is set to 1 and we break 
flag = 0
  
# Iterate from 0 to end of the file, 
# with increment = interval 
for i in range(0, n, interval): 
    if i == 0: 
        start = 0
        end = interval 

    else: 
        start = end - overlap 
        end = start + interval  

    if end >= n: 
        end = n 
        flag = 1

    chunk = audio[start:end] 
    
    
    path = FILE_DIR+"/tmp"

    # Check whether the specified path exists or not
    isExist = os.path.exists(path)

    if not isExist:
    
        # Create a new directory because it does not exist 
        os.makedirs(path)
        print("The tmp directory is created!")
  
    # Filename / Path to store the sliced audio 
    filename = Path(FILE_DIR+"/tmp/chunk"+str(counter)+".wav")
    print("File name: ",filename)
    # Store the sliced audio file to the defined path 
    chunk.export(str(filename), format ="wav") 
    # Print information about the current chunk 
    print("Processing chunk "+str(counter)+". Start = "
                        +str(start)+" end = "+str(end)) 
  
    # Increment counter for the next chunk 
    counter = counter + 1

  
  

    
  