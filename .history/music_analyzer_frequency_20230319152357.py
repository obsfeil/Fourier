import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Sett inn filnavn for lydfilen du vil analysere
filename = "my_audio_file.wav"

# Les inn lydfilen og konverter til numerisk signal
sampling_rate, data = wavfile.read(filename)

# Gjennomfør Fourier-transformasjon for å dekomponere signalet til sinus-bølger
freq_domain = np.fft.fft(data)

# Finn amplituden og frekvensen til hver sinus-bølge
amplitude = np.abs(freq_domain)
frequency = np.fft.fftfreq(len(data), 1/sampling_rate)

# Lag en array med tidspunktene for hvert datapunkt i signalet
time = np.arange(0, len(data)) / sampling_rate

# Hvis du vil justere størrelsen på plottet eller utseendet, 
# kan du gjøre dette ved å legge til flere funksjonskall i koden, 
# for eksempel 
# plt.figure(figsize=(10, 5)) 
# for å sette størrelsen på plottet eller 
plt.grid() 
# for å legge til rutenett.

# Plot resultatene som en sinus-kurve
plt.plot(time, frequency, label="Frequency")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.legend()
plt.show()
