import sys


filein=open(sys.argv[1], 'r')
fileout=open(sys.argv[2],'w')


for i, line in enumerate(filein):

        sep=line.split()
        space= ' '
        fileout.write(str(i+1) + space + sep[1] + space + sep[2] + space + sep[3] + space + sep[4] + space + sep[5] + '\n')
