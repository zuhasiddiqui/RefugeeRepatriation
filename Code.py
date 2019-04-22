import urllib.request
import http.cookiejar
from collections import Counter

cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

webURL = "https://data.humdata.org/dataset/8aefb53d-5c18-4719-8730-19188ae8c1e7/resource/046057a3-b126-4be9-9f8d-8b07e616a56b/download/afghan-voluntary-repatriation-2018.csv"
outfilename = "Afghan2018.csv"

try:
    infile = opener.open(webURL, timeout=15)
    outfile = open(outfilename, "w")
    newpage = infile.read().decode('utf-8')

except:
    print("We have an error")
    newpage = ""

if newpage != "":
    for line in newpage:
        datalist = line.strip().split(",")
        stringlist = str(datalist)
        outfile.write(line)
        infile.close()

infile2 = open("Afghan2018.csv", "r+")
infile3 = open("Afghan2017.csv", "r+")
infile4 = open("Afghan2016.csv", "r+")
infile5 = open("Afghan2015.csv", "r+")
infile6 = open("Afghan2014.csv", "r+")

outfile2 = open("displaced2018.csv", "w")
outfile3 = open("displaced2017.csv", "w")
outfile4 = open("displaced2016.csv", "w")
outfile5 = open("displaced2015.csv", "w")
outfile6 = open("displaced2014.csv", "w")

firstline = infile2.readline().strip()
headerlist = firstline.split(",")
outfile2.write(firstline)
# outfile3.write(firstline)
# outfile4.write(firstline)
# outfile5.write(firstline)
# outfile6.write(firstline)

asylumcountry = headerlist.index("COUNTRY_OF_ASYLUM")
dateposition = headerlist.index("RETURN_DATE")
origprovposition = headerlist.index("ORIG_PROV_NAME")
origdistposition = headerlist.index("ORIG_DIST_NAME")
destprovposition = headerlist.index("DESTINATION_PROV_NAME")
destdistposition = headerlist.index("DESTINATION_DIST_NAME")
maleposition = headerlist.index("MALE")
femaleposition = headerlist.index("FEMALE")
individualposition = headerlist.index("INDIVIDUALS")

# If ORIG_DIST_NAME != DESTINATION_DIST_NAME
# then print all data to new files called displaced.csv

for line in infile2:
    datalist2 = line.strip().split(",")
    origdist = datalist2[origdistposition]
    destdist = datalist2[destdistposition]
    if origdist != destdist:
        outfile2.write(line)

for line in infile3:
    datalist3 = line.strip().split(",")
    origdist = datalist3[origdistposition]
    destdist = datalist3[destdistposition]
    if origdist != destdist:
        outfile3.write(line)

for line in infile4:
    datalist4 = line.strip().split(",")
    origdist = datalist4[origdistposition]
    destdist = datalist4[destdistposition]
    if origdist != destdist:
        outfile4.write(line)

for line in infile5:
    datalist5 = line.strip().split(",")
    origdist = datalist5[origdistposition]
    destdist = datalist5[destdistposition]
    if origdist != destdist:
        outfile5.write(line)

for line in infile6:
    datalist6 = line.strip().split(",")
    origdist = datalist6[origdistposition]
    destdist = datalist6[destdistposition]
    if origdist != destdist:
        outfile6.write(line)

print("Repatriation data of displaced refugees has been sorted.")
print()
outfile2.close()
infile2.close()
outfile3.close()
infile3.close()
outfile4.close()
infile4.close()
outfile5.close()
infile5.close()
outfile6.close()
infile6.close()

# analyse repatriation data for 2018##

newfile = open("displaced2018.csv", "r+")

# how many repatriated to Kabul, Mazar-e-Sharif, Herat, Jalalabad in 2018

kcount18 = 0
mcount18 = 0
hcount18 = 0
jcount18 = 0

koriglist18 = []
horiglist18 = []
joriglist18 = []
moriglist18 = []


