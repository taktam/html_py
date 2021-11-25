#The script read the html file to python dictionary


import pandas
#import numpy

file_name = "feeders.html"
#file = open(file_name, 'r')

data = pandas.read_html(file_name, parse_dates='Package Name')
print (len(data[0]))
