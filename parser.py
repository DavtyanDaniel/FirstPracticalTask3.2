"""

"""
# TODO write comments
from datetime import datetime

from stars_filtering import filtering_by_coordinates
import constants


def open_and_parse_file(file_name, range_of_square):
    """
        Function not only opening and parsing the file but also filtering them with the help
        of filtering_by_coordinates function.
    """
    try:
        with open(file_name, 'r') as tsv_file:
            list_of_objects = []
            for row in tsv_file:
                try:
                    splitted_row = row.split("\t")
                    data = filtering_by_coordinates(splitted_row,
                                                    range_of_square[constants.fov_ra_min_index],
                                                    range_of_square[constants.fov_ra_max_index],
                                                    range_of_square[constants.fov_dec_min_index],
                                                    range_of_square[constants.fov_dec_max_index])
                    if data is not None:
                        list_of_objects.append(data)
                except ValueError:
                    pass
    except FileNotFoundError:
        raise Exception(f'path isn\'t correct {file_name}')
    return list_of_objects


def write_the_file(filtered_stars: list):
    """

    :param filtered_stars:
    :return:
    """
    # TODO write comments
    with open(f"{datetime.now()}.csv", 'w') as f:
        header = "ID, RA, DEC, Magnitude, Dis_from_gv_point\n"
        f.write(header)
        for star in filtered_stars:
            row_data = f'{star.star_id}' + ',' + \
                       f'{star.ra},' + \
                       f'{star.dec},' + \
                       f'{star.mag},' + \
                       f'{star.euclidean_distance} \n'
            f.write(row_data)




