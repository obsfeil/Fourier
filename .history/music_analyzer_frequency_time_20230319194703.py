import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Sett inn filnavn for lydfilen du vil analysere
filename = "my_audio_file.wav"

# Les inn lydfilen og konverter til numerisk signal
sampling_rate, data = wavfile.read(filename)

# Choose start and stop time periods (in seconds)
start_time = 1
stop_time = 2

# Extract the portion of the data within the chosen time period
start_index = int(start_time * sampling_rate)
stop_index = int(stop_time * sampling_rate)
data = data[start_index:stop_index]

# Gjennomfør Fourier-transformasjon for å dekomponere signalet til sinus-bølger
freq_domain = np.fft.fft(data)

# Finn amplituden og frekvensen til hver sinus-bølge
amplitude = np.abs(freq_domain)
frequency = np.fft.fftfreq(len(data), 1/sampling_rate)

# Lag en tidslinje basert på sampling raten
time = np.linspace(start_time, stop_time, num=len(data))

# Her har jeg lagt til en tidslinje time basert på sampling raten, 
# og lagt denne som x-aksen i plottet sammen med frekvensen på y-aksen. 

# Hvis du vil justere størrelsen på plottet eller utseendet, 
# kan du gjøre dette ved å legge til flere funksjonskall i koden, 
# for eksempel 
plt.figure(figsize=(10, 5)) 
# for å sette størrelsen på plottet eller 
plt.grid() 
# for å legge til rutenett.
# Plot resultatene som en sinus-kurve
plt.plot(time, frequency)
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.show()
