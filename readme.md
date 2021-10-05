#Introduction
The project is a task for FreeDOM Astronomy's internship program.It's aim to test python knowledge and skills.

The script takes ra, dec, id, mag of a star from .tsv file and using them for creating a list of N the brightest stars sorted by distance from a given RA, DEC coordinates.



# Table of Content
* [System Requirements](#system-requirements)
* [Installation](#installation)
* [How To Run](#how-to-run)
# System Requirements:
 - python3 
 - pip3
​
# Installation
  - Clone latest version from  https://github.com/DavtyanDaniel/FirstPracticalTask3.2.git  
  - It is highly recommended to create isolated environment
  
# How to run
 ```sh
$ python3 main.py
 ```

### Run parameters
The script is accepting parameters that you can write in input.ini file.

List of parameters

NumberOfStars - Is the number of the brightest stars in the given FOV.

RA, DEC - are the coordinates that you give for know the center of FOV.

Fov_h, Fov_v - are the horizontal and vertical FOVs.

FileName - is the name of .tsv file in current directory.
