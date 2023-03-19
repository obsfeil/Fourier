import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import sys

# read in the wave file
samplerate, data = wavfile.read(sys.argv[1])

# set up time array based on the duration of the sound file
duration = len(data) / samplerate
time = np.linspace(0, duration, len(data))

# compute FFT of the data
fft = np.fft.fft(data)

# compute frequency array
freqs = np.fft.fftfreq(len(data)) * samplerate

# keep only the positive frequencies
positive_freqs = freqs[:len(freqs)//2]
fft = fft[:len(fft)//2]

# plot the frequency spectrum over time
fig, ax = plt.subplots()
ax.set_xlabel('Time (s)')
ax.set_ylabel('Frequency (Hz)')
ax.set_xlim([0, duration]) # type: ignore

time_unit = 1 # in seconds
time_period = 5 # in seconds

for i in range(0, len(data) - samplerate*time_period, samplerate*time_period*time_unit):
    spectrum = np.abs(fft[i:i+samplerate*time_period])
    ax.plot(time[i:i+samplerate*time_period], positive_freqs[:len(spectrum)], label=f'Time: {i/samplerate:.2f}s - {i/samplerate+samplerate*time_period:.2f}s')

ax.legend()
plt.show()

