# With Help from http://gis.stackexchange.com/questions/21637/arcgis-10-python-split-string

# Script written for Field Calculator, parsing the value from a string field into a new string field 

# Pre-logic Script Code:
def getFirst(inField):
  if inField is None:
    return None
  else:
    return inField.split('US')[1]

# Notes: split works by finding the value in single quotes ('abc'), splitting the entire entry at that value, and then returns the entity number in brackets[].
# Split value can also be space(s) (' '), commas (',').  Important to note that python counts the return entity value starting with 0.

# Codeblock:
getFirst( !GEO_id! )

# !GEO_id! is the field the script parses and should be replaced with the appropriate column name






# An alternative version is to split brackets and return the value inside with all lower case letters:
def parse(inField):
  if inField is None:
    return None
  else:
    return inField.split('{')[1].split('}')[0].lower()

# Codeblock
parse( !GlobalID! )