import glob
import re

def build_list(filenames):
    file_terms = {}
    for file in filenames:
        pattern = re.compile('[\W_]+')
        file_terms[file] = open(file, 'r').read().lower();
        file_terms[file] = pattern.sub(' ', file_terms[file])
        re.sub(r'[\W_]+', '', file_terms[file])
        file_terms[file] = file_terms[file].split()
    return file_terms


def indexer_for_file(wordlist):
    fileIndex = {}
    for index,word in enumerate(wordlist):
        if word in fileIndex.keys():
            fileIndex[word].append(index)
        else:
            fileIndex[word] = [index]
    return fileIndex

def make_index(filelist):
    result = {}
    for filename in filelist.keys():
        result[filename] = indexer_for_file(filelist[filename])
    return result

#to construct the inverted index from index
def inverted(total):
    inverted_result = {}
    for filename in total.keys():
        for word1 in total[filename].keys():
            if word1 in inverted_result.keys():
                     if filename in inverted_result[word1].keys():
                         inverted_result[word1][filename].extend(total[filename][word1][:])
                     else:
                         inverted_result[word1][filename] = total[filename][word1]
            else:
                     inverted_result[word1] = {filename: total[filename][word1]}
    return inverted_result


#path = '/home/chandra/A1_pro/file_folder/*.*'
filenames = glob.glob('/home/chandra/PycharmProjects/search_engine_pro/file_folder/*.*')
file_list = build_list(filenames)

total = make_index(file_list)
indexfile = inverted(total)
#print(str(indexfile))
f = open('a2.txt','w')
f.write(str(indexfile))
f.close()
