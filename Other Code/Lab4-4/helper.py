import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,2,4,6,8,10,12,14,16,18,20,24,26])
oneGram = np.array([0,27.794])
twoGram = np.array([0,24.740,15.754,20.791,24.868,27.783,32.817,41.092,45.042,50.159,54.159,57.134,63.022])
threeGram = np.array([0,15.856,19.757,24.740,38.751,42.816,47.847,14*60 + 2.693,14*60 + 26.746,14*60 + 36.728,15*60 + 16.829,15*60 + 53.915,20*60 + 19.331])

plt.plot([0,26],oneGram, label="unigram")
plt.plot(x,twoGram, label="bigram")
plt.plot(x,threeGram, label="trigram")
plt.title("RunTime Graphs")
plt.xlabel("No of Files (sorted by size)")
plt.ylabel("Runtime (s)")
plt.legend(loc='upper left')
plt.xlim(0,30)
plt.show()