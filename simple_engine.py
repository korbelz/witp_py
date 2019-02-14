# Comment section
# spoil written by Korbelz
# current scope: simple engine numbers

print ('*** This app is a simple engine calculator ***')
print ('*** Written by Korbelz ***')
print ('*** Feedback/Bugs: Discord: Korbelz#3504 ***')
input('Press ENTER to continue')

import csv 
import datetime

airfile = open('AirframeProd.csv')
airreader = csv.reader(airfile)
#airreader = csv.DictReader(airfile)
airdata = list(airreader)
#aircount = Counter(airreader)
#airdict = dict(airreader)

#airdict = {}
#for row in airreader: 
#    if row["Engine Use"] == '0':
#        continue
#    airdict.update({row['Engine']: row['Engine Use']})

#for row in airdict:
#    print (airdict)
# Aircraft[1], enigne name[4], Engine use[5]
# print (airdata[2][1], airdata[2][4], airdata[2][5])
ha31total = 0
ha31eng = 0
ha32total = 0
ha32eng = 0
ha33total = 0
ha33eng = 0
ha34total = 0
ha34eng = 0
ha35total = 0
ha35eng = 0
for airdata in airdata:
    if airdata[5] == '0':
        continue    
    elif airdata[4] == 'Nakajima Ha-35 ':
        ha35total = ha35total + int(airdata[5])
        #print (ha35total)

    elif airdata[4] == 'Mitsubishi Ha-33':
        ha33total = ha33total + int(airdata[5])
        #print (ha35total)
    elif airdata[4] == 'Mitsubishi Ha-32':
        ha32total = ha32total + int(airdata[5])
        #print (ha32total)
    elif airdata[4] == 'Mitsubishi Ha-31 ':
        ha31total = ha31total + int(airdata[5])
        #print (ha31total)
    elif airdata[4] == 'Nakajima Ha-34 ':
        ha34total = ha34total + int(airdata[5])
        #print (ha34total)

    #elif airdata[4] == 'Nakajima Ha-35 ':
    #    ha35total = ha35total + int(airdata[5])
    #elif airdata[4] == 'Nakajima Ha-35 ':
    #    ha35total = ha35total + int(airdata[5])
    #print (airdata[1], airdata[4], airdata[5])


engfile = open('engines.csv')
engreader = csv.reader(engfile)
engdata = list(engreader)

#engine [1], building right now[3], repairing [4]
#print (engdata[0][1], engdata[0][3], engdata[0][4])
#print (engdata[7][1], engdata[7][3], engdata[7][4])

for engdata in engdata:
    if engdata[3] == '0.0 (0)':
        continue 

    elif engdata[1] == 'Nakajima Ha-35 ':
        ha35eng = ha35eng + int(engdata[7])
        #print (ha35total)

    elif engdata[1] == 'Mitsubishi Ha-33':
        ha33eng = ha33eng + int(engdata[7])

    elif engdata[1] == 'Mitsubishi Ha-32':
        ha32eng = ha32eng + int(engdata[7])

    elif engdata[1] == 'Mitsubishi Ha-31 ':
        ha31eng = ha31eng + int(engdata[7])

    elif engdata[1] == 'Nakajima Ha-34 ':
        ha34eng = ha34eng + int(engdata[7])
    
    #print (engdata[1], engdata[7])
    #print (aircount[engdata[1]])
#print (ha35eng)
print ('Engine name.......Number required.....Extra Engines Required')
print (f'Nakajima Ha-35          {ha35total}                {ha35total - ha35eng}')
print (f'Nakajima Ha-34          {ha34total}                  {ha34total - ha34eng}')
print (f'Mitsubishi Ha-31        {ha31total}                  {ha31total - ha31eng}')
print (f'Mitsubishi Ha-32        {ha32total}                  {ha32total - ha32eng}')
print (f'Mitsubishi Ha-33        {ha33total}                  {ha33total - ha33eng}')

input('Press ENTER to exit')