"""
- The experimental data for $^{105}$Pd nucleus
- Data extracted from https://www.nndc.bnl.gov/ensdf/
- Data are provided through the work: 96Zr(13C,4nγ):XUNDL-3 [2019Ti02] (unevaluated)
"""


class Tools:
    @staticmethod
    def ExtractSpins(raw_string):
        # separate all the spins by the commmas
        extracted_spins = raw_string.split(',')
        # only get the integer part after splitting is done
        # with the integer part determined, compute the numerical values of each spins
        spins = [float(x[:-2]) / 2 for x in extracted_spins]

        return spins


class Band_B:
    """
    - the collection of energies belonging to the rotational structure B
    - it represents the band built on the neutron h=11/2
    - signature: \alpha=+1/2
    - negative parity spin states: \pi=-1
    """

    band_B_energies = [8405, 7190, 6071, 4952, 3800, 2700, 1742, 970, 489]
    """ the absolute energies """
    band_B_spins = '41/2,37/2,33/2,29/2,25/2,21/2,17/2,13/2'
    """ the absolute spins """
    band_B_transitions = [1302, 1148, 1064, 1089, 918, 814, 604]
    """ the in-band transition energies (DeltaI=2) """


class Band_A:
    """
    - the collection of energies belonging to the rotational structure A
    - it represents the YRAST band built on the neutron h = 11 / 2
    - signature: \alpha = -1 / 2
    - negative parity spin states: \pi=-1
    """

    band_A_energies = [8405, 7190, 6071, 4952, 3800, 2700, 1742, 970, 489]
    """ the absolute energies """
    band_A_spins = '43/2,39/2,35/2,31/2,27/2,23/2,19/2,15/2,11/2'
    """ the absolute spins """
    band_A_transitions = [1215, 1119, 1119, 1152, 1100, 958, 481]
    """ the in-band transition energies (DeltaI=2) """


class Band_C:
    """
    - the band C - SIGNATURE PARTNER of band A (according to Timar et al 2019)
    - similar parity as the Band A
    - built on the neutron h=11/2 configuration 
    - opposite signature as of Band A: \alpha=+1/2
    """

    band_C_spins = '29/2,25/2,21/2'
    band_C_energies = [4955, 3859, 2900]
    band_C_transitions = [1097, 959]


def main():
    a_band_spins = Tools.ExtractSpins(Band_A.band_A_spins)
    b_band_spins = Tools.ExtractSpins(Band_B.band_B_spins)
    c_band_spins = Tools.ExtractSpins(Band_C.band_C_spins)

    print(a_band_spins)
    print(b_band_spins)
    print(c_band_spins)


if __name__ == '__main__':
    main()
