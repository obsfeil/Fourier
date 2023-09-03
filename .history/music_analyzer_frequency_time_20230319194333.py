import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Set the filename for the audio file you want to analyze
filename = "my_audio_file.wav"

# Read in the audio file and convert it to a numerical signal
sampling_rate, data = wavfile.read(filename)

# Set the time period you want to analyze in seconds
timeperiod = 1

# Get the number of samples to use for the analysis
samples = int(timeperiod * sampling_rate)

# Take a slice of the data for the analysis
data_slice = data[:samples]

# Perform a Fourier transformation to decompose the signal into sinusoidal waves
freq_domain = np.fft.fft(data_slice)

# Get the amplitude and frequency of each sinusoidal wave
amplitude = np.abs(freq_domain)
frequency = np.fft.fftfreq(len(data_slice), 1/sampling_rate)

# Create a timeline based on the sampling rate
time = np.arange(0, len(data_slice)/sampling_rate, 1/sampling_rate)

# Create a plot showing the amplitude of each frequency component over time
plt.figure(figsize=(10, 5))
plt.plot(time, frequency, amplitude)
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.show()
