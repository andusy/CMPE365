import csv

es_files = ['datasets/es1.csv','datasets/es2.csv','datasets/es3.csv']
us_files = ['datasets/us1.csv','datasets/us2.csv','datasets/us3.csv','datasets/us4.csv']
scores = []
max_scores = [] # List of max scores starting from es1 to us4

# Look in each dataset and find the best score

# Looking at scores drawn from exponential distribution
for i in range(0,3): 
	with open(es_files[i]) as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			scores.append(row)

# Looking at the scores drawn from uniform random distribution
for i in range(0,4): 
	with open(us_files[i]) as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			scores.append(row)

# Find the max in each list
for i in range(0,len(scores)): # Check each list
	mx = float(scores[i][0])
	for j in range(0,len(scores[i])): # Check the elements in the list
		if float(scores[i][j]) > mx:
			mx = float(scores[i][j])
	max_scores.append(mx)

print (max_scores)
