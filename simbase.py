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

        if self.random:
            self.timebase = np.linspace(0, self.n_sine * 100 , self.n_sine * 100)
            pure_samples = np.random.sample(self.n_sine * 100)

            i = 0
            for x in range(0, self.n_sine * 100, 100):
                if 0 <= i <= 2:
                    pure_samples[x:x + 100] = pure_samples[x:x + 100] * 0.25 + 0.375
                elif i == 5:
                    i = -1
                i = i + 1

            pure_samples = (pure_samples - 0.5) * 2
        else:
            self.timebase = np.linspace(-self.n_sine * np.pi, self.n_sine * np.pi, self.n_sine * 1500)
            pure_samples = np.sin(self.timebase)

        samples = np.copy(pure_samples)

        for (index,), value in np.ndenumerate(samples):
            samples[index] = self.process(value)

        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)

        original, = self.ax.plot(self.timebase, pure_samples, label='Original')
        processed, = self.ax.plot(self.timebase, samples, label='Processed', alpha = 0.9)

        self.post_simulation()

        self.ax.legend(handles=[processed, original] + self.legends)
        self.ax.set_title(self.name)
        self.ax.axhline(0, color='k')
        self.figure.show()


    def post_simulation(self):
        pass




