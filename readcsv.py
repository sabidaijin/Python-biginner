import os, glob

def process_a_file(file_name, d):
    f = open(file_name, 'r', encoding='utf-8')
    line1 = f.readline()
    f.readline()
    lines = f.readlines()
    f.close()
    word_seq = []
    for line in lines:
        for w in line.split():
            w = w.strip().strip('`";:[]{}()*&^%$#@!~/><,.=+' + "'").lower()
            if not w:
                continue
            if w.isdecimal():
                continue
            if not w in d:
                d[w] = 1
            else:
                d[w] += 1

def read_files():
    d = {}
    for fn in glob.glob('ebooks/*.txt'):
        process_a_file(fn, d)
    return d

d = read_files()
w_list = []
for w in d:
    w_list.append( [d[w], w] )
print(w_list)
w_list.sort()
w_list.reverse()

for n, w in w_list[:10]:
    print('{:8d} {:s}'.format(n, w))

