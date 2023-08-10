"""
Spectrogram for fast possible results check.
"""
# for visualizing the data
import matplotlib.pyplot as plt
# for opening the media file
from scipy.io import wavfile

fs, audio = wavfile.read('rec03.wav')
plt.specgram(audio, Fs=fs)
plt.show()
