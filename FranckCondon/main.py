import ParseFile as pf
import Dushinsky as d
import DiffFreqs as df
import Mode as m
import RecursiveModes as r
import Plots as p
import sys
import getopt
import optparse

if __name__ == "__main__":
    gsfile = ''
    exfile = ''
    E_electronic = 0
    threshold = 0
    graph = "none"
    myopts, args = getopt.getopt(sys.argv[1:], "i:f:e:t:F:g:o:")
    output = None 

    # o == option
    # a == argument passed to the o
    READ_FILE = 1
    for o, a in myopts:
        if o == '-i':
            gsfile=a
        if o == '-f':
            exfile=a
        elif o == '-e':
            E_electronic = float(a)
        elif o == '-t':
            threshold = float(a)
        elif o == '-F':
            READ_FILE = a
            print "Setting READ_FILE to", a
        elif o == '-g':
            graph = a
        elif o == '-o':
            output = a
        else:
            print(("Usage: %s -i initialStateFile -f finalStateFile" +
                   " -e E_Electronic -t threshold [-g [curve or stick]") % sys.argv[0])
 
    # Display input and output file name passed as the args
    print (("Initial state file : %s, Final state file : %s,"+
            " electronic energy : %f,"+
            "threshold : %f") % (gsfile, exfile, E_electronic, threshold) )
    
    dQ = 2.5
    if READ_FILE == 1:
        print "Read File is", READ_FILE
        (gsEq, gsFreqCoords) = pf.parseNormalCoordinates(gsfile)
        (exEq, exFreqCoords) = pf.parseNormalCoordinates(exfile)
        
        freqsAndDQs = d.calcDQ(gsEq, gsFreqCoords, exEq, exFreqCoords)
        print freqsAndDQs
        modes = [m.Mode(gsFreq, exFreq, dQ) for (gsFreq, exFreq, dQ) in 
                 freqsAndDQs]
        modes = modes

    else:
        #  modes = [m.Mode(507.64, 507.64,0.374722838/0.5291711), m.Mode(897.05, 897.05, -0.203348073/0.5291711)]
        modes = [m.Mode(897.05, 897.05, dQ)]
        E_electronic = 50406.3

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

    

   # for x in range(len(energies)):
   #     print "E: ", energies[x], " I: ", intensities[x]

    if graph == "stick":
        p.plotSticks(energies, intensities, gsfile + " -> " + exfile)
    elif graph == "curve":
        p.plotSpectrum(energies, intensities, skinny, gsfile + " -> " + exfile)
    print "Showing graph"
    raw_input("Press ENTER to exit ")
