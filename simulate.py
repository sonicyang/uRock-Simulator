import distortion

overdrive = distortion.overdrive_sigmoid(2)
distor1 = distortion.distortion_threshold(2)
distor2 = distortion.distortion_amplification(2)

overdrive .simulate()
distor1.simulate()
distor2.simulate()

try:
    input("Press Enter to continue...")
except:
    pass
