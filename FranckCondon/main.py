import ParseFile as pf
import Dushinsky as d

(gsEq, gsFreqCoords) = pf.parseNormalCoordinates("InputFiles/ccl2_gs_mbpt_freq.normco.new")
(exEq, exFreqCoords) = pf.parseNormalCoordinates("InputFiles/ccl2_cation_mbpt_freq.normco.new")

dQ = d.calcDQ(gsEq, gsFreqCoords, exEq, exFreqCoords)
print dQ
