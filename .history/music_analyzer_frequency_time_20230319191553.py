import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import datetime

# Set the filename for the audio file you want to analyze
filename = "my_audio_file.wav"

# Read the audio file and convert to a numeric signal
sampling_rate, data = wavfile.read(filename)

# Increase the sampling rate
new_sampling_rate = 44100
data = np.interp(np.arange(0, len(data), len(data)/new_sampling_rate), np.arange(0, len(data)), data).astype(np.int16)
sampling_rate = new_sampling_rate

# Perform Fourier transform to decompose the signal into sinusoidal waves
freq_domain = np.fft.fft(data)

# Find the amplitude and frequency of each sinusoidal wave
amplitude = np.abs(freq_domain)
frequency = np.fft.fftfreq(len(data), 1/sampling_rate)

# Set the time interval and time unit for plotting
start_time = 0.0
end_time = len(data) / sampling_rate
time_interval = 0.01  # time interval in seconds
time_unit = 's'

if time_interval < 1e-3:
    time_interval *= 1000
    time_unit = 'ms'
elif time_interval < 1:
    time_interval *= 1e6
    time_unit = 'us'

# Set the start and end indices based on the time interval
start_index = int(start_time * sampling_rate)
end_index = int(end_time * sampling_rate)

# Slice the time array using the same index
time = np.arange(start_index, end_index) / sampling_rate

# Slice the frequency array using the same index
frequency = frequency[start_index:end_index]

# Slice the amplitude array to match the length of the time array
amplitude = amplitude[start_index:end_index]

# Normalize the amplitude to the range [0,1]
amplitude_normalized = amplitude / np.max(amplitude)

# Set the y-axis range for the frequency axis
plt.ylim(0, 30000)

# Plot the results as a sinusoidal wave with time on the x-axis
fig, ax = plt.subplots()
ax.plot(time, amplitude_normalized)
ax.set_xlabel(f"Time ({time_unit})")
ax.set_ylabel("Amplitude")
ax.set_title("Audio Signal")

plt.show()