for line in newfile:
    newlist = line.strip().split(",")
    destdist = newlist[destdistposition]
    k2018found = destdist.find("Kabul")
    if (k2018found != -1):
        indiv = int(newlist[individualposition])
        kcount18 = kcount18 + indiv
        origdist = newlist[origdistposition]
        koriglist18.append(origdist)
    h2018found = destdist.find("Herat")
    if (h2018found != -1):
        indiv = int(newlist[individualposition])
        hcount18 = hcount18 + indiv
        origdist = newlist[origdistposition]
        horiglist18.append(origdist)
    j2018found = destdist.find("Jalalabad")
    if (j2018found != -1):
        indiv = int(newlist[individualposition])
        jcount18 = jcount18 + indiv
        origdist = newlist[origdistposition]
        joriglist18.append(origdist)
    m2018found = destdist.find("Mazar-e-Sharif")
    if (m2018found != -1):
        indiv = int(newlist[individualposition])
        mcount18 = mcount18 + indiv
        origdist = newlist[origdistposition]
        moriglist18.append(origdist)

print(kcount18, "refugees were repatriated to Kabul in 2018.")
print(hcount18, "refugees were repatriated to Herat in 2018.")
print(jcount18, "refugees were repatriated to Jalalabad in 2018.")
print(mcount18, "refugees were repatriated to Mazar-e-Sharif in 2018.")
print()

# where did repatriated refugees come from

kcounter18 = Counter(koriglist18).most_common(10)
print("Refugees repatriated to Kabul in 2018 came from these districts: ")
print(kcounter18)
print()

hcounter18 = Counter(horiglist18).most_common(10)
print("Refugees repatriated to Herat in 2018 came from these districts: ")
print(hcounter18)
print()

jcounter18 = Counter(joriglist18).most_common(10)
print("Refugees repatriated to Jalalabad in 2018 came from these districts: ")
print(jcounter18)
print()

mcounter18 = Counter(moriglist18).most_common(10)
print("Refugees repatriated to Mazar-e-Sharif in 2018 came from these districts: ")
print(mcounter18)
print()

newfile.close()

# analyse repatriation data for 2017##

newfile2 = open("displaced2017.csv", "r+")

# how many repatriated to Kabul, Mazar-e-Sharif, Herat, Jalalabad in 2017

kcount17 = 0
mcount17 = 0
hcount17 = 0
jcount17 = 0

koriglist17 = []
horiglist17 = []
joriglist17 = []
moriglist17 = []


for line in newfile2:
    newlist = line.strip().split(",")
    destdist = newlist[destdistposition]
    k2017found = destdist.find("Kabul")
    if (k2017found != -1):
        indiv = int(newlist[individualposition])
        kcount17 = kcount17 + indiv
        origdist = newlist[origdistposition]
        koriglist17.append(origdist)
    h2017found = destdist.find("Herat")
    if (h2017found != -1):
        indiv = int(newlist[individualposition])
        hcount17 = hcount17 + indiv
        origdist = newlist[origdistposition]
        horiglist17.append(origdist)
    j2017found = destdist.find("Jalalabad")
    if (j2017found != -1):
        indiv = int(newlist[individualposition])
        jcount17 = jcount17 + indiv
        origdist = newlist[origdistposition]
        joriglist17.append(origdist)
    m2017found = destdist.find("Mazar-e-Sharif")
    if (m2017found != -1):
        indiv = int(newlist[individualposition])
        mcount17 = mcount17 + indiv
        origdist = newlist[origdistposition]
        moriglist17.append(origdist)

print(kcount17, "refugees were repatriated to Kabul in 2017.")
print(hcount17, "refugees were repatriated to Herat in 2017.")
print(jcount17, "refugees were repatriated to Jalalabad in 2017.")
print(mcount17, "refugees were repatriated to Mazar-e-Sharif in 2017.")
print()

# where did repatriated refugees come from


kcounter17 = Counter(koriglist17).most_common(10)
print("Refugees repatriated to Kabul in 2017 came from these districts: ")
print(kcounter17)
print()

