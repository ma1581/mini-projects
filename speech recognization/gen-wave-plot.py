# https://learnpython.com/blog/plot-waveform-in-python/
import wave
import numpy as np
import matplotlib.pyplot as plt


#create and open the file as a object
wav_obj = wave.open('output.wav', 'r')


#get audio parameter
framerate = wav_obj.getframerate()
print(framerate)
sampframe = wav_obj.getnframes()
print(sampframe)
duration = sampframe/framerate
print(duration, "seconds")
audiobit = wav_obj.readframes(sampframe)

#this array is for y axis paramter to take the audiobit and store it as 16 bit integer in the array
signal_array = np.frombuffer(audiobit, dtype=np.int16)
#print(signal_array.shape)
# for stereo:
#l_channel = signal_array[0::2]
#r_channel = signal_array[1::2]

#this array takes the start and end of audio duration along with the number of frames (sample frame)
times = np.linspace(0, duration, num=sampframe)

#plot configuration
#size of graph
plt.figure(figsize=(15, 5))
#plot axis parameter
plt.plot(times, signal_array)
#plot title
plt.title('Audio')
#plot label on x axis
plt.ylabel('Signal Value')
#plot label on y axis
plt.xlabel('Time (s)')
#plot limit(range) on x axis
plt.xlim(0, duration)
#display the plot
plt.show()

#size of graph
plt.figure(figsize=(15, 5))

plt.specgram(signal_array, Fs=framerate, vmin=-20, vmax=50)
plt.title('Left Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, duration)
#displays a color bar on side
plt.colorbar()
plt.show()