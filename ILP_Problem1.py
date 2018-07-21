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

prob = LpProblem("Puzzle 1",LpMinimize)

distances = [15, 25, 35, 45]
students = ["Ella", "Henrietta", "Omar", "Valerie"]
colors = ["black", "blue", "pink", "silver"]

#Create all student and color variables. Store them in their corresponding lists
#student_vars[students][distances] and colors_vars[colors][distances]
students_vars = LpVariable.dicts("choice",(students, distances),0,1,LpInteger)
colors_vars = LpVariable.dicts("choice",(colors, distances),0,1,LpInteger)

prob += 0, "Arbitrary Objective Function"

#Constraint: Each student can only have one distance value combination set to 1
for s in students:
    prob += lpSum([students_vars[s][d] for d in distances]) <= 1, ""
    prob += -lpSum([students_vars[s][d] for d in distances]) <= -1, ""

#Constraint: Distance values must be unique amongst all student variables
for d in distances:
    prob += lpSum([students_vars[s][d] for s in students]) <= 1, ""
    prob += -lpSum([students_vars[s][d] for s in students]) <= -1, ""

#Constraint: Each color can only have one distance value combination set to 1
for c in colors:
    prob += lpSum([colors_vars[c][d] for d in distances]) <= 1, ""
    prob += -lpSum([colors_vars[c][d] for d in distances]) <= -1, ""    

#Constraint: Distance values must be unique amongst all color variables
for d in distances:
    prob += lpSum([colors_vars[c][d] for c in colors]) <= 1, ""
    prob += -lpSum([colors_vars[c][d] for c in colors]) <= -1, ""



#Clue#1
prob += students_vars["Henrietta"][35] <= 1,""
prob += -students_vars["Henrietta"][35] <= -1,""



#Clue#2
for d in distances:
   prob += students_vars["Henrietta"][d] - colors_vars["silver"][d] <= 0,""
   prob += -students_vars["Henrietta"][d] + colors_vars["silver"][d] <= 0,""



#Clue#3
prob += colors_vars["silver"][45] <= 0, ""
prob += students_vars["Omar"][15] <= 0, ""

prob += colors_vars["silver"][35] + students_vars["Omar"][45] <= 2, ""
prob += colors_vars["silver"][35] + students_vars["Omar"][35] <= 1, ""
prob += colors_vars["silver"][35] + students_vars["Omar"][25] <= 1, ""

prob += colors_vars["silver"][25] + students_vars["Omar"][45] <= 2, ""
prob += colors_vars["silver"][25] + students_vars["Omar"][35] <= 2, ""
prob += colors_vars["silver"][25] + students_vars["Omar"][25] <= 1, ""

prob += colors_vars["silver"][15] + students_vars["Omar"][45] <= 2, ""
prob += colors_vars["silver"][15] + students_vars["Omar"][35] <= 2, ""
prob += colors_vars["silver"][15] + students_vars["Omar"][25] <= 2, ""




#Clue#4
prob += colors_vars["black"][45] <= 0, ""
prob += students_vars["Ella"][15] <= 0, ""

prob += colors_vars["black"][35] + students_vars["Ella"][45] <= 2, ""
prob += colors_vars["black"][35] + students_vars["Ella"][35] <= 1, ""
prob += colors_vars["black"][35] + students_vars["Ella"][25] <= 1, ""

prob += colors_vars["black"][25] + students_vars["Ella"][45] <= 1, ""
prob += colors_vars["black"][25] + students_vars["Ella"][35] <= 2, ""
prob += colors_vars["black"][25] + students_vars["Ella"][25] <= 1, ""

prob += colors_vars["black"][15] + students_vars["Ella"][45] <= 1, ""
prob += colors_vars["black"][15] + students_vars["Ella"][35] <= 1, ""
prob += colors_vars["black"][15] + students_vars["Ella"][25] <= 2, ""



#Clue#5
prob += colors_vars["black"][45] <= 0, ""
prob += colors_vars["pink"][15] <= 0, ""

prob += colors_vars["black"][35] + colors_vars["pink"][45] <= 2, ""
prob += colors_vars["black"][35] + colors_vars["pink"][35] <= 1, ""
prob += colors_vars["black"][35] + colors_vars["pink"][25] <= 1, ""

prob += colors_vars["black"][25] + colors_vars["pink"][45] <= 1, ""
prob += colors_vars["black"][25] + colors_vars["pink"][35] <= 2, ""
prob += colors_vars["black"][25] + colors_vars["pink"][25] <= 1, ""

prob += colors_vars["black"][15] + colors_vars["pink"][45] <= 1, ""
prob += colors_vars["black"][15] + colors_vars["pink"][35] <= 1, ""
prob += colors_vars["black"][15] + colors_vars["pink"][25] <= 2, ""


prob.writeLP("Puzzle1.lp")
prob.solve()

print("Status:", LpStatus[prob.status])

#Retrieve and display solution
result1 = ["15 feet"]
result2 = ["25 feet"]
result3 = ["35 feet"]
result4 = ["45 feet"]

for v in prob.variables():
   if v.varValue == 1:
       s = v.name.split("_")
       size = len(s)

       if size == 3:
          if s[2] == "15":
             result1 += [s[1]]
          elif s[2] == "25":
             result2 += [s[1]]
          elif s[2] == "35":
             result3 += [s[1]]
          else:
             result4 += [s[1]]
       else:
          if s[3] == "15":
             result1 += [s[1] + " " + s[2]]
          elif s[3] == "25":
             result2 += [s[1] + " " + s[2]]
          elif s[3] == "35":
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

