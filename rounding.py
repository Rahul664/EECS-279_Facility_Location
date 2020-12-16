# IMPORTS
import pandas as pd

# Reading Data from drive
PATH = "/home/ad26/Courses/EECS-279/Project/EECS-279_Facility_Location/"

df_distance = pd.read_csv(PATH+"distance.csv")
distance = df_distance.values.tolist()

df_connection = pd.read_csv(PATH+"connection-costs.csv")
connection = df_connection.values.tolist()

df_facility = pd.read_csv(PATH+"facility_cost.csv")
facility = df_facility.values.tolist()


# Replicating CSV data to data structure
N = 500 # Describes total number of data points

FACILITIES = [0 for i in range(0,N)] # Defaulting 0 1-D List | Holds the probability of facility to be opened
for index, row in df_facility.iterrows():
    idx = int(row[0])
    val = row[1]
    FACILITIES[idx] = val

DISTANCES = [[0 for j in range(0,N)] for i in range(0,500)] # Defaulting 0 | 2-D List | Holds distance(d) between any point two points A and B 
for index, row in df_distance.iterrows():
    A = int(row[0])
    B = int(row[1])
    d = row[2]
    DISTANCES[A][B] = d

CONNECTIONS = [[0 for j in range(0,N)] for i in range(0,500)] # Defaulting 0 2-D List | Holds probability of facility j connects with client i
for index, row in df_connection.iterrows():
    facility = int(row[0])
    client = int(row[1])
    val = row[2]
    CONNECTIONS[facility][client] = val


# Calulating DeltaJ and Bj
def listSum(_ListA):
  suM = 0
  for i in range(0,len(_ListA)):
    suM += _ListA[i]
  return suM

deltaJ = [0 for i in range(0,N)]
Bj = [0 for i in range(0,N)]
for j in range(0,N):
  deltaJ[j] = listSum([DISTANCES[j][i]*CONNECTIONS[j][i] for i in range(0,N)])
  Bj[j] = deltaJ[j]*2


# Calculating the final facilities and cost
FC_used = [False for i in range(0,500)]
deltaJ_sorted = sorted(deltaJ)
FINAL_FACILITY = []
TOTAL_COST = 0
F = 40
COUNT = 0 # Count the number of clients, not facilities

for val in deltaJ_sorted:
  min_deltaJ_idx = deltaJ.index(val) # Getting the index of minimum of smallest deltaJ
  
  if FC_used[min_deltaJ_idx] == True: # Check for city is already assigned to a facility or a facility 
    continue
  
  FINAL_FACILITY.append(min_deltaJ_idx) # Add the current facility in the final facility list
  TOTAL_COST += F #* FACILITIES[min_deltaJ_idx] # Adding facility opening cost towards the total cost
  
  
  for i in range(0,500):
    if i not in FINAL_FACILITY and DISTANCES[min_deltaJ_idx][i] <= Bj[min_deltaJ_idx] and FC_used[i] == False: # Check if distance(facility->client) <= Bj
      FC_used[i] = True 
      COUNT+=1
      TOTAL_COST += DISTANCES[min_deltaJ_idx][i] # * CONNECTIONS[min_deltaJ_idx][i] # Adding the distance towards total cost
      
print("######################################################################################################\n")
print("Object for 6 Approximiation rounding : ", TOTAL_COST)
print("Number of Facilities : ", len(FINAL_FACILITY))
print("Facilities open : ", FINAL_FACILITY)
print("######################################################################################################\n")


# -------------------------------------------- 4 Approximiation rounding -------------------------------------#

# Scaling FACILITIES (y_i) and  CONNECTIONS(x_ij) By (1+alpha)/alpha alpha=1/3
alpha = 1/3# Constant
sf = (1+alpha)/alpha

FACILITIES_4APX = [sf*i for i in FACILITIES]
CONNECTIONS_4APX = [ [0 for j in range(0,500)] for i in range(0,500)]

for i in range(0,500):
  for j in range(0,500):
    CONNECTIONS_4APX[i][j] = CONNECTIONS[i][j] * sf 

# Calculating deltaJ and Bj
deltaJ_4APX = [0 for i in range(0,N)]
Bj_4APX = [0 for i in range(0,N)]
for j in range(0,N):
  deltaJ_4APX[j] = listSum([DISTANCES[j][i]*CONNECTIONS_4APX[j][i] for i in range(0,N)])
  Bj_4APX[j] = deltaJ_4APX[j]*(1+alpha)

# Calculating the objective
FC_used_4APX = [False for i in range(0,500)]
deltaJ_4APX_sorted = sorted(deltaJ_4APX)
FINAL_FACILITY_4APX = []
TOTAL = 0
TOTAL_COST_4APX = 0
F = 40.16

for val in deltaJ_4APX_sorted:
  min_deltaJ_idx = deltaJ_4APX.index(val)
  
  if(FC_used_4APX[min_deltaJ_idx] == True):
    continue
  FINAL_FACILITY_4APX.append(min_deltaJ_idx)
  TOTAL_COST_4APX += F #* FACILITIES_4APX[min_deltaJ_idx]

  COUNT = 0
  
  for i in range(0,500):
    if i not in FINAL_FACILITY_4APX and DISTANCES[min_deltaJ_idx][i] <= Bj_4APX[min_deltaJ_idx] and FC_used_4APX[i] == False:
      FC_used_4APX[i] = True
      COUNT+=1
      TOTAL+=1
      TOTAL_COST_4APX += DISTANCES[min_deltaJ_idx][i] #* CONNECTIONS_4APX[min_deltaJ_idx][i]


print("Object for 4 Approximiation rounding : ", TOTAL_COST_4APX)
print("Number of Facilities : ", len(FINAL_FACILITY_4APX))
print("Facilities open : ", FINAL_FACILITY_4APX)
print("------------------------------------------------------------------------------------------------------\n")