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

prob = LpProblem("Puzzle 4",LpMinimize)

months = [1, 2, 3, 4]
drugs = ["Bizolam", "Damasol", "Favolin", "Gravon"]
conditions = ["dengue fever", "diabetes", "heart disease", "influenza"]
sources = ["beetle", "bromeliad", "frog", "mushroom"]


#Create all variables
drugs_vars = LpVariable.dicts("choice",(drugs, months),0,1,LpInteger)
conditions_vars = LpVariable.dicts("choice",(conditions, months),0,1,LpInteger)
sources_vars = LpVariable.dicts("choice",(sources, months),0,1,LpInteger)

prob += 0, "Arbitrary Objective Function"

#Global Constraints
for d in drugs:
    prob += lpSum([drugs_vars[d][m] for m in months]) <= 1, ""
    prob += -lpSum([drugs_vars[d][m] for m in months]) <= -1, ""

for m in months:
    prob += lpSum([drugs_vars[d][m] for d in drugs]) <= 1, ""
    prob += -lpSum([drugs_vars[d][m] for d in drugs]) <= -1, ""

for c in conditions:
    prob += lpSum([conditions_vars[c][m] for m in months]) <= 1, ""
    prob += -lpSum([conditions_vars[c][m] for m in months]) <= -1, ""

for m in months:
    prob += lpSum([conditions_vars[c][m] for c in conditions]) <= 1, ""
    prob += -lpSum([conditions_vars[c][m] for c in conditions]) <= -1, ""

for s in sources:
    prob += lpSum([sources_vars[s][m] for m in months]) <= 1, ""
    prob += -lpSum([sources_vars[s][m] for m in months]) <= -1, ""

for m in months:
    prob += lpSum([sources_vars[s][m] for s in sources]) <= 1, ""
    prob += -lpSum([sources_vars[s][m] for s in sources]) <= -1, ""



#Clue#1
for m in months:
   prob += sources_vars["mushroom"][m] - conditions_vars["heart disease"][m] <= 0,""
   prob += -sources_vars["mushroom"][m] + conditions_vars["heart disease"][m] <= 0,""



#Clue#2
for m in months:
   prob += sources_vars["mushroom"][m] - conditions_vars["heart disease"][m] <= 0,""
   prob += -sources_vars["mushroom"][m] + conditions_vars["heart disease"][m] <= 0,""


#Clue#3
prob += conditions_vars["heart disease"][3] + sources_vars["beetle"][3] <= 1,""
prob += -conditions_vars["heart disease"][3] - sources_vars["beetle"][3] <= -1,""

prob += drugs_vars["Damasol"][3] <= 0,""

for m in months:
   if m == 3:
      continue
   prob += drugs_vars["Damasol"][m] - conditions_vars["heart disease"][m] - sources_vars["beetle"][m] <= 0,""
   prob += -drugs_vars["Damasol"][m] + conditions_vars["heart disease"][m] + sources_vars["beetle"][m] <= 0,""



#Clue#4
prob += conditions_vars["diabetes"][4] <= 0, ""
prob += drugs_vars["Favolin"][1] <= 0, ""

prob += conditions_vars["diabetes"][3] + drugs_vars["Favolin"][4] <= 1, ""
prob += conditions_vars["diabetes"][3] + drugs_vars["Favolin"][3] <= 1, ""
prob += conditions_vars["diabetes"][3] + drugs_vars["Favolin"][2] <= 1, ""

prob += conditions_vars["diabetes"][2] + drugs_vars["Favolin"][4] <= 2, ""
prob += conditions_vars["diabetes"][2] + drugs_vars["Favolin"][3] <= 1, ""
prob += conditions_vars["diabetes"][2] + drugs_vars["Favolin"][2] <= 1, ""

prob += conditions_vars["diabetes"][1] + drugs_vars["Favolin"][4] <= 1, ""
prob += conditions_vars["diabetes"][1] + drugs_vars["Favolin"][3] <= 2, ""
prob += conditions_vars["diabetes"][1] + drugs_vars["Favolin"][2] <= 1, ""


#Clue#5
prob += conditions_vars["diabetes"][4] <= 0, ""
prob += sources_vars["bromeliad"][4] <= 0, ""

for m in months:
   if m == 4:
      continue
   prob += conditions_vars["diabetes"][m] + sources_vars["bromeliad"][m] <= 1, ""



#Clue#6
prob += sources_vars["bromeliad"][3] <= 0,""

for m in months:
   prob += drugs_vars["Gravon"][m] - drugs_vars["Gravon"][3] - sources_vars["bromeliad"][m] <= 0,""


#Clue#7
for m in months:
   prob += drugs_vars["Favolin"][m] + sources_vars["beetle"][m] <= 1,""


prob.writeLP("Puzzle4.lp")
prob.solve()

print("Status:", LpStatus[prob.status])

#Retrieve and display variable
result1 = ["January"]
result2 = ["February"]
result3 = ["March"]
result4 = ["April"]

for v in prob.variables():
   if v.varValue == 1:
       s = v.name.split("_")
       size = len(s)

       if size == 3:
          if s[2] == "1":
             result1 += [s[1]]
          elif s[2] == "2":
             result2 += [s[1]]
          elif s[2] == "3":
             result3 += [s[1]]
          else:
             result4 += [s[1]]
       else:
          if s[3] == "1":
             result1 += [s[1] + " " + s[2]]
          elif s[3] == "2":
             result2 += [s[1] + " " + s[2]]
          elif s[3] == "3":
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
