import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import datetime

# Set the filename of the audio file you want to analyze
filename = "my_audio_file.wav"

# Read in the audio file and convert to a numeric signal
sampling_rate, data = wavfile.read(filename)

# Resample the signal to increase the sampling rate
new_sampling_rate = 44100
data = np.interp(np.arange(0, len(data), len(data)/new_sampling_rate), np.arange(0, len(data)), data).astype(np.int16)
sampling_rate = new_sampling_rate

# Perform Fourier transform to decompose the signal into sinusoidal waves
freq_domain = np.fft.fft(data)

# Calculate the amplitude and frequency of each sinusoidal wave
amplitude = np.abs(freq_domain)
frequency = np.fft.fftfreq(len(data), 1/sampling_rate)

# Define the time interval to plot (from start_time to end_time in time_unit)
start_time = 0
end_time = len(data) / sampling_rate
time_interval = 0.01  # time interval in seconds

# Define the units for the x-axis labels based on the time interval
if time_interval >= 1:
    time_unit = 's'
    time_scale = 1
elif time_interval >= 1e-3:
    time_unit = 'ms'
    time_scale = 1000
else:
    time_unit = 'us'
    time_scale = 1e6

# Define the start and end indices based on the start and end times
start_index = int(start_time * sampling_rate)
end_index = int(end_time * sampling_rate)

# Slice the frequency and amplitude arrays based on the start and end indices
frequency = frequency[start_index:end_index]
amplitude = amplitude[start_index:end_index]

# Plot the results as a line plot with time on the x-axis and frequency on the y-axis
fig, ax = plt.subplots()
ax.plot(np.arange(start_index, end_index)/sampling_rate*time_scale, frequency)
ax.set_xlabel(f"Time ({time_unit})")
ax.set_ylabel("Frequency (Hz)")
plt.show()
