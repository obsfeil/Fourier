import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import math

# Sett inn filnavn for lydfilen du vil analysere
filename = "my_audio_file.wav"

# Les inn lydfilen og konverter til numerisk signal
sampling_rate, data = wavfile.read(filename)

# Begrens antall datapunkter til ett sekund av lyddataen
data = data[:sampling_rate]
frequency = np.fft.fftfreq(len(data), 10/sampling_rate)

# Øk samplingsfrekvensen
new_sampling_rate = 44100
data = np.interp(np.arange(0, len(data), len(data)/new_sampling_rate), np.arange(0, len(data)), data).astype(np.int16)
sampling_rate = new_sampling_rate

# Gjennomfør Fourier-transformasjon for å dekomponere signalet til sinus-bølger
freq_domain = np.fft.fft(data)

# Finn amplituden og frekvensen til hver sinus-bølge
amplitude = np.abs(freq_domain)
frequency = np.fft.fftfreq(len(data), 1/sampling_rate)

# Plot resultatene som en sinus-kurve med tidslinje på x-aksen
fig, ax = plt.subplots()
ax.plot(np.arange(0, len(data)/sampling_rate, 1/sampling_rate), amplitude)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Frequency (Hz)")
plt.show()
