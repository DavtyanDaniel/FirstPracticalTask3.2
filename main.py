"""

"""
# TODO write comments
import parser
import stars_filtering
from constants import SORTING_DIRECTION_DIS, SORTING_DIRECTION_MAG, FILE_NAME, RA, DEC, FOV_H, FOV_V, N


def main(file_path_or_name: str,
         ra: float,
         dec: float,
         fov_h: float,
         fov_v: float,
         number_of_stars: int) -> None:
    """
    This is main function, that units all the work in different functions.
    """
    range_of_square = stars_filtering.computing_range_of_square(ra, dec, fov_h, fov_v)
    filtered_stars = parser.open_and_parse_file(file_path_or_name, range_of_square)
    sorted_stars_by_mag = stars_filtering.quicksort(filtered_stars,
                                                    stars_filtering.get_mag,
                                                    SORTING_DIRECTION_MAG)
    sliced_by_n_stars = stars_filtering.mag_slicing(sorted_stars_by_mag, number_of_stars)
    sorted_stars_by_dis = stars_filtering.quicksort(sliced_by_n_stars,
                                                    stars_filtering.get_dis,
                                                    SORTING_DIRECTION_DIS)
    parser.write_the_file(sorted_stars_by_dis)


if __name__ == "__main__":
    main(FILE_NAME, RA, DEC, FOV_H, FOV_V, N)

