#!/usr/bin/python


#Setup vars
xpos=0
count=0
tracker=0 #tracker tracks the number of points. OBJ files reference the point number, tracker is my way of tracking that.
cweight = 0
rweight = 0

pathtodata="points.asc"
outfile = "points.obj"

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
	
	if count > 2:
		temp =[]
		temp = blarg.split()
		tracker += 1
		vector = "v " + ' ' + str(float(temp[0]) * 5) + ' ' + str(float(temp[2]) * 5) + ' ' + str(float(temp[1]) * 5) #data point location, not polygon.
		outfile.write(vector + '\n')
		print(tracker)
				
			



#outfile.write(faces)
datafile.close()
outfile.close()
