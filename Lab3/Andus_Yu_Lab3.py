import csv 
import math
import numpy as np
import matplotlib.pyplot as plt

image_file = "images.csv"
coord_file = "coords.csv"

num_bits = 10
image_List = []
coord = []
best_images = []
best_coord = []

# Loads the images into a list
def loadImages():
	# Load the images into image_List
	with open(image_file) as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			image_List.append(row)

	# Load the coordinates into coord
	with open(coord_file) as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			coord.append(row)

# Calculates the hamming distance between 2 lists
def calcHamming(b1, b2): 
	count = 0 # Hamming distance
	for i in range (0,len(b1)):
		if b1[i] != b2[i]: # Characters are different
			count = count + 1 # Increment counter
	return count

# Finds the best k images
def bestImg(k):
	best_images.append(['1','1','1','1','1','1','1','1','1','1']) # Append the theoretical best image to the list

	for i in range (1, k+1): 
		count = 0
		hd = 1 # Hamming distance
		image_Found = False # Bool for if the image has been found for that iteration

		while (not image_Found): # Look for image with the specified hamming distance
			if (count == len(image_List) - 1): # Reached the end of the list
				hd = hd + 1 # Increment the hamming distance
				count = 0

			if (calcHamming(best_images[i-1], image_List[count]) == hd): # Found an image with hamming distance hd
					unique = True

					# Compare hamming distance of the currently selected image with the 
					# ones in the best_images list. If the hamming distance is 0
					# then the image is not unique and will not be appended to the list
					for j in range(0, len(best_images)):
						if (calcHamming(image_List[count], best_images[j]) == 0):
							unique = False
							break;

					if (unique): # If the image has never been seen before			
						best_images.append(image_List[count]) # Append best_images list with the current image
						best_coord.append(coord[count]) # Append the coordinate corresponding to the best image
						image_Found = True # Image was found
			count = count + 1
	best_images.pop(0)



loadImages()

bestImg(50)
for i in range(0, len(best_images)):
	print(best_images[i])

data = np.array(best_coord)
x, y = data.T
plt.scatter(x,y)
plt.show()