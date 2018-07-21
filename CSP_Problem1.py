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
problem.addVariables(["Ella","Henrietta","Omar","Valerie",
                     "black","blue","pink","silver"], [15,25,35,45])

problem.addConstraint(AllDifferentConstraint(), ["Ella","Henrietta","Omar","Valerie"])
problem.addConstraint(AllDifferentConstraint(), ["black","blue","pink","silver"])

#Clue#1
problem.addConstraint(lambda x: x == 35, ["Henrietta"])

#Clue#2
problem.addConstraint(lambda x, y: x == y, ["Henrietta","silver"])

#Clue#3
problem.addConstraint(lambda x, y: x > y, ["Omar","silver"])

#Clue#4
problem.addConstraint(lambda x, y: x == y+10, ["Ella","black"])

#Clue#5
problem.addConstraint(lambda x, y: x == y+10, ["pink","black"])

print("Solution Set:")
solution = problem.getSolutions()
print(solution)

print("\nSolution:")
for dict in solution:
   print ["15 feet"] + [variable for variable, value in dict.iteritems() if value == 15]
   print ["25 feet"] + [variable for variable, value in dict.iteritems() if value == 25]
   print ["35 feet"] + [variable for variable, value in dict.iteritems() if value == 35]
   print ["45 feet"] + [variable for variable, value in dict.iteritems() if value == 45]

print("\nRunning Time in seconds:")
end = time.time()
print(end-start)
