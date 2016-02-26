import distortion
import compressor

overdrive = distortion.overdrive_sigmoid(2)
distor1 = distortion.distortion_threshold(2)
distor2 = distortion.distortion_amplification(2)
compressor1 = compressor.compressor()
compressor2 = compressor.compressor_attack()

# overdrive .simulate()
# distor1.simulate()
# distor2.simulate()
compressor1.simulate()
compressor2.simulate()

try:
    input("Press Enter to exit...")
except:
    pass
