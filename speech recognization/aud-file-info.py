import wave
import pyaudio
filename=input("Enter the filename of the audio:")
filename=filename+".wav"
ob=wave.open(filename,"rb")
print("The channel in this file is ",ob.getnchannels())
print("The width in this file is ",ob.getsampwidth())
print("The frame in this file is ",ob.getnframes())
print("The rate in this file is ",ob.getframerate())
print("The time in this file is ",ob.getnframes()/ob.getframerate())
ob.close()


