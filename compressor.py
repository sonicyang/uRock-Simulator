import simbase

class compressor(simbase.simulation):
    def __init__(self):
        super(compressor, self).__init__(15, True)

        self.name = "Compressor with 1:2 Ratio"

        self.ratio = 2
        self.threshold = 0.5
        return

    def process(self, sample):
        if abs(sample) > 0.5:
            sample = sample / 2
        return sample

    def post_simulation(self):
        hline1 = self.ax.axhline(self.threshold, color='r', ls='dashed', label='Threshold')
        self.ax.axhline(-self.threshold, color='r', ls='dashed', label='Threshold')

        self.legends.append(hline1)
        return

class compressor_attack(simbase.simulation):
    def __init__(self):
        super(compressor_attack, self).__init__(15, True)

        self.name = "Compressor with 1:2 Ratio"

        self.ratio = 2
        self.threshold = 0.5
        self.attack = 100

        self.stat = 0
        self.direction = 1
        return

    def process(self, sample):
        if self.stat == 0:
            if abs(sample) > self.threshold + 0.1:
                self.stat == 1
                self.direction = 1

        elif self.attack > self.stat >= 1:
            if self.direction == 1 and abs(sample) > self.threshold:
                self.stat += 1
            else:
                self.direction = -1

            if self.direction == -1 and abs(sample) < self.threshold:
                self.stat -= 1
            else:
                self.direction = 1

            sample = sample / (self.ratio * self.stat / self.attack)
        elif self.stat >= self.attack:
            if abs(sample) < self.threshold - 0.1:
                self.stat -= 1
                self.direction = -1

            sample = sample / self.ratio
        return sample

    def post_simulation(self):
        hline1 = self.ax.axhline(self.threshold, color='r', ls='dashed', label='Threshold')
        self.ax.axhline(-self.threshold, color='r', ls='dashed', label='Threshold')

        self.legends.append(hline1)
        return
