import DiffFreqs as DF
import SimpleOscillator as SO

print "SO, <1|0>", SO.overlap(1, 0)
print "DF, <1|0>", DF.diffFreqOverlap([1, 450], [0, 550])
