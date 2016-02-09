import simbase

class distortion(simbase.simulation):
    def __init__(self, n_sine):
        super(distortion, self).__init__(n_sine)

        self.name = "Distortion"
        self.threshold = 0.5

    def process(self, sample):
        if abs(sample) > self.threshold:
            sample = sample / abs(sample) * self.threshold
        return sample

    def post_simulation(self):
        hline1 = self.ax.axhline(0.5, color='r', ls='dashed', label='Threshold')
        self.ax.axhline(-0.5, color='r', ls='dashed', label='Threshold')

        self.legends = [hline1]
