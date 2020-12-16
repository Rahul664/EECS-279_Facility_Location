# Importing libraries
<<<<<<< HEAD
import numpy as np
=======
>>>>>>> LinearSolver
import math
import sys
import csv
from pulp import *
from scipy.spatial import distance

# Below function will load the data in program
def load_data(PATH): 
	input_file = open(PATH,'r').read().splitlines()
	cities = []
	for coordinate in input_file:
		x = float(coordinate.split()[0])
		y = float(coordinate.split()[1])
		cities.append([x,y])
	return cities

<<<<<<< HEAD
PATH = "/home/ad26/Courses/EECS-279/Project/"
=======
PATH = "/home/ad26/Courses/EECS-279/Project/EECS-279_Facility_Location/"
>>>>>>> LinearSolver
CITIES = load_data(PATH+"500-us-city-coordinates.txt")


# SETS
CLIENT = [i for i in range(len(CITIES))]
FACILITY = [i for i in range(len(CITIES))]
DISTANCES = {}

csv_file_2 = open(PATH+"distance.csv",'w+')
csv_writer = csv.writer(csv_file_2)

for i in range(0,500):
  DISTANCES[i] = {}
  for j in range(0,500):
    DISTANCES[i][j] = distance.euclidean(CITIES[i],CITIES[j])
    csv_writer.writerow([i,j,DISTANCES[i][j]])

# PROBLEM VARIABLE
solver = LpProblem("FacilityLocation",LpMinimize)

# DECISION VARIABLE
<<<<<<< HEAD
client_facility = LpVariable.dicts("clientTOfacility",[(i,j) for i in CLIENT for j in FACILITY],0,1,cat='Continuous')
faclity_indicator = LpVariable.dicts("openedFacility",FACILITY,0,1,cat='Continuous')

# OBJECTIVE FUNCTION
f = 1 # Facility opening cost determined by Local search algorithm
solver += lpSum(f * faclity_indicator[i] for i in FACILITY) + lpSum(DISTANCES[i][j] * client_facility[(i,j)] for i in FACILITY for j in CLIENT)
=======
client_facility = LpVariable.dicts("clientTOfacility",[(i,j) for i in CLIENT for j in FACILITY],0,cat='Continuous')
faclity_indicator = LpVariable.dicts("openedFacility",FACILITY,0,cat='Continuous')

# OBJECTIVE FUNCTION
f = 40 # Facility opening cost determined by Local search algorithm
solver += lpSum(f * faclity_indicator[i] for i in FACILITY) + lpSum(DISTANCES[i][j] * client_facility[(i,j)] for i in CLIENT for j in FACILITY)
>>>>>>> LinearSolver

# CONSTRAINTS
for i in CLIENT:
  solver += lpSum(client_facility[(i,j)] for j in FACILITY) == 1 # CONSTRAINT 1

<<<<<<< HEAD
for i in CLIENT:
  for j in FACILITY:
    solver+= client_facility[(i,j)] - faclity_indicator[i] <= 0
=======
for i in CLIENT: # CONSTRAINT 2
  for j in FACILITY:
    solver+= (faclity_indicator[i] - client_facility[(i,j)])  >= 0

# solver += lpSum(faclity_indicator[i] for i in FACILITY) == 19 # CONSTRAINT 3
>>>>>>> LinearSolver


# SOLUTION
solver.solve()
print("Status",LpStatus[solver.status])

# EXPORT THE DATA
write_solver = open(PATH+"solver.txt",'w')
write_solver.write(str(solver))
write_solver.close()

csv_file_1 = open(PATH+"facility_cost.csv",'w+')
csv_writer = csv.writer(csv_file_1)
for i in FACILITY:
<<<<<<< HEAD
  # line = str(i)+','+str(faclity_indicator[i].varValue)+"\n"
=======
>>>>>>> LinearSolver
  csv_writer.writerow([i,faclity_indicator[i].varValue])


#write_connections = open(PATH+"connection-costs.txt",'w')
csv_file = open(PATH+"connection-costs.csv",'w+')
csv_writer = csv.writer(csv_file)
for i in CLIENT:
  for j in FACILITY:
<<<<<<< HEAD
    # cost = client_facility[i,j].varValue
    # line = client_facility[i,j]+','+str(cost)
=======
>>>>>>> LinearSolver
    csv_writer.writerow([i,j,client_facility[i,j].varValue])
