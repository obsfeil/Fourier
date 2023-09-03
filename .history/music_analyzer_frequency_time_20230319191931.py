import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Set the file name of the audio file you want to analyze
filename = "my_audio_file.wav"

# Read in the audio file and convert it to a numeric signal
sampling_rate, data = wavfile.read(filename)

# Perform Fourier transformation to decompose the signal into sine waves
freq_domain = np.fft.fft(data)

# Calculate the amplitude and frequency of each sine wave
amplitude = np.abs(freq_domain)
frequency = np.fft.fftfreq(len(data), 1/sampling_rate)

# Set the time interval and unit to plot (here from 0 to the duration of the audio file in the desired time unit)
start_time = 0
end_time = len(data) / sampling_rate
time_interval = 0.001 # time interval in seconds, change as needed
time_unit = "s"

if time_interval >= 1:
    time_scale = 1
elif time_interval >= 1e-3:
    time_scale = 1000
    time_unit = "ms"
else:
    time_scale = 1e6
    time_unit = "us"

# Set the start and end indices for the time interval to plot
start_index = int(start_time * sampling_rate)
end_index = int(end_time * sampling_rate)

# Slice the frequency and amplitude arrays to match the length of the time array
frequency = frequency[start_index:end_index]
amplitude = amplitude[start_index:end_index]

# Set the y-axis range to show frequencies up to half the sampling rate
plt.ylim(0, sampling_rate/2)

# Plot the results as a frequency spectrum with time on the x-axis
fig, ax = plt.subplots()
ax.plot(frequency, amplitude)
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Amplitude")
ax.set_xlim(0, sampling_rate/2)
plt.show()
