# source: https://www.youtube.com/watch?v=rfscVS0vtbw&ab_channel=freeCodeCamp.org
import random
import re

feet_in_mile = 52800
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Start"]


def get_file_ext(filename):
    '''Python offers two different primitive operations based on regular expressions: re.match() checks for a match only at the beginning of the string, while re.search() checks for a match anywhere in the string (this is what Perl does by default).'''
    return re.search("\\.[a-zA-Z]+$", filename).start()


def roll_dice(num):
    return random.randint(1, num)
