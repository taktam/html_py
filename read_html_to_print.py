#The script read the html file to python list (DataFrame)


import pandas

file_name = "feeders.html"

data = pandas.read_html(file_name)

fdr = None
fdr_nr = 0

for i in range(len(data[0])):
     if (len(str(data[0].iloc[i]["Feeder Name.2"])) >3)&(str(data[0].iloc[i]["Feeder Name.2"])!="Stationary")&(str(data[0].iloc[i]["Feeder Name.2"])!="Automatic")&(str(data[0].iloc[i]["Feeder Name.2"])!="Feeders"):
        print (data[0].iloc[i]["Feeder Name.2"])
