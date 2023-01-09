# SAVE TO JSON DEMO by MR. V

# *********************************************************************************
# Demo of how to save Data to a file as JSON
# JSON stands for JavaScript Object Notation
# It is a notation for representing data
# JSON may be used to convert data to a string and vice versa
# In Python, JSON supports all basic data, lists and dictionaries (not objects)
# *********************************************************************************

# Import JSON module
import json

# Create some data (List of Point Dictionaries)
points = [
    {"x": 11, "y": 1},
    {"x": 21, "y": 2},
    {"x": 31, "y": 3}]

# Open a file and use json.dump to write data to file as JSON
with open("point-data.json", "w") as file_ref:
    json.dump(points, file_ref)
