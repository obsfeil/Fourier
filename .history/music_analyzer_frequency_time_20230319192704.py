import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import stft

# read audio file
sample_rate, data = wavfile.read('my_audio_file.wav')

# convert audio data to mono
if len(data.shape) > 1:
    data = data.sum(axis=1) / 2

# set time unit and time period
time_unit = 1/sample_rate
time_period = 1

# calculate the length of each segment
nperseg = int(time_period/time_unit)

# calculate the frequency resolution
freq_res = sample_rate/nperseg

# calculate the number of segments
n_segments = int(np.ceil(len(data)/nperseg))

# perform short-time Fourier transform
f, t, Zxx = stft(data, fs=sample_rate, nperseg=nperseg, noverlap=0, nfft=nperseg)

# calculate the power spectral density
psd = np.abs(Zxx)**2/nperseg

# sum the power spectral density over each segment
psd_sum = np.sum(psd, axis=1)

# calculate the frequency corresponding to each segment
frequency = np.arange(len(psd_sum))*freq_res

# plot the results
fig, ax = plt.subplots()
ax.plot(t, frequency)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Frequency (Hz)')
ax.set_ylim([0, sample_rate/2]) # type: ignore
plt.show()
