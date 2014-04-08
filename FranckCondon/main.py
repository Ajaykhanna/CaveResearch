import ParseFile as pf
import Dushinsky as d
import DiffFreqs as df
import Mode as m
import RecursiveModes as r
import Plots as p
import sys
import getopt

if __name__ == "__main__":
    gsfile = ''
    exfile = ''
    E_electronic = 0
    threshold = 0

    myopts, args = getopt.getopt(sys.argv[1:], "i:f:e:t:")

    # o == option
    # a == argument passed to the o

    for o, a in myopts:
        if o == '-i':
            gsfile=a
        if o == '-f':
            exfile=a
        elif o == '-e':
            E_electronic = float(a)
        elif o == '-t':
            threshold = float(a)
        else:
            print(("Usage: %s -i initialStateFile -f finalStateFile" +
                   " -e E_Electronic -t sys") % sys.argv[0])
 
    # Display input and output file name passed as the args
    print (("Initial state file : %s, Final state file : %s, electronic energy : %f,"+
            "threshold : %f") % (gsfile, exfile, E_electronic, threshold) )
    
    
    (gsEq, gsFreqCoords) = pf.parseNormalCoordinates(gsfile)
    (exEq, exFreqCoords) = pf.parseNormalCoordinates(exfile)

    freqsAndDQs = d.calcDQ(gsEq, gsFreqCoords, exEq, exFreqCoords)
    print freqsAndDQs
    modes = [m.Mode(gsFreq, exFreq, dQ) for (gsFreq, exFreq, dQ) in freqsAndDQs]

    for m in modes:
        print "Frequency: ", m.groundFreqWN
        m.computeFranckCondons(range(11), 0)
        print "FCs", m.FrankCondons

    print("Found %d modes" % (len(modes)))

    (energies, intensities, numpoints)  = r.genMultiModePoints(
        threshold, modes, E_electronic, 11)
    
    print "E len", len(energies), "I len", len(intensities)
    
    wide = [0.01]*numpoints
    med = [0.005]*numpoints
    skinny = [0.001]*numpoints
    
    energies.reverse()
    intensities.reverse()
    print("Found %d intensities" % len(intensities))

    #print intensities
    
    #get the gaussians
   # points = p.genSpectrum(energies, intensities, skinny)
    
    points = [energies, intensities]
    #for x in range(len(energies)):
    #    print "E: ", energies[x], " I: ", intensities[x]
    #p.plotSpectrum(points[0], points[1], "N Modes")
    p.plotSticks(points[0], points[1], "%d Modes" % len(modes))
    raw_input("Press ENTER to exit ")