hcounter17 = Counter(horiglist17).most_common(10)
print("Refugees repatriated to Herat in 2017 came from these districts: ")
print(hcounter17)
print()

jcounter17 = Counter(joriglist17).most_common(10)
print("Refugees repatriated to Jalalabad in 2017 came from these districts: ")
print(jcounter17)
print()

mcounter17 = Counter(moriglist17).most_common(10)
print("Refugees repatriated to Mazar-e-Sharif in 2017 came from these districts: ")
print(mcounter17)
print()

newfile2.close()

# analyse repatriation data for 2016##

newfile3 = open("displaced2016.csv", "r+")

# how many repatriated to Kabul, Mazar-e-Sharif, Herat, Jalalabad in 2016

kcount16 = 0
mcount16 = 0
hcount16 = 0
jcount16 = 0

koriglist16 = []
horiglist16 = []
joriglist16 = []
moriglist16 = []


for line in newfile3:
    newlist = line.strip().split(",")
    destdist = newlist[destdistposition]
    k2016found = destdist.find("Kabul")
    if (k2016found != -1):
        indiv = int(newlist[individualposition])
        kcount16 = kcount16 + indiv
        origdist = newlist[origdistposition]
        koriglist16.append(origdist)
    h2016found = destdist.find("Herat")
    if (h2016found != -1):
        indiv = int(newlist[individualposition])
        hcount16 = hcount16 + indiv
        origdist = newlist[origdistposition]
        horiglist16.append(origdist)
    j2016found = destdist.find("Jalalabad")
    if (j2016found != -1):
        indiv = int(newlist[individualposition])
        jcount16 = jcount16 + indiv
        origdist = newlist[origdistposition]
        joriglist16.append(origdist)
    m2016found = destdist.find("Mazar-e-Sharif")
    if (m2016found != -1):
        indiv = int(newlist[individualposition])
        mcount16 = mcount16 + indiv
        origdist = newlist[origdistposition]
        moriglist16.append(origdist)

print(kcount16, "refugees were repatriated to Kabul in 2016.")
print(hcount16, "refugees were repatriated to Herat in 2016.")
print(jcount16, "refugees were repatriated to Jalalabad in 2016.")
print(mcount16, "refugees were repatriated to Mazar-e-Sharif in 2016.")
print()

# where did repatriated refugees come from

kcounter16 = Counter(koriglist16).most_common(10)
print("Refugees repatriated to Kabul in 2016 came from these districts: ")
print(kcounter16)
print()

hcounter16 = Counter(horiglist16).most_common(10)
print("Refugees repatriated to Herat in 2016 came from these districts: ")
print(hcounter16)
print()

jcounter16 = Counter(joriglist16).most_common(10)
print("Refugees repatriated to Jalalabad in 2016 came from these districts: ")
print(jcounter16)
print()

mcounter16 = Counter(moriglist16).most_common(10)
print("Refugees repatriated to Mazar-e-Sharif in 2016 came from these districts: ")
print(mcounter16)
print()

newfile3.close()

# analyse repatriation data for 2015##

newfile4 = open("displaced2015.csv", "r+")

# how many repatriated to Kabul, Mazar-e-Sharif, Herat, Jalalabad in 2015

kcount15 = 0
mcount15 = 0
hcount15 = 0
jcount15 = 0

koriglist15 = []
horiglist15 = []
joriglist15 = []
moriglist15 = []


for line in newfile4:
    newlist = line.strip().split(",")
    destdist = newlist[destdistposition]
    k2015found = destdist.find("Kabul")
    if (k2015found != -1):
        indiv = int(newlist[individualposition])
        kcount15 = kcount15 + indiv
        origdist = newlist[origdistposition]
        koriglist15.append(origdist)
    h2015found = destdist.find("Herat")
    if (h2015found != -1):
        indiv = int(newlist[individualposition])
        hcount15 = hcount15 + indiv
        origdist = newlist[origdistposition]
        horiglist15.append(origdist)
    j2015found = destdist.find("Jalalabad")
    if (j2015found != -1):
        indiv = int(newlist[individualposition])
        jcount15 = jcount15 + indiv
        origdist = newlist[origdistposition]
        joriglist15.append(origdist)
    m2015found = destdist.find("Mazar-e-Sharif")
    if (m2015found != -1):
        indiv = int(newlist[individualposition])
        mcount15 = mcount15 + indiv
        origdist = newlist[origdistposition]
        moriglist15.append(origdist)

