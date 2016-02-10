import numpy as np
import matplotlib.pylab as plt
from pylab import*
from scipy.io import wavfile

class simulation(object):
    def __init__(self, n_sine, random_amp=False):
        self.n_sine = n_sine
        self.random = random_amp
        self.name = "Pure"
        self.legends = []

    def process(self, sample):
        pass

    def simulate(self):
        sampFreq, snd = wavfile.read('sample.wav')
        snd = snd / (2.**15)

        for index, value in np.ndenumerate(snd):
            snd[index[0]][index[1]] = self.process(value)

        wavfile.write(self.name + '.wav', sampFreq, snd)

        self.timebase = np.linspace(-self.n_sine * np.pi, self.n_sine * np.pi, 3000)

        pure_samples = np.sin(self.timebase)
        samples = np.sin(self.timebase)

        for (index,), value in np.ndenumerate(samples):
            samples[index] = self.process(value)

        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)

        processed, = self.ax.plot(self.timebase, samples, label='Processed')
        original, = self.ax.plot(self.timebase, pure_samples, label='Original')

        self.post_simulation()

        self.ax.legend(handles=[processed, original] + self.legends)
        self.ax.set_title(self.name)
        self.figure.show()


    def post_simulation(self):
        pass




