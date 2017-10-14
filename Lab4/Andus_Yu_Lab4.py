import csv

points_file = "points.csv"

pointsIncX = []
pointsIncY = []

# Loads the points into a list
def loadPoints(pts):
	# Load the images into image_List
	with open(points_file) as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			pts.append(row)

# Quicksort algorithm that sorts by the points using their x values
def quickSort(alist, xory):
	quickSortHelper(alist, 0, len(alist)-1, xory)

# Quicksort helper 
def quickSortHelper(alist, first, last, xory):
	if (first < last):

		splitpoint = partition(alist, first, last, xory)
		quickSortHelper(alist, first, splitpoint-1, xory)
		quickSortHelper(alist, splitpoint+1, last, xory)

# Partition for quicksort
def partition(alist, first, last, xory):
	pivotvalue = float(alist[first][xory])

	leftmark = first + 1
	rightmark = last
	done = False

	while (not done):
		while (leftmark <= rightmark and float(alist[leftmark][xory]) <= pivotvalue):
			leftmark = leftmark + 1

		while (float(alist[rightmark][xory]) >= pivotvalue and rightmark >= leftmark):
			rightmark = rightmark - 1

		if (rightmark < leftmark):
			done = True
		else:
			temp = float(alist[leftmark][xory])
			alist[leftmark][xory] = float(alist[rightmark][xory])
			alist[rightmark][xory] = temp

	temp = float(alist[first][xory])
	alist[first][xory] = float(alist[rightmark][xory])
	alist[rightmark][xory] = temp

	return rightmark

class BoundingBox:
	def __init__(self, x1, y1, x2, y2, ptsList):
		self.x1 = float(x1)
		self.y1 = float(y1)
		self.x2 = float(x2)
		self.y2 = float(y2)
		self.pts = ptsList
		self.calcPoints()
		self.calcArea()
		self.calcPointDensity()

	# Returns the area of the bounding box
	def calcArea(self):
		length = abs(float(self.x2) - float(self.x1))
		height = abs(float(self.y2) - float(self.y1))
		area = float(height) * float(length)
		self.area = float(height) * float(length)

	# Calculates the total number of points
	def calcPoints(self):
		count = 0
		for i in range (0, len(self.pts)):
			if (float(self.pts[i][0]) >= self.x1 and float(self.pts[i][0]) <= self.x2 and float(self.pts[i][1]) >= self.y1 and float(self.pts[i][1]) <= self.y2):
				count = count + 1
		self.numPoints = count

	#Calculates total point density
	def calcPointDensity(self):
		self.density = self.numPoints / self.area

	def fullestSubRectangle(self):
		count = 0

		parent = BoundingBox(self.x1, self.y1, self.x2, self.y2, self.pts)
		bb = BoundingBox(self.x1, self.y1, self.x2, self.y2, self.pts)

		while bb.density >= parent.density and bb.area >= 1:
			parent = bb
			if (count % 2 == 0):
				x_center = (parent.x2 + parent.x1) / 2
				bb1 = BoundingBox(parent.x1, parent.y1, x_center, parent.y2, self.pts)
				bb2 = BoundingBox(x_center, parent.y1, parent.x2, parent.y2, self.pts)

				if (bb1.density > bb2.density): # First half has larger density
					bb = bb1
				elif (bb2.density > bb1.density): # Second half has larger density
					bb = bb2
			else:
				y_center = (parent.y2 + parent.y1) / 2
				bb1 = BoundingBox(parent.x1, parent.y1, parent.x2, y_center, self.pts)
				bb2 = BoundingBox(parent.x1, y_center, parent.x2, parent.y2, self.pts)

				if (bb1.density > bb2.density): # First half has larger density
					bb = bb1
				elif (bb2.density > bb1.density): # Second half has larger density
					bb = bb2

			print (parent.density, parent.numPoints, parent.area)
			count = count + 1
		coord = [parent.x1, parent.y1, parent.x2, parent.y2]
		return coord
		

loadPoints(pointsIncX) # Load points from csv file
loadPoints(pointsIncY) # Load points from csv file

quickSort(pointsIncX, 0) # Sort the points by increasing x value
quickSort(pointsIncY, 1) # Sort the points by increasing y value

bb = BoundingBox(pointsIncX[0][0], pointsIncY[0][1], pointsIncX[len(pointsIncX) - 1][0], pointsIncY[len(pointsIncY) - 1][1], pointsIncX)

coord = bb.fullestSubRectangle() 
print(coord)
