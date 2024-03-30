import re

def extract_variable_names(string):
    variable_names = re.findall(r'\b_(\w+)\b', string)
    return variable_names

string = input()

all_variable_names = []
variable_names = extract_variable_names(string)
all_variable_names.extend(variable_names)

print(','.join(all_variable_names))
