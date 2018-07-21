#!/usr/bin/python
'''
Student Name: Lester Hernandez Alfonso
Panther ID: 4017986
Course: CAP4630 - U01
Assignment#2
'''

from pulp import *
import time

start = time.time()

prob = LpProblem("Puzzle 3",LpMinimize)

fines = [25, 50, 75, 100]
cars = ["Cavalo", "Fierro", "Grandero", "Injitsu"]
plates = ["FRZ-192", "GGZ-007", "MRT-628", "YGA-441"]
states = ["Alaska", "Colorado", "Hawaii", "Louisiana"]

#Create all variables
cars_vars = LpVariable.dicts("choice",(cars, fines),0,1,LpInteger)
plates_vars = LpVariable.dicts("choice",(plates, fines),0,1,LpInteger)
states_vars = LpVariable.dicts("choice",(states, fines),0,1,LpInteger)

prob += 0, "Arbitrary Objective Function"

#Global Constraints
for c in cars:
    prob += lpSum([cars_vars[c][f] for f in fines]) <= 1, ""
    prob += -lpSum([cars_vars[c][f] for f in fines]) <= -1, ""

for f in fines:
    prob += lpSum([cars_vars[c][f] for c in cars]) <= 1, ""
    prob += -lpSum([cars_vars[c][f] for c in cars]) <= -1, ""

for p in plates:
    prob += lpSum([plates_vars[p][f] for f in fines]) <= 1, ""
    prob += -lpSum([plates_vars[p][f] for f in fines]) <= -1, ""

for f in fines:
    prob += lpSum([plates_vars[p][f] for p in plates]) <= 1, ""
    prob += -lpSum([plates_vars[p][f] for p in plates]) <= -1, ""

for s in states:
    prob += lpSum([states_vars[s][f] for f in fines]) <= 1, ""
    prob += -lpSum([states_vars[s][f] for f in fines]) <= -1, ""

for f in fines:
    prob += lpSum([states_vars[s][f] for s in states]) <= 1, ""
    prob += -lpSum([states_vars[s][f] for s in states]) <= -1, ""



#Clue#1
prob += states_vars["Hawaii"][100] <= 0, ""
prob += plates_vars["YGA-441"][25] <= 0, ""

prob += states_vars["Hawaii"][75] + plates_vars["YGA-441"][100] <= 2, ""
prob += states_vars["Hawaii"][75] + plates_vars["YGA-441"][75] <= 1, ""
prob += states_vars["Hawaii"][75] + plates_vars["YGA-441"][50] <= 1, ""

prob += states_vars["Hawaii"][50] + plates_vars["YGA-441"][100] <= 1, ""
prob += states_vars["Hawaii"][50] + plates_vars["YGA-441"][75] <= 2, ""
prob += states_vars["Hawaii"][50] + plates_vars["YGA-441"][50] <= 1, ""

prob += states_vars["Hawaii"][25] + plates_vars["YGA-441"][100] <= 1, ""
prob += states_vars["Hawaii"][25] + plates_vars["YGA-441"][75] <= 1, ""
prob += states_vars["Hawaii"][25] + plates_vars["YGA-441"][50] <= 2, ""



#Clue#2
prob += cars_vars["Fierro"][100] <= 0, ""
prob += plates_vars["GGZ-007"][25] <= 0, ""

prob += cars_vars["Fierro"][75] + plates_vars["GGZ-007"][100] <= 2, ""
prob += cars_vars["Fierro"][75] + plates_vars["GGZ-007"][75] <= 1, ""
prob += cars_vars["Fierro"][75] + plates_vars["GGZ-007"][50] <= 1, ""

prob += cars_vars["Fierro"][50] + plates_vars["GGZ-007"][100] <= 2, ""
prob += cars_vars["Fierro"][50] + plates_vars["GGZ-007"][75] <= 2, ""
prob += cars_vars["Fierro"][50] + plates_vars["GGZ-007"][50] <= 1, ""

