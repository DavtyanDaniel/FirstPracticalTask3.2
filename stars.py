"""
Module for Stars class.
"""
import constants


class Stars:
    """
    Stars class that has an star_id, ra, dec, mag, euclidean_distance that are respectively
    stands for ID of star, right ascension, declination, magnitude and euclidean distance
    """
    def __init__(self, ra, dec, star_id, mag):
        self.star_id = star_id
        self.ra = ra
        self.dec = dec
        self.mag = mag
        self.euclidean_distance = ((ra - constants.RA) ** 2 + (dec - constants.DEC) ** 2) ** 0.5

    def __repr__(self):
        return f"{self.star_id}, {self.ra}, {self.dec}, {self.mag}, {self.euclidean_distance}\n"

