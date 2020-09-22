import glob
import re
from index import indexfile
from resulter import resulter

def check(q):
    if '"' in q:
        return 'phrase'
    elif len(q.split()) > 1:
        return 'freetext'
    elif len(q.split()) == 1:
        return 'oneword'

def oneword(q, indexfile):
    pattern = re.compile('[\W_]+')
    q = pattern.sub(' ', q)
    if q in indexfile.keys():
        f = [filename for filename in indexfile[q].keys()]
        return f
    else:
        return []
def freetext(input_string, indexfile):
    pattern = re.compile('[\W_]+')
    input_string = pattern.sub(' ', input_string)
    result = []
    for term in input_string.split():
         result = result + oneword(term, indexfile)
    return list(set(result))

def phrase(input_string, indexfile):

    pattern = re.compile('[\W_]+')
    input_string = pattern.sub(' ', input_string)
    list2 = []
    result = []
    for term in input_string.split():
         list2.append(oneword(term, indexfile))
    intersected = set(list2[0]).intersection(*list2)
    for filename in intersected:
         count = []
         for word in input_string.split():
             count.append(indexfile[word][filename][:])
         for i in range(len(count)):
             for j in range(len(count[i])):
                 count[i][j] = count[i][j] - i
         if set(count[0]).intersection(*count):
             result.append(filename)
    return result




def main():
    #indexfile = '/home/chandra/A1_pro/a.txt'
    q = input()                                   # q is the actual query here!
    x = check(q)                                  # 
    #print(str(x))
    if x is 'phrase':
        result = phrase(q, indexfile)
        q = re.sub('"','',q)
        for file in result:
            resulter(q,file)

    elif x is 'freetext':
        result1 = phrase(q,indexfile)
        if result1:
           for file in result1:
               resulter(q,file)
        
        result = freetext(q, indexfile)
        for word in q.split():
            for file in result:
                resulter(word,file)
    elif x is 'oneword':
        result = oneword(q, indexfile)
        for file in result:
            resulter(q,file)

if __name__ == '__main__':
    main()