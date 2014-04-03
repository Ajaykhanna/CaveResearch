import ParseFile as pf
import Dushinsky as d
import DiffFreqs as df
import Mode as m
import RecursiveModes as r
import Plots as p

(gsEq, gsFreqCoords) = pf.parseNormalCoordinates("InputFiles/ccl2_gs_mbpt_freq.normco.new")
(exEq, exFreqCoords) = pf.parseNormalCoordinates("InputFiles/ccl2_cation_mbpt_freq.normco.new")

freqsAndDQs = d.calcDQ(gsEq, gsFreqCoords, exEq, exFreqCoords)
modes = [m.Mode(gsFreq, exFreq, dQ) for (gsFreq, exFreq, dQ) in freqsAndDQs]

E_electronic = 0.05
threshold = 0.0001
(energies, intensities, numpoints)  = r.genMultiModePoints(threshold, modes, E_electronic, 11)

print "E len", len(energies), "I len", len(intensities)

wide = [0.01]*numpoints
med = [0.005]*numpoints
skinny = [0.001]*numpoints

energies.reverse()
intensities.reverse()

#get the gaussians
#points = p.genSpectrum(energies, intensities, skinny)

points = [energies, intensities]
# for x in range(len(energies)):
#     print "E: ", energies[x], " I: ", intensities[x]x
#p.plotSpectrum(points[0], points[1], "N Modes")
p.plotSticks(points[0], points[1], "N Modes")
raw_input("Press ENTER to exit ")
