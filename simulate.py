import distortion

distor1 = distortion.distortion_threshold(2)
distor2 = distortion.distortion_amplification(2)
distor3 = distortion.distortion_sigmoid(2)

distor1.simulate()
distor2.simulate()
distor3.simulate()

try:
    input("Press Enter to continue...")
except:
    pass
