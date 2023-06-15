from pydub import AudioSegment
audio=AudioSegment.from_wav("output.wav")

audio=audio+50
audio=audio*2
audio=audio.fade_in(2000)
audio.export("converted.mp3",format="mp3")