#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up. In the first exercise we want you to audit
the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- NoneType if the value is a string "NULL" or an empty string ""
- list, if the value starts with "{"
- int, if the value can be cast to int
- float, if the value can be cast to float, but CANNOT be cast to int.
   For example, '3.23e+07' should be considered a float because it can be cast
   as float but int('3.23e+07') will throw a ValueError
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a 
SET of the types that can be found in the field. e.g.
{"field1": set([type(float()), type(int()), type(str())]),
 "field2": set([type(str())]),
  ....
}
The type() function returns a type object describing the argument given to the 
function. You can also use examples of objects to create type objects, e.g.
type(1.1) for a float: see the test function below for examples.

Note that the first three rows (after the header row) in the cities.csv file
are not actual data points. The contents of these rows should note be included
when processing data types. Be sure to include functionality in your code to
skip over or detect these rows.
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label",
          "isPartOf_label", "areaCode", "populationTotal", "elevation",
          "maximumElevation", "minimumElevation", "populationDensity",
          "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]

def isInteger(num):
  try:
    num = int(num)
  except ValueError:
    return False
  return True

def isFloat(num):
  if isInteger(num):
    return False
  try:
    num = float(num)
  except ValueError:
    return False
  return True

def audit_file(filename, fields):
    fieldtypes = {}

    # YOUR CODE HERE
    with open(filename) as csvfile:
      reader = csv.DictReader(csvfile)
      # skip the first 3 lines
      for _ in range(3):
        reader.__next__()
      for row in reader:
        for field in fields:
          if not field in fieldtypes:
            fieldtypes[field] = set()

          cell = row[field]
          if cell == None or cell == "NULL" or cell == "" or cell == "null" :
            # print("cell {0} type {1}".format(cell, type(None)))
            fieldtypes[field].add(type(None))
          elif cell.startswith("{"):
            # print("cell {0} type {1}".format(cell, type([])))
            fieldtypes[field].add(type([]))
          elif isInteger(cell):
            # print("cell {0} type {1}".format(cell, type(1)))
            fieldtypes[field].add(type(1))
          elif isFloat(cell):
            # print("cell {0} type {1}".format(cell, type(1.0)))
            fieldtypes[field].add(type(1.0))
          else:
            if field == "areaLand":
              print("hello!! cell {0} type {1}".format(cell, type("")))
            fieldtypes[field].add(type(""))

    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    print(fieldtypes["areaLand"])
    print(set([type(1.1), type([]), type(None)]))

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()
