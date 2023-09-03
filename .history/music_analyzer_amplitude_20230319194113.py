import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Set the filename and desired time unit and period
filename = "my_audio_file.wav"
time_unit = "s"  # or "ms" or "us"
time_period = 1  # in units of the chosen time unit

# Read in the audio file and convert to numerical signal
sampling_rate, data = wavfile.read(filename)

# Perform Fourier transform to decompose the signal into sinusoidal waves
freq_domain = np.fft.fft(data)

# Find the amplitude and frequency of each sinusoidal wave
amplitude = np.abs(freq_domain)
frequency = np.fft.fftfreq(len(data), 1/sampling_rate)

# Create a timeline based on the sampling rate and chosen time unit
if time_unit == "s":
    time = np.arange(0, len(data)/sampling_rate, 1/sampling_rate)
    xlabel = "Time (s)"
elif time_unit == "ms":
    time = np.arange(0, len(data)/sampling_rate, 1/sampling_rate) * 1000
    xlabel = "Time (ms)"
elif time_unit == "us":
    time = np.arange(0, len(data)/sampling_rate, 1/sampling_rate) * 1000000
    xlabel = "Time (us)"
else:
    raise ValueError("Invalid time unit")

# Plot the amplitude as a function of time
plt.figure(figsize=(10, 5))
plt.plot(time[::time_period], amplitude[::time_period])
plt.xlabel(xlabel)
plt.ylabel("Amplitude")
plt.grid()
plt.show()
