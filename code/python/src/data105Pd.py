"""
- The experimental data for $^{105}$Pd nucleus
- Data extracted from https://www.nndc.bnl.gov/ensdf/
- Data are provided through the work: 96Zr(13C,4nγ):XUNDL-3 [2019Ti02] (unevaluated)
"""


class Tools:
    """
    - tools for extracting and parsing the experimental data
    """
    @staticmethod
    def ExtractSpins(raw_string):
        # separate all the spins by the commmas
        extracted_spins = raw_string.split(',')
        # only get the integer part after splitting is done
        # with the integer part determined, compute the numerical values of each spins
        spins = [float(x[:-2]) / 2 for x in extracted_spins]

        # perform sorting of the spins in ascending order
        spins.sort()

        return spins

    @staticmethod
    def keV_to_MeV(energies):
        """
        - transform the energies from units of keV to units of MeV
        - 1 MeV is 1000 keV
        """

        energies_mev = [float(x / 1000) for x in energies]

        # also sort the energies within ascending order
        energies_mev.sort()

        return energies_mev

    @staticmethod
    def normalize_energies(energies, band_head):
        """
        - subtract the value of the band-head (first energy within the YRAST band) from all the energies 
        """

        normalized_energies = [float(x - band_head) for x in energies]

        # sort the energies in ascending order
        normalized_energies.sort()

        return normalized_energies


class Band_B:
    """
    - the collection of energies belonging to the rotational structure B
    - it represents the band built on the neutron h=11/2
    - signature: \alpha=+1/2
    - negative parity spin states: \pi=-1
    """

    SIGNATURE = +0.5
    PARITY = -1

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

    SIGNATURE = -0.5
    PARITY = -1

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

    SIGNATURE = +0.5
    PARITY = -1

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

    a_band_energies = Tools.keV_to_MeV(Band_A.band_A_energies)

    print(Band_A.band_A_energies)
    print(a_band_energies)


if __name__ == '__main__':
    main()
