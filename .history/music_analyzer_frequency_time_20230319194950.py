import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Set the filename of the audio file to analyze
filename = "my_audio_file.wav"

# Read in the audio file and convert to numerical signal
sampling_rate, data = wavfile.read(filename)

# Get user input for the start and stop times of the time period to analyze
start_time = float(input("Enter the start time (in seconds): "))
stop_time = float(input("Enter the stop time (in seconds): "))

# Find the index of the start and stop times in the data array
start_index = int(start_time * sampling_rate)
stop_index = int(stop_time * sampling_rate)

# Get the subset of the data to analyze based on the start and stop times
data_subset = data[start_index:stop_index]

# Perform Fourier transformation to decompose the signal into sine waves
freq_domain = np.fft.fft(data_subset)

# Find the amplitude and frequency of each sine wave
amplitude = np.abs(freq_domain)
frequency = np.fft.fftfreq(len(data_subset), 1/sampling_rate)

# Create a timeline based on the sampling rate
time = np.linspace(start_time, stop_time, len(data_subset))

# Plot the results as a frequency vs. time spectrogram
plt.specgram(data_subset, Fs=sampling_rate)
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.show()
