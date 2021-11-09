import csv
import numpy as np
import matplotlib.pyplot as plt
import io
from PIL import Image

#import alcohol percentages from CSV
scrapedlist = open('scrapedcsv.csv','r')
reader = csv.reader(scrapedlist)
alcoholdict = {}
for row in reader:
    alcoholdict = {"Vdka":row[0],'Gin':row[1],'Rum': row[2],'Whiskey':row[3],'Tequila':row[4],'liqeurs':row[5],'Fortified Wine':row[6],'Unfortified Wine':row[7],'Beer':row[8],'Malt Beverage':row[9]}
    
#calculates alcohol content
def A(vodka=0, gin=0,rum=0, whiskey=0, tequila=0, liqeurs=0, fortwine=0, unfortwine=0, beer=0, maltbev=0):
    B=((vodka *1.25 *float(alcoholdict["Vdka"]))+(gin* 1.25* float(alcoholdict["Gin"]))+ (rum * 1.25 * float(alcoholdict["Rum"]))+ (whiskey * 1.25 * float(alcoholdict["Whiskey"]))+
    (whiskey * 1.25 * float(alcoholdict["Whiskey"]))+ (tequila * 1.25 * float(alcoholdict["Tequila"]))+(liqeurs * 1.25 * float(alcoholdict["liqeurs"]))+ 
    (unfortwine * 5 * float(alcoholdict["Unfortified Wine"]))+(fortwine * 5 * float(alcoholdict["Fortified Wine"])) + (beer * 12 * float(alcoholdict["Beer"])) + (maltbev * 12 * float(alcoholdict["Malt Beverage"])))
    return(B)
myA= float(A())

#calculates BAC%
def BACP(myalc= myA, gender='male', weight=150,starttime = 2):
    if gender == 'male':
        C=((((myalc*.01) * 5.14) / (float(weight) * .73)) - (.015*float(starttime)))
        return(C)
    elif gender == 'female':
        C=((((myalc*.01) * 5.14) / (float(weight) * .66)) - (.015*float(starttime)))
        return(C)

#calculates hours until BAC = 0
def TD(tbacp=0):
    D=(tbacp/.015)
    return(D)
myF= TD()

#sets up x values for graph
def linegraph1():
    x = np.arange(0,50,1)
    return(x)
myx= linegraph1()

#sets up function for graph
def linegraph2( xd = 0):
    myfunc = lambda myx: (-.015*myx)+xd
    y = np.array(list(map(myfunc, myx)))
    return(y)

#plots graph
def display(myy, bacp, F):
    plt.style.use('ggplot') 
    plt.rcParams["figure.figsize"] = (20,3)
    plt2 = plt.subplot2grid((11,1), (4,0), rowspan = 15, colspan = 1) 
    plt.title('Your current BAC is '+str(bacp)+'% and it will take '+str(F)+" hours to get your BAC% to zero.")
    x= linegraph1()
    y= linegraph2(bacp)
    plt2.plot(x, y, label = "x axis =Time & y axis = BAC" ,color = 'r') 
    plt2.legend() 
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return(buf)



