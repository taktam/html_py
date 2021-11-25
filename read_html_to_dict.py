#The script read the html file to python dictionary


import pandas

file_name = "feeders.html"
#file = open(file_name, 'r')

tables = pandas.read_html(file_name)
print (tables[0])