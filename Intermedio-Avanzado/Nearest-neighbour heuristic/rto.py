from math import sqrt
import pandas as pd

##############################################################################
#### Read excel file (Author) ################################################

file_name = input("Please, put the name of the input file: ")

# The input should be "test1", "test2" or "test3"

# Read excel with pandas
Archivo = pd.read_excel(str(file_name) + '.xlsx')

#Read the column names
names = Archivo.columns[:]
#print(names)

# The columns are extracted
x = Archivo['X'].values
y = Archivo['Y'].values

# The "setP" is created as an empty list
setP = list()

# The coordinates of the excel file are added to the setP list
for i in range(len(x)):
	setP.append([x[i], y[i]])

##############################################################################
### calculate the Euclidean distance between two vectors (Reference[1]) ######
def euclidean_distance(row1, row2):
    
	distance = 0.0

	for i in range(len(row1)):
		distance = distance + (row1[i] - row2[i])**2

	return sqrt(distance)

##############################################################################
### Locate the most similar neighbors (Reference[1])##########################
def get_neighbors(train, test_row, num_neighbors):
    
    # The "c" is created as an empty list
	distances = list()
	
	for train_row in train:
        # Euclidean distance
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))

	distances.sort(key=lambda tup: tup[1])
	neighbors = list()

	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors

##############################################################################
### (Reference[2]) ###########################################################

def tour_length(tour):
    "The total of distances between each pair of consecutive cities in the tour."
    return sum(euclidean_distance(tour[i], tour[i-1]) for i in range(len(tour)))

##############################################################################
#### Output (Author) #########################################################

num_cities = len(setP)
num_index = list()
solution = list()

print("Instance:")
for i in range(len(setP)):
	print(str(i+1) + "  " + str(setP[i][0]) + "  " + str(setP[i][1]))
    
trayect = list()
tour = list()
alltours = list()
final_tour = list()

#Get all the neighbors from all the cities
for j in range(len(setP)):
    
    neighbors = get_neighbors(setP, setP[j], num_cities)
    
    tour = list()
    num_index = list()
    
    #neighbors
    for neighbor in neighbors:
        num_index.append(neighbor)
    
    #get index
    for k in range (len(num_index)):
        indice = setP.index((num_index[k]))
        tour.append(indice)
        
    alltours.append(tour)      
    #print(tour)
    
#print(alltours)

# init points
first_point = 9
actual_point = 0

#Make the tour point to point
while (len(final_tour) < len(setP)):
    
    #The final_tour list is empty?
    if final_tour == []:
        #If is empty add the firs two points of the trayect
        final_tour.append(first_point)
    
    # Start to fill the final_tour list 
    if final_tour != []:
        
        actual_point = final_tour[-1]
        
        index_actual = alltours[actual_point]
        
        for i in range(len(index_actual)):
            if (alltours[actual_point][i] in final_tour) == False:
                final_tour.append(alltours[actual_point][i])
                break

#Add initial point at the end
final_tour.append(final_tour[0])

coordenates = list()

for i in range(len(final_tour)):
    coordenates.append(setP[int((final_tour[i]))])

final_tour_to_print = list()

for i in range(len(final_tour)):
    final_tour_to_print.append(final_tour[i] + 1)

final_distance = tour_length(coordenates)

print("Solution: " + str(final_tour_to_print))

print("Distance: " + str((final_distance)))
print()

##############################################################################
### For (Author) #############################################################

best_distance = final_distance
best_tour = final_tour_to_print

for l in range(len(setP)):
    
    trayect = list()
    tour = list()
    alltours = list()
    final_tour = list()

    #Get all the neighbors from all the cities
    for j in range(len(setP)):
    
        neighbors = get_neighbors(setP, setP[j], num_cities)
    
        tour = list()
        num_index = list()
    
        #neighbors
        for neighbor in neighbors:
            num_index.append(neighbor)
    
        #get index
        for k in range (len(num_index)):
            indice = setP.index((num_index[k]))
            tour.append(indice)
        
        alltours.append(tour)      
        #print(tour)
    
    #print(alltours)

    # init points
    actual_point = 0

    #Make the tour point to point
    while (len(final_tour) < len(setP)):
    
        #The final_tour list is empty?
        if final_tour == []:
            #If is empty add the firs two points of the trayect
            final_tour.append(l)
    
        # Start to fill the final_tour list 
        if final_tour != []:
        
            actual_point = final_tour[-1]
        
            index_actual = alltours[actual_point]
        
            for i in range(len(index_actual)):
                if (alltours[actual_point][i] in final_tour) == False:
                    final_tour.append(alltours[actual_point][i])
                    break

    #Add initial point at the end
    final_tour.append(final_tour[0])

    coordenates = list()

    for i in range(len(final_tour)):
        coordenates.append(setP[int((final_tour[i]))])

    final_tour_to_print = list()

    for i in range(len(final_tour)):
        final_tour_to_print.append(final_tour[i] + 1)

    final_distance_actual = tour_length(coordenates)
    
    if final_distance_actual < best_distance:
        best_tour = final_tour_to_print
        best_distance = final_distance_actual
    
print("Best solution: " + str(best_tour))
print("Best distance: " + str((best_distance)))
    

##############################################################################
# Reference
# [1] https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
# [2] https://jupyter.brynmawr.edu/services/public/dblank/jupyter.cs/FLAIRS-2015/TSPv3.ipynb
