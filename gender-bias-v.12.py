""" This program analyses text file containing author names, counting
     how many male, female, and neutral given names are in the file.
     Each line in file should contain only author's name, last name first,
      and words separated by spaces."""

"""
v.01 2017/09/01 3:34pm JJ  reads one line at a time.
v.02 2017/09/01 3:39pm JJ  break line into words. Pull out 2nd word (given name)
v.03 2017/09/01 3:42pm JJ  create list of given names (nameList)
v.04 2017/09/01 3:53pm JJ  compare list to female and male names
v.05 2017/09/01 3:56pm JJ  pull out "both" male/female names
v.06 2017/09/01 3:59pm JJ  pull out "neither" male/female names
v.07 2017/09/01 4:02pm JJ  increment counts for male/female/both/neither
v.08 2017/09/01 4:11pm JJ  add names to list (male/female/both/neither)
v.09 2017/09/01        JJ  use len instead of incrementing counters. WORKS.  

v.10 2017/10/20 2:26pm JJ  Using medium-length file. WORKS.
V.11 2017/10/20 2:32pm JJ  Send lists to files. WORKS.
v.12 2017/10/20 2:46pm JJ  Use "A"s from the nameList. WORKS
v.13 2017/10/20 2:49pm JJ  Process whole list

"""
import nltk

import os
path = "C:/Users/jajames/Documents/gender-bias/"
os.chdir(path)
nameList = []


maleList = []
femaleList = []
bothList = []
neitherList = []

i = 0
with open('gender-bias-full-trimmed.txt') as f:
    i = 0 
    for line in f:
        if i > 500:
            break
        else:
            i += 1
            print(line)
            s=line.strip()
            w = s.split(" ")
            if len(w) > 1:
                nameList.append(w[1])


names = nltk.corpus.names
male_names = names.words('male.txt')
female_names = names.words('female.txt')

for w in nameList:
    if (w.title() in male_names) and (w.title() in female_names):
        #print("neutral name: ", w)
        bothList.append(w)
    elif w.title() in female_names:
        #print("female name: ", w)
        femaleList.append(w)
    elif w.title() in male_names:
        #print("male name: ", w)
        maleList.append(w)
    else:
        #print("not in name list: ", w)
        neitherList.append(w)

g = open('female-list.txt', 'w')
for line in femaleList:
    g.write(line)
    g.write('\n')
g.close()

g = open('male-list.txt', 'w')
for line in maleList:
    g.write(line)
    g.write('\n')
g.close()

g = open('both-list.txt', 'w')
for line in bothList:
    g.write(line)
    g.write('\n')
g.close()

g = open('neither-list.txt', 'w')
for line in neitherList:
    g.write(line)
    g.write('\n')
g.close()

"""
print("female list: ", femaleList)
print("male list: ", maleList)
print("both list: ", bothList)
print("neither list: ", neitherList)
"""

print("\nCOUNTS:\nfemale: ", len(femaleList),
      "\nmale: ", len(maleList),
      "\nboth: ", len(bothList),
      "\nneither: ", len(neitherList),
      "\ntotal: ", len(nameList))