prob += cars_vars["Fierro"][25] + plates_vars["GGZ-007"][100] <= 2, ""
prob += cars_vars["Fierro"][25] + plates_vars["GGZ-007"][75] <= 2, ""
prob += cars_vars["Fierro"][25] + plates_vars["GGZ-007"][50] <= 2, ""



#Clue#3
for f in fines:
   prob += states_vars["Colorado"][f] + cars_vars["Grandero"][f] + cars_vars["Fierro"][f] + cars_vars["Injitsu"][f] <= 1,""



#Clue#4
prob += cars_vars["Grandero"][50] <= 0, ""
prob += cars_vars["Injitsu"][50] <= 0, ""

for f in fines:
   if f == 50:
      continue
   prob += cars_vars["Grandero"][f] + cars_vars["Injitsu"][f] <= 1, ""



#Clue#5
prob += cars_vars["Fierro"][100] <= 0, ""
prob += states_vars["Alaska"][25] <= 0, ""

prob += cars_vars["Fierro"][75] + states_vars["Alaska"][100] <= 2, ""
prob += cars_vars["Fierro"][75] + states_vars["Alaska"][75] <= 1, ""
prob += cars_vars["Fierro"][75] + states_vars["Alaska"][50] <= 1, ""

prob += cars_vars["Fierro"][50] + states_vars["Alaska"][100] <= 1, ""
prob += cars_vars["Fierro"][50] + states_vars["Alaska"][75] <= 2, ""
prob += cars_vars["Fierro"][50] + states_vars["Alaska"][50] <= 1, ""

prob += cars_vars["Fierro"][25] + states_vars["Alaska"][100] <= 1, ""
prob += cars_vars["Fierro"][25] + states_vars["Alaska"][75] <= 1, ""
prob += cars_vars["Fierro"][25] + states_vars["Alaska"][50] <= 2, ""



#Clue#6
prob += plates_vars["FRZ-192"][100] <= 0, ""
prob += cars_vars["Grandero"][25] <= 0, ""

prob += plates_vars["FRZ-192"][75] + cars_vars["Grandero"][100] <= 2, ""
prob += plates_vars["FRZ-192"][75] + cars_vars["Grandero"][75] <= 1, ""
prob += plates_vars["FRZ-192"][75] + cars_vars["Grandero"][50] <= 1, ""

prob += plates_vars["FRZ-192"][50] + cars_vars["Grandero"][100] <= 2, ""
prob += plates_vars["FRZ-192"][50] + cars_vars["Grandero"][75] <= 2, ""
prob += plates_vars["FRZ-192"][50] + cars_vars["Grandero"][50] <= 1, ""

prob += plates_vars["FRZ-192"][25] + cars_vars["Grandero"][100] <= 2, ""
prob += plates_vars["FRZ-192"][25] + cars_vars["Grandero"][75] <= 2, ""
prob += plates_vars["FRZ-192"][25] + cars_vars["Grandero"][50] <= 2, ""



#Clue#7
prob += plates_vars["GGZ-007"][100] <= 0, ""


prob.writeLP("Puzzle3.lp")
prob.solve()

print("Status:", LpStatus[prob.status])

#Retrieve and display solution
result1 = ["$25"]
result2 = ["$50"]
result3 = ["$75"]
result4 = ["$100"]

for v in prob.variables():
   if v.varValue == 1:
       s = v.name.split("_")
       size = len(s)

       if size == 3:
          if s[2] == "25":
             result1 += [s[1]]
          elif s[2] == "50":
             result2 += [s[1]]
          elif s[2] == "75":
             result3 += [s[1]]
          else:
             result4 += [s[1]]
       else:
          if s[3] == "25":
             result1 += [s[1] + " " + s[2]]
          elif s[3] == "50":
             result2 += [s[1] + " " + s[2]]
          elif s[3] == "75":
             result3 += [s[1] + " " + s[2]]
          else:
             result4 += [s[1] + " " + s[2]]


print ("Solution:")
print result1
print result2
print result3
print result4

print("\nRunning Time in seconds:")
end = time.time()
print(end-start)
