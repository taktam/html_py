from os import close
import pandas
import csv
import fnmatch

open_file_name = "feeders.html"
save_file_name = "feeders.csv"

data = pandas.read_html(open_file_name)
file_to_save = open (save_file_name, 'w')
writer = csv.writer(file_to_save)
list_to_write = []
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
                        list_to_write.clear
                        list_to_write.append [str(fdr_name)]
                        list_to_write.append [str(data[0].iloc[i,3])]
                        list_to_write.append [str(data[0].iloc[i,5])]
                        print (fdr_name,',', str(data[0].iloc[i,3])+'\t'+','+str(data[0].iloc[i,5]))
                        writer.writerows(list_to_write)
file_to_save.close

