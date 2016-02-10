import simbase

class distortion_threshold(simbase.simulation):
    def __init__(self, n_sine):
        super(distortion_threshold, self).__init__(n_sine)

        self.name = "Distortion Threshold Method"
        self.threshold = 0.05
        return

    def process(self, sample):
        if abs(sample) > self.threshold:
            sample = sample / abs(sample) * self.threshold
        return sample

    def post_simulation(self):
        hline1 = self.ax.axhline(self.threshold, color='r', ls='dashed', label='Threshold')
        self.ax.axhline(-self.threshold, color='r', ls='dashed', label='Threshold')

        self.legends.append(hline1)
        return

class distortion_amplification(simbase.simulation):
    def __init__(self, n_sine):
        super(distortion_amplification, self).__init__(n_sine)

        self.name = "Distortion Amplification Method"
        self.gain = 10.0

        return

    def process(self, sample):
        sample = sample * self.gain
        if abs(sample) > 1:
            sample = sample / abs(sample)
        return sample

    def post_simulation(self):
        return

class distortion_sigmoid(simbase.simulation):
    def __init__(self, n_sine):
        super(distortion_sigmoid, self).__init__(n_sine)

        self.name = "Distortion Sigmoid Method"
        self.gain = 10
        self.sigmoid_function = self.fast_sigmoid
        return

    def process(self, sample):
        sample = sample * self.gain

        return self.fast_sigmoid(sample)

    def post_simulation(self):
        return

    def fast_sigmoid(self, sample):
        return sample / (1 + abs(sample))
