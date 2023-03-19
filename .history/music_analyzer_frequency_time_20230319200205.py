import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Set the file name of the audio file you want to analyze
filename = "my_audio_file.wav"

# Set the desired sample rate
samplerate = 96000

# Read in the audio file and convert to numerical signal
sampling_rate, data = wavfile.read(filename)

# Resample the audio to the desired sample rate
data = np.interp(np.linspace(0, len(data), int(len(data) * samplerate / sampling_rate)), np.arange(len(data)), data)

# Calculate the frequency domain of the signal using Fourier transform
freq_domain = np.fft.fft(data)

# Calculate the amplitude and frequency of each sinusoidal wave
amplitude = np.abs(freq_domain)
frequency = np.fft.fftfreq(len(data), 1/samplerate)

# Create a timeline based on the sample rate
time = np.arange(0, len(data)/samplerate, 1/samplerate)

# Set the time period to display (in seconds)
start_time = 10
end_time = 11

# Find the indices of the time period to display
start_index = int(start_time * samplerate)
end_index = int(end_time * samplerate)

# Plot the sinusoidal waves
fig, ax = plt.subplots()
ax.plot(time[start_index:end_index], frequency[start_index:end_index])
ax.set_xlabel('Time (s)')
ax.set_ylabel('Frequency (Hz)')
plt.show()
