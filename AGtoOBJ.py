#!/usr/bin/python

xpos = 0
zpos = 0
count = 0
tracker = 0
#pathtodata="./ny30/ny3409_DTM_1M.asc"
pathtodata="SU31.asc"
outfile = "lake_map.obj"

####File stuff

datafile = open(pathtodata)
outfile = open(outfile, 'w')
########set obj file header

outfile.write("#OBJ file create by ASCii grid to obj convertor\n")
outfile.write("#\n")
outfile.write("g map\n\n\n")

########


while datafile.readline():
        count += 1 # count > 6
        if count > 6 and count <=1006: #1000x1000 Ascii Grid data.
                temp=[]
                blarg = datafile.readline()
                temp = blarg.split()
                for num in range (0, len(temp)):
                #for num in range (0, 100):
                        tracker+=1
                #        xpos = xpos + 1
                        pointheight = 80 - float(temp[num])
                        vector = "v " + ' ' +  str(num) + ' ' + str(pointheight) + ' ' + str(xpos)
                        outfile.write(vector + '\n')
                        if count <= 504 and num < 999 and num > 2:
                                fthing = "f " + str(tracker) + ' ' + str(tracker + 1) + ' ' + str(tracker - 1) + ' ' + str(tracker + 998) + ' ' + str(tracker + 999) + ' ' + str(tracker + 1000) + ' ' + str(tracker + 1001) 
                                outfile.write(fthing + '\n')
                #xpos = 0

        print (xpos)
        
        xpos += 1

datafile.close()
outfile.close()		
		
