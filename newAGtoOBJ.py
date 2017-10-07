#!/usr/bin/python


#Setup vars
xpos=0
count=0
tracker=0 #tracker tracks the number of points. OBJ files reference the point number, tracker is my way of tracking that.
cweight = 0
rweight = 0

pathtodata="uni_dsm.asc"
outfile = "uni_dsm.obj"

faces = ""

#weighting is for every other point and every other row.
#We want all the points, but not all the faces/polygons
rweight = 0 #Switch, we need every other row
cwidth = 0 #Swtich we need every other column



####Files

datafile = open(pathtodata)
outfile = open(outfile, 'w')

#Write outfile obj header

outfile.write("#OBJ file created by Ascii grid to obj convertor\n")
outfile.write("\n")
outfile.write("g map\n\n\n") # Object name

##end of object file header.

for blarg in datafile:
	count +=1 # Just a line counter first 6 lines are ascii file descriptor. Should use it, I'm ignoring it.
	
	if count > 6:
		temp =[]
		temp = blarg.split()
		for num in range (0, len(temp)):
			tracker += 1
			pointheight = float(temp[num])
			if pointheight < 0:
				pointheight = 30
			vector = "v " + ' ' + str(num) + ' ' + str(pointheight) + ' ' + str(xpos) #data point location, not polygon.
			outfile.write(vector + '\n')
			print(tracker)
			if num > 2 and num < 999 and tracker < 999000:
				faces += '\n' + "f " + ' ' + str(tracker) + ' ' + str(tracker + 1) + ' ' + str(tracker + 1001) + ' ' + str(tracker + 1000) 
				
			if cweight == 0:
				cweight = 1
			else:
				cweight = 0
			
			
		xpos += 1 # move cursor one dot.

		if rweight == 1:
			rweight = 0
		else:
			rweight = 1


		#xpos = 0

outfile.write(faces)
datafile.close()
outfile.close()
