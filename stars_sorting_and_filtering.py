"""
Every function that related to filtering and sorting are here.
"""
from random import randint

from stars import Stars
import constants


def computing_range_of_square(ra, dec, fov_h, fov_v) -> tuple:
    """
    Calculating the range of given FOV
    """
    # square's weight left number
    square_w_l = ra - fov_h / 2
    # square's weight right number
    square_w_r = ra + fov_h / 2
    # square's height left number
    square_h_l = dec - fov_v / 2
    # square's height right number
    square_h_r = dec + fov_v / 2
    return square_w_l, square_w_r, square_h_l, square_h_r


def filtering_by_coordinates(row: list,
                             square_w_l: float,
                             square_w_r: float,
                             square_h_l: float,
                             square_h_r: float) -> Stars:
    """
    filtering by ra/dec coordinates, for that we have to know the range of FOV, that's
    why in parameters list we have range of it.
    """
    if (square_w_l <= float(row[0]) <= square_w_r) and (square_h_l <= float(row[1]) <= square_h_r):
        return Stars(float(row[constants.RA_INDEX]),
                     float(row[constants.DEC_INDEX]),
                     int(row[constants.ID_INDEX]),
                     float(row[constants.MAG_INDEX]))


def quicksort(array: list, key, reverse: bool) -> list:
    """
    quicksort sorting algorithm that takes an array, key function, and sort direction and returns a sorted array
    """
    if len(array) < 2:
        return array
    left = []
    same = []
    right = []
    delimiter = key(array[randint(0, len(array) - 1)])
    for item in array:
        value = key(item)
        if value > delimiter:
            if reverse is False:
                left.append(item)
            else:
                right.append(item)
        elif value == delimiter:
            same.append(item)
        elif value < delimiter:
            if reverse is False:
                right.append(item)
            else:
                left.append(item)
    sorted_array = quicksort(left, key, reverse) + same + quicksort(right, key, reverse)
    return sorted_array


def get_mag(item):
    return item.mag


def get_dis(item):
    return item.euclidean_distance


def mag_slicing(array: list, n: int) -> list:
    return array[:n]
