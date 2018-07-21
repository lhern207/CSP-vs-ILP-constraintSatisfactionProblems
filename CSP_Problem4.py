#!/usr/bin/python
'''
Student Name: Lester Hernandez Alfonso
Panther ID: 4017986
Course: CAP4630 - U01
Assignment#2
'''

from constraint import *
import time

start = time.time()

problem = Problem()

#January, February, March and April will be equal to their corresponding integer value 1,2,3,4 for convenience.
problem.addVariables(["Bizolam","Damasol","Favolin","Gravon",
                     "dengue fever","diabetes","heart disease","influenza", 
                     "beetle","bromeliad","frog","mushroom"], [1,2,3,4])

problem.addConstraint(AllDifferentConstraint(), ["Bizolam","Damasol","Favolin","Gravon"])
problem.addConstraint(AllDifferentConstraint(), ["dengue fever","diabetes","heart disease","influenza"])
problem.addConstraint(AllDifferentConstraint(), ["beetle","bromeliad","frog","mushroom"])

#Clue#1
problem.addConstraint(lambda x, y: x == y, ["mushroom","heart disease"])

#Clue#2
problem.addConstraint(lambda x, y: x == y, ["beetle","dengue fever"])

#Clue#3
problem.addConstraint(lambda x, y, z: (x == z and y == 3) or (x == 3 and y == z), ["heart disease","beetle","Damasol"])

#Clue#4
problem.addConstraint(lambda x, y: x == y+2, ["Favolin","diabetes"])

#Clue#5
problem.addConstraint(lambda x, y: x != 4 and y != 4 and x != y, ["diabetes","bromeliad"])

#Clue#6
problem.addConstraint(lambda x, y: (x == 3 and x != y) or (x == y and x != 3), ["Gravon","bromeliad"])

#Clue#7
problem.addConstraint(lambda x, y: x != y, ["Favolin", "beetle"])

print("Solution Set:")
solution = problem.getSolutions()
print(solution)

print("\nSolution:")
for dict in solution:
   print ["January"] + [variable for variable, value in dict.iteritems() if value == 1]
   print ["February"] + [variable for variable, value in dict.iteritems() if value == 2]
   print ["March"] + [variable for variable, value in dict.iteritems() if value == 3]
   print ["April"] + [variable for variable, value in dict.iteritems() if value == 4]

print("\nRunning Time in seconds:")
end = time.time()
print(end-start)
