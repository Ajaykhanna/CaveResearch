# Author: Coline Devin
# File created: April 1, 2014
#
# This file uses the normal coordinates of the molecule to determine the change
# in normal coordinates between states.

import numpy as np

def calcDQ(gsFreqCoords, exFreqCoords):
    """ Input is two lists of the form [eqCoords, (f1, f1coords), ... (fm, fm coords)]
        where the "coords" are lists of the form [x1, y1, z1, x2, y2,..., xn, yn, zn]
        for a molecule with n atoms and m vibrational modes. The ground state list
        comes first.
        Output is a list of length m in the form [dq1, dq2,... dqm]
    """

    # Make a list of lists [[x1_1, ...zn_1], ..., [x1_m, ..., zn_m]]
    gsListOfQCoords = [coords for (f, coords) in gsFreqCoords]
    exListOfQCoords = [coords for (f, coords) in exFreqCoords]
 
    # Convert lists into vectors
    gsEqCartCoords = np.array(gsFreqCoords[0])
    exEqCartCoords = np.array(exFreqCoords[0])

    gsQCoords = np.array(gsListOfQCoords)
    exQCoords = np.array(exListOfQCoords)

    changeCartCoords = gsEqCartCoords - exEqCartCoords

    dQArray = np.dot(exQCoords.T, changeCartCoords)
