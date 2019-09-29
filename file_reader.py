"""
Author: Ashley Beckers
File: file_reader.py
Description: Reads and parses files related to merge dragons into data usable by program
"""

def time_file_parser(filename):
    """
    Takes the name of a file with dragon harvest time information by species and puts it into a dictionary
    :pre: file must be organized such that:
            each line has one species' information
            flower level and nod number are separated by :
            entries are separated by a space
            species name is separated from entries by a space
    :param filename: name of the file
    :return: a dictionary of the data | {species(string): {flower level(int): number of nods(float)}}
    """
    dragon_harvest_times = {}
    with open(filename) as file:
        duplicates = False # whether or not duplicates have been found yet, used to avoid multiple error statements
        for line in file:
            line = line.strip().split(' ')
            species = line[0]
            line = line[1:]
            entries = {}
            for entry in line:
                entry = entry.split(':')
                entries[int(entry[0])] = float(entry[1])
            if species in dragon_harvest_times and not duplicates:
                print('One or more lines marked duplicate and ignored')
                duplicates = True
            elif species not in dragon_harvest_times:
                dragon_harvest_times[species] = entries
    return dragon_harvest_times
