"""
Pipeline that construct AF history, run adaptation and evaluate results.
"""
# for visualizing the data
import matplotlib.pyplot as plt
# for opening the media file
from scipy.io import wavfile
# padasip for signal processing and ND tasks
import padasip as pa
import numpy as np


# load data
fs, audio = wavfile.read('rec02.wav')
plt.figure()
# create spectrogram
plt.specgram(audio, Fs=fs)
audio = audio[50000:]

#prepare af inputs
x = pa.input_from_history(audio, 50, bias=False)
# prepare af
adaptive_filter = pa.filters.AdaptiveFilter(model="NLMS", n=50, mu=1, w="random")
print(x.shape, audio[49:].shape)
y,e,w = adaptive_filter.run(audio[49:], x)

elbnd = pa.detection.ELBND(w, e, function="max")
le = pa.detection.learning_entropy(w, m=30, order=1)
ese = pa.detection.ESE(w)
plt.figure()
# ELBND plot

plt.plot(elbnd[50000:])
plt.figure()
plt.plot(le[50000:], "g")
plt.figure()
plt.plot(ese)
plt.show()