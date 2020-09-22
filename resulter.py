import re
#import argparse
import os
import glob

for i in range(1,10):
    for y in x:
        




def resulter(word,textfile):
     x = str(textfile)
     f = open(textfile,'r')
     lineNum = 0
     searchResultNumber = 0
     for lines in f.readlines():
        lines = lines.strip('\n\r')
        lineNum+=1
        result = re.search(word,lines, re.M|re.I)
        if result:
            searchResultNumber +=1
            if searchResultNumber != 0:
                  print(" "+str(lineNum)+":"+lines.replace(word, '\033[44;33m{}\033[m'.format(word)))
     print(str(searchResultNumber) + " RESULT FOUND   IN " +str(x))
def main():
    word = input()
    word = str(word)
    #path = '/home/chandra/A1_pro/file_folder/*.*'
    for file in glob.glob('/home/chandra/A1_pro/file_folder/*.*'):
        #f = open(file,"r")
        resulter(word,file)

if __name__ == '__main__':
    main()