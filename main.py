import speech_recognition as sr
import wave, os, glob
import subprocess
#  init recognizer
r = sr.Recognizer()

# list wave files

class audioProcessor:
  def __init__(self):
    # yet to implement
    return

  def textClassifications(**kwargs):
      print(kwargs)
      fullSring  = kwargs["textData"]
      # get Folder & File name
      tempFile = fullSring.split(' ', 1)
      folderName = tempFile[0]
      print(folderName)
      tempFile  = tempFile[1].split(' ', 1)
      fileName = tempFile[0] + ".txt"
      print( fileName )
      textToWrite = tempFile[1]
      print( textToWrite )
      filePath = folderName + "/" + fileName
      print(filePath)
      
      CHECK_FOLDER = os.path.isdir(folderName)
      FILE_EXISTS = os.path.isfile(filePath) 

      # If folder doesn't exist, then create it.
      if not CHECK_FOLDER:
          os.makedirs(folderName)
      # file not exist then create or append it.
      if FILE_EXISTS:
          # if Exists then append data
          f = open(filePath, "a")
          f.write(textToWrite)
          f.close()
      else:
          # if file not exits then create and write contents
          f = open(filePath, "w")
          f.write(textToWrite)
          f.close()
      
  def audioToText():
    path = 'audio'
    for filename in glob.glob(os.path.join(path, '*.wav')):
        # audio = wave.open(filename, 'r')
        print(filename)
        
        # Incase of mp4 to wave converts.
        # command = "ffmpeg -i C:/test.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav"
        # subprocess.call(command, shell=True)

        # continue working
        audioData = sr.AudioFile(filename)
        with audioData as source:
          audio = r.record(source)
          textData = r.recognize_google(audio)
          print(textData)
          # Call the function
          audioProcessor.textClassifications(textData = textData)
    
#  Entry point
if __name__ == '__main__':
  # a is Object
  a = audioProcessor
  # Call funcition to convet text
  a.audioToText()


