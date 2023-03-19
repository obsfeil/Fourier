import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Set the filename of the audio file you want to analyze
filename = "my_audio_file.wav"

# Read the audio file and convert to a numerical signal
sampling_rate, data = wavfile.read(filename)

# Set the new sampling rate
new_sampling_rate = 98600

# Resample the data to the new sampling rate
data = np.interp(np.arange(0, len(data), len(data) / new_sampling_rate),
                 np.arange(0, len(data)), data).astype(np.int16)
sampling_rate = new_sampling_rate

# Perform Fourier transform to decompose the signal into sine waves
freq_domain = np.fft.fft(data)

# Find the amplitude and frequency of each sine wave
amplitude = np.abs(freq_domain)
frequency = np.fft.fftfreq(len(data), 1/sampling_rate)

# Define the time interval and time unit
time_interval = 0.01  # Time interval in seconds
time_unit = 's'

# Define the time period to plot
start_time = 0
end_time = 5  # Time period in seconds

# Convert the time period to the desired time unit
if time_unit == 's':
    start_index = int(start_time * sampling_rate)
    end_index = int(end_time * sampling_rate)
elif time_unit == 'ms':
    start_index = int(start_time * sampling_rate / 1000)
    end_index = int(end_time * sampling_rate / 1000)
elif time_unit == 'us':
    start_index = int(start_time * sampling_rate / 1e6)
    end_index = int(end_time * sampling_rate / 1e6)

# Slice the time array using the same index
time = np.arange(start_index, end_index) / sampling_rate

# Slice the frequency array using the same index
frequency = frequency[start_index:end_index]

# Slice the amplitude array to match the length of the time array
amplitude = amplitude[start_index:end_index]

# Plot the results as a line graph with time on the x-axis and frequency on the y-axis
fig, ax = plt.subplots()
ax.plot(time, frequency)
ax.set_xlabel(f"Time ({time_unit})")
ax.set_ylabel("Frequency (Hz)")
ax.set_xlim(start_time, end_time)
ax.set_ylim(0, np.max(frequency))
plt.show()
