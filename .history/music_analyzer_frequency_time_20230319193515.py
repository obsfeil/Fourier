import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

# Load the wav file
samplerate, data = wavfile.read("my_audio_file.wav")

# Define time unit and period
time_unit = 1 # 1 second
time_period = 5 # 5 seconds

# Calculate the number of samples to take for the given time period
num_samples = int(time_period * samplerate)

# Take the subset of the data for the given time period
subset_data = data[:num_samples]

# Calculate the time array based on the subset of data
time = np.arange(len(subset_data)) / samplerate

# Calculate the Fourier transform of the subset of data
frequency = np.fft.fft(subset_data)

# Take the absolute value of the complex numbers to get the magnitude of the frequencies
frequency = np.abs(frequency)

# Calculate the frequencies corresponding to the Fourier transform
freqs = np.fft.fftfreq(subset_data.size, 1/samplerate)

# Take only the positive frequencies
positive_freqs = freqs[:freqs.size//2]

# Plot the frequency vs time
fig, ax = plt.subplots()
ax.plot(time, positive_freqs[:len(time)])

# Set the axis labels
ax.set_xlabel('Time (s)')
ax.set_ylabel('Frequency (Hz)')

# Show the plot
plt.show()
