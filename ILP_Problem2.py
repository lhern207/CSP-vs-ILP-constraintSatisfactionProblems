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

prob = LpProblem("Puzzle 2",LpMinimize)

manatees = [3, 4, 5, 6]
boats = ["Daily Ray", "Foxy Roxy", "Samantha", "Watery Pete"]
captains = ["Armstrong", "Jacobson", "Romero", "Yang"]
locations = ["Arno's Spit", "Betty Beach", "Rainbow Reef", "Trey's Tunnel"]

#Create all variables
boats_vars = LpVariable.dicts("choice",(boats, manatees),0,1,LpInteger)
captains_vars = LpVariable.dicts("choice",(captains, manatees),0,1,LpInteger)
locations_vars = LpVariable.dicts("choice",(locations, manatees),0,1,LpInteger)

prob += 0, "Arbitrary Objective Function"

#Global Constraints
for b in boats:
    prob += lpSum([boats_vars[b][m] for m in manatees]) <= 1, ""
    prob += -lpSum([boats_vars[b][m] for m in manatees]) <= -1, ""

for m in manatees:
    prob += lpSum([boats_vars[b][m] for b in boats]) <= 1, ""
    prob += -lpSum([boats_vars[b][m] for b in boats]) <= -1, ""

for c in captains:
    prob += lpSum([captains_vars[c][m] for m in manatees]) <= 1, ""
    prob += -lpSum([captains_vars[c][m] for m in manatees]) <= -1, ""

for m in manatees:
    prob += lpSum([captains_vars[c][m] for c in captains]) <= 1, ""
    prob += -lpSum([captains_vars[c][m] for c in captains]) <= -1, ""

for l in locations:
    prob += lpSum([locations_vars[l][m] for m in manatees]) <= 1, ""
    prob += -lpSum([locations_vars[l][m] for m in manatees]) <= -1, ""

for m in manatees:
    prob += lpSum([locations_vars[l][m] for l in locations]) <= 1, ""
    prob += -lpSum([locations_vars[l][m] for l in locations]) <= -1, ""




#Clue#1
for m in manatees:
   prob += locations_vars["Rainbow Reef"][m] + captains_vars["Romero"][m] <= 1,""
   prob += boats_vars["Daily Ray"][m] - locations_vars["Rainbow Reef"][m] - captains_vars["Romero"][m] <= 0,""


#Clue#2
prob += locations_vars["Rainbow Reef"][6] <= 0, ""
prob += boats_vars["Watery Pete"][3] <= 0, ""

prob += locations_vars["Rainbow Reef"][5] + boats_vars["Watery Pete"][6] <= 2, ""
prob += locations_vars["Rainbow Reef"][5] + boats_vars["Watery Pete"][5] <= 1, ""
prob += locations_vars["Rainbow Reef"][5] + boats_vars["Watery Pete"][4] <= 1, ""

prob += locations_vars["Rainbow Reef"][4] + boats_vars["Watery Pete"][6] <= 2, ""
prob += locations_vars["Rainbow Reef"][4] + boats_vars["Watery Pete"][5] <= 2, ""
prob += locations_vars["Rainbow Reef"][4] + boats_vars["Watery Pete"][4] <= 1, ""

prob += locations_vars["Rainbow Reef"][3] + boats_vars["Watery Pete"][6] <= 2, ""
prob += locations_vars["Rainbow Reef"][3] + boats_vars["Watery Pete"][5] <= 2, ""
prob += locations_vars["Rainbow Reef"][3] + boats_vars["Watery Pete"][4] <= 2, ""

#Clue#3
for m in manatees:
   prob += locations_vars["Rainbow Reef"][m] + captains_vars["Yang"][m] + boats_vars["Samantha"][m] <= 1,""


#Clue#4
prob += locations_vars["Rainbow Reef"][6] <= 0, ""
prob += locations_vars["Betty Beach"][3] <= 0, ""

prob += locations_vars["Rainbow Reef"][5] + locations_vars["Betty Beach"][6] <= 1, ""
prob += locations_vars["Rainbow Reef"][5] + locations_vars["Betty Beach"][5] <= 1, ""
prob += locations_vars["Rainbow Reef"][5] + locations_vars["Betty Beach"][4] <= 1, ""

prob += locations_vars["Rainbow Reef"][4] + locations_vars["Betty Beach"][6] <= 2, ""
prob += locations_vars["Rainbow Reef"][4] + locations_vars["Betty Beach"][5] <= 1, ""
prob += locations_vars["Rainbow Reef"][4] + locations_vars["Betty Beach"][4] <= 1, ""

prob += locations_vars["Rainbow Reef"][3] + locations_vars["Betty Beach"][6] <= 1, ""
prob += locations_vars["Rainbow Reef"][3] + locations_vars["Betty Beach"][5] <= 2, ""
prob += locations_vars["Rainbow Reef"][3] + locations_vars["Betty Beach"][4] <= 1, ""


#Clue#5
prob += locations_vars["Arno's Spit"][5] <= 0, ""

#Clue#6
prob += captains_vars["Yang"][3] + boats_vars["Samantha"][3] <= 1,""
prob += -captains_vars["Yang"][3] - boats_vars["Samantha"][3] <= -1,""


#Clue#7
prob += boats_vars["Foxy Roxy"][3] + locations_vars["Betty Beach"][3] <= 1,""
prob += -boats_vars["Foxy Roxy"][3] - locations_vars["Betty Beach"][3] <= -1,""

prob += captains_vars["Armstrong"][3] <= 0,""

for m in manatees:
   if m == 3:
      continue
   prob += captains_vars["Armstrong"][m] - boats_vars["Foxy Roxy"][m] - locations_vars["Betty Beach"][m] <= 0,""
   prob += -captains_vars["Armstrong"][m] + (boats_vars["Foxy Roxy"][m] + locations_vars["Betty Beach"][m]) <= 0,""



#Clue#8
for m in manatees:
   prob += boats_vars["Samantha"][m] - locations_vars["Betty Beach"][m] <= 0,""
   prob += -boats_vars["Samantha"][m] + locations_vars["Betty Beach"][m] <= 0,""



prob.writeLP("Puzzle2.lp")
prob.solve()

print("Status:", LpStatus[prob.status])

#Retrieve and display solution
result1 = ["3 manatees"]
result2 = ["4 manatees"]
result3 = ["5 manatees"]
result4 = ["6 manatees"]

for v in prob.variables():
   if v.varValue == 1:
       s = v.name.split("_")
       size = len(s)

       if size == 3:
          if s[2] == "3":
             result1 += [s[1]]
          elif s[2] == "4":
             result2 += [s[1]]
          elif s[2] == "5":
             result3 += [s[1]]
          else:
             result4 += [s[1]]
       else:
          if s[3] == "3":
             result1 += [s[1] + " " + s[2]]
          elif s[3] == "4":
             result2 += [s[1] + " " + s[2]]
          elif s[3] == "5":
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
