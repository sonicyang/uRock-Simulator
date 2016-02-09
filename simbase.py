import numpy as np
import matplotlib.pylab as plt

class simulation(object):
    def __init__(self, n_sine, random_amp=False):
        self.n_sine = n_sine
        self.random = random_amp
        self.name = "Pure"

    def process(self, sample):
        pass

    def simulate(self):
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




