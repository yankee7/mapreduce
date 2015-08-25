#!/usr/bin/python


import sys


#def mapper():
#    """ this method checks if there is buildings higher then 10m or 3 stores """
#according to few articles there' s no need to make a function, anyway I can do so

building = []  # initalize the building variable
for line in sys.stdin:

    # do only for  <way /> tag, it often starts building attributes
    if "<way" in line:
        # gets the  id of <way /> tag
        building = [strng[4:-1] for strng in line.split(' ') if strng.startswith('id')]
    elif "<tag" in line:
        # removes parts of tag leaves only attributes
        line = line.replace("<tag", "").replace("/>", "").replace('\n', '')
        # removes attributes keys of tag
        line = line.replace('k=', '').replace('v=', '')
        # converting to dict from tag attributes
        tag = dict([' '.join(line.split()).replace('"', '').split(" ", 1)])
        # searches if there is needed attribute in tag dict and checks its value
    if 'building:levels' in tag:
        if tag['building:levels'] >= 3:
            return building
    # searches if there is needed attribute in tag dict and checks its value
    elif 'height' in tag:
        if tag['height'] > 10:
            return building
