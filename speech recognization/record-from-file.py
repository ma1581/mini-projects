import wave

filename=input("Enter file name audio:")
filename=filename+".wav"
ob=wave.open(filename,"rb")
c=ob.getnchannels()
w=ob.getsampwidth()
fr=ob.getframerate()
f=ob.readframes(-1)
ob.close()


wf = wave.open("rep.wav", 'wb')
wf.setnchannels(c)
wf.setsampwidth(w)
wf.setframerate(fr)
wf.writeframes(f)
wf.close()