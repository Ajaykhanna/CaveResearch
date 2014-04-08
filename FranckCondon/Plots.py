import DiffFreqs as DF
import matplotlib as mpl
import matplotlib.pyplot as plt
import Gaussian as G
import numpy as np

plt.ion()
def genSpectrum(energies, intensities, widths):
    """ Gaussianifies the points on the spectrum using the input widths
    """
    energyRange = np.arange(0, energies[len(energies)-1]*2, energies[0]/1000)
    intensityRange = [0]*len(energyRange)

    # for i in range(len(energies)):
#         print "E: ", energies[i], " I: ", intensities[i]
    for i in range(0,len(energies)):
        gauss = G.gaussianGenerator(intensities[i], widths[i], energies[i])
        for x in range(len(energyRange)):
            intensityRange[x] += gauss(energyRange[x])

    ypoints = [gauss(x) for x in energyRange]
    print "Number of points to plot:", len(energyRange)
    return [energyRange, intensityRange]

# def plotProbs(probs, deltaE, widths):
#     energies = L[0]
#     intensities = L[1]
#     energyRange = np.arange(0, energies[len(energies)-1]*2, energies[0]/10)
#     intensityRange = [0]*len(energyRange)
#     for x in intensities:
#         print x
#     for i in range(0,11):
#         gauss = G.gaussianGenerator(intensities[i], widths[i], energies[i])
#         for x in range(len(energyRange)):
#             intensityRange[x] += gauss(energyRange[x])

def plotSticks(xpoints, ypoints, title):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel("Energies")
    ax.set_ylabel("Intensities")
    ax.bar(xpoints, ypoints, 0.0003) # last input is bar width
    #plt.ylim([0, max(ypoints)])
    plt.draw()
    plt.show()

def plotSpectrum(xpoints, ypoints, title):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel("Energies")
    ax.set_ylabel("Intensities")
    p = ax.plot( xpoints, ypoints)
    plt.ylim([0, max(ypoints)])
    plt.draw()
    plt.show()

