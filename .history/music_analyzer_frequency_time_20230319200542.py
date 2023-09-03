import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Set input file name and read audio data
filename = "my_audio_file.wav"
sampling_rate, audio_data = wavfile.read(filename)

# Define start and stop times (in seconds)
start_time = 0
stop_time = len(audio_data) / sampling_rate

# Define time scale (in seconds)
time_scale = 1 / sampling_rate

# Define time period (in seconds)
time_period = 1

# Calculate number of samples in each time period
num_samples = int(time_period / time_scale)

# Create empty arrays to store frequency and time data
frequencies = []
times = []

# Iterate over audio data, calculating frequency and time for each time period
for i in range(start_time, stop_time, time_period):
    # Calculate frequency for each time period
    freq_domain = np.fft.fft(audio_data[i:i+num_samples])
    freq = np.abs(freq_domain[:num_samples//2])
    freq = freq / np.max(freq) # Normalize amplitude
    freq = freq[:int(len(freq)/2)] # Discard frequencies higher than the Nyquist frequency
    frequency = np.linspace(0, sampling_rate/2, len(freq))
    frequencies.append(frequency)
    
    # Calculate time for each time period
    time = np.linspace(i, i+time_period, num_samples)
    times.append(time)
    
# Convert lists of frequency and time data into arrays
frequencies = np.concatenate(frequencies)
times = np.concatenate(times)

# Create plot of frequency as a function of time
plt.plot(times, frequencies)
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.show()
