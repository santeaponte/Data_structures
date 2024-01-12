# files test: this code search for an specific word and then, make the average before 
# transform an string to a float
import numpy as np

fname = input('Enter the file name: ')
try:
    fh = open(fname, 'r')
except:
    print('file cannot be opened: ', fname)
    quit()
count_lines = 0
count_characteres = 0
contador = 0
sumador = 0
for i in fh:
    count_lines += 1
    count_characteres += len(i)
    if i.startswith('X-DSPAM-Confidence:'):
        i = i.strip()
        #print(i)
        var = i 
        for token in var.split():
            try:
                prom = float(token)
                #print(prom)
                contador += 1
                sumador += prom
            except:
                continue
print('Average spam confidence: ', sumador/contador)
print('que esta pasando')





 
