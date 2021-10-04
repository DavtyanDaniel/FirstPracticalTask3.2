"""

"""
# TODO write comments
import configparser

config = configparser.ConfigParser()
config.read('input.ini')
FILE_NAME = config['USER']['FileName']

try:
    RA = float(config['USER']['ra'])
    DEC = float(config['USER']['dec'])
    FOV_H = float(config['USER']['fov_h'])
    FOV_V = float(config['USER']['fov_v'])
    N = int(config['USER']['n'])
    SORTING_DIRECTION_MAG = bool(config['USER']['sorting_reverse_on_mag'])
    SORTING_DIRECTION_DIS = bool(config['USER']['sorting_reverse_on_dis'])

except ValueError as error:
    raise Exception('invalid variable' + str(error))

# column indexes in data file

RA_INDEX = 5
DEC_INDEX = 6
ID_INDEX = 7
MAG_INDEX = 22

# constants for range_of_square

fov_ra_min_index = 0
fov_ra_max_index = 1
fov_dec_min_index = 2
fov_dec_max_index = 3





