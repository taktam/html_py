import pandas
import csv
import fnmatch

file_name = "feeders.html"

data = pandas.read_html(file_name)

fdr_name = None
sap = 0

for i in range(len(data[0])):
    if (str(data[0].iloc[i,3]!="Lane'\*'")):
        if (len(str(data[0].iloc[i]["Feeder Name.2"])) >3)&(str(data[0].iloc[i]["Feeder Name.2"])!="Stationary")&(str(data[0].iloc[i]["Feeder Name.2"])!="Automatic")&(str(data[0].iloc[i]["Feeder Name.2"])!="Feeders"):
            fdr_name = str(data[0].iloc[i,3])
        if (fdr_name != None):
            if fnmatch.fnmatch(str(data[0].iloc[i,3]), 'Smart*')!=True:
                if fnmatch.fnmatch(str(data[0].iloc[i,3]), 'Stationary*')!=True:
                    if fnmatch.fnmatch(str(data[0].iloc[i,3]), 'Tape Strips*')!=True:
                        print (fdr_name,',', str(data[0].iloc[i,3])+'\t'+','+str(data[0].iloc[i,5]))