import csv
import networkx as nx
import numpy as np

path = "datasets/"

network_path = path + "network.csv"
requests_path = path + "requests.csv"

network = []
requests = []
request_time = [] # Times that the ubers were requested at
start = [] # Start locations
end = [] # End locations

# Loads the information from the given csv file into the list
def loadData(filepath, data):
	with open(filepath) as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			data.append(row)

	# Convert the data appended to the lists from string to int
	for i in range(0, len(data)):
		for j in range(0,len(data[i])):
			data[i][j] = int(data[i][j])
	
loadData(network_path, network)
loadData(requests_path, requests)

# Seperate the requests into differents lists by request time, start nodes, and end nodes
for i in range (0, len(requests)):
	request_time.append(requests[i][0])
	start.append(requests[i][1])
	end.append(requests[i][2])

A = np.matrix(network) # Convert the 2d array to a numpy matrix
G = nx.from_numpy_matrix(A, create_using=nx.DiGraph()) # Convert the numpy matrix to a graph

time_elapsed = 0
wait_time = 0

for i in range (0, len(request_time)):
	path = nx.dijkstra_path(G, start[i] - 1, end[i] - 1) # Optimal path from start node to end node (+1 because nodes are 1-50 in csv instead of 0-49)

	# Calculate the time elapsed to complete the path
	for j in range (0, len(path) - 1):
		time_elapsed += network[path[j]][path[j+1]] # Get the edge value 

	if (i != len(request_time) - 1): # Run if not the last request
		path = nx.dijkstra_path(G, end[i] - 1, start[i + 1] - 1) # Head to the next start location

		# Calculate the time elapsed to complete the path
		for j in range (0, len(path) - 1):
			time_elapsed += network[path[j]][path[j+1]] # Get the edge value 

		if (time_elapsed > request_time[i + 1]): # If the time it took to get to the location of the request is greater than the request time
			wait_time += time_elapsed - request_time[i + 1] # Calculate the difference and add it to the wait time
		elif(time_elapsed < request_time[i + 1]): # Got there before the request was made
			time_elapsed = request_time[i + 1] # Wait for the request to be made
		print("Request No. " + str(i + 1) + " " +str(wait_time))

print ("Total wait time is " + str(wait_time))