print(kcount15, "refugees were repatriated to Kabul in 2015.")
print(hcount15, "refugees were repatriated to Herat in 2015.")
print(jcount15, "refugees were repatriated to Jalalabad in 2015.")
print(mcount15, "refugees were repatriated to Mazar-e-Sharif in 2015.")
print()

# where did repatriated refugees come from

kcounter15 = Counter(koriglist15).most_common(10)
print("Refugees repatriated to Kabul in 2015 came from these districts: ")
print(kcounter15)
print()

hcounter15 = Counter(horiglist15).most_common(10)
print("Refugees repatriated to Herat in 2015 came from these districts: ")
print(hcounter15)
print()

jcounter15 = Counter(joriglist15).most_common(10)
print("Refugees repatriated to Jalalabad in 2015 came from these districts: ")
print(jcounter15)
print()

mcounter15 = Counter(moriglist16).most_common(10)
print("Refugees repatriated to Mazar-e-Sharif in 2016 came from these districts: ")
print(mcounter15)
print()

newfile4.close()

# analyse repatriation data for 2014##

newfile5 = open("displaced2014.csv", "r+")

# how many repatriated to Kabul, Mazar-e-Sharif, Herat, Jalalabad in 2014

kcount14 = 0
mcount14 = 0
hcount14 = 0
jcount14 = 0

koriglist14 = []
horiglist14 = []
joriglist14 = []
moriglist14 = []


for line in newfile5:
    newlist = line.strip().split(",")
    destdist = newlist[destdistposition]
    k2014found = destdist.find("Kabul")
    if (k2014found != -1):
        indiv = int(newlist[individualposition])
        kcount14 = kcount14 + indiv
        origdist = newlist[origdistposition]
        koriglist14.append(origdist)
    h2014found = destdist.find("Herat")
    if (h2014found != -1):
        indiv = int(newlist[individualposition])
        hcount14 = hcount14 + indiv
        origdist = newlist[origdistposition]
        horiglist14.append(origdist)
    j2014found = destdist.find("Jalalabad")
    if (j2014found != -1):
        indiv = int(newlist[individualposition])
        jcount14 = jcount14 + indiv
        origdist = newlist[origdistposition]
        joriglist14.append(origdist)
    m2014found = destdist.find("Mazar-e-Sharif")
    if (m2014found != -1):
        indiv = int(newlist[individualposition])
        mcount14 = mcount14 + indiv
        origdist = newlist[origdistposition]
        moriglist14.append(origdist)

print(kcount14, "refugees were repatriated to Kabul in 2014.")
print(hcount14, "refugees were repatriated to Herat in 2014.")
print(jcount14, "refugees were repatriated to Jalalabad in 2014.")
print(mcount14, "refugees were repatriated to Mazar-e-Sharif in 2014.")
print()

# where did repatriated refugees come from

kcounter14 = Counter(koriglist14).most_common(10)
print("Refugees repatriated to Kabul in 2014 came from these districts: ")
print(kcounter14)
print()

hcounter14 = Counter(horiglist14).most_common(10)
print("Refugees repatriated to Herat in 2014 came from these districts: ")
print(hcounter14)
print()

jcounter14 = Counter(joriglist14).most_common(10)
print("Refugees repatriated to Jalalabad in 2014 came from these districts: ")
print(jcounter14)
print()

mcounter14 = Counter(moriglist14).most_common(10)
print("Refugees repatriated to Mazar-e-Sharif in 2016 came from these districts: ")
print(mcounter14)
print()

newfile5.close()
