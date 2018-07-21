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
problem.addVariables(["Daily Ray","Foxy Roxy","Samantha","Watery Pete",
                     "Armstrong","Jacobson","Romero","Yang", 
                     "Arno's Spit","Betty Beach","Rainbow Reef","Trey's Tunnel"], [3,4,5,6])

problem.addConstraint(AllDifferentConstraint(), ["Daily Ray","Foxy Roxy","Samantha","Watery Pete"])
problem.addConstraint(AllDifferentConstraint(), ["Armstrong","Jacobson","Romero","Yang"])
problem.addConstraint(AllDifferentConstraint(), ["Arno's Spit","Betty Beach","Rainbow Reef","Trey's Tunnel"])

#Clue#1
problem.addConstraint(lambda x, y, z: (x == y and x != z) or (x == z and x != y), ["Daily Ray","Rainbow Reef","Romero"])

#Clue#2
problem.addConstraint(lambda x, y: x < y, ["Rainbow Reef","Watery Pete"])

#Clue#3
problem.addConstraint(AllDifferentConstraint(), ["Rainbow Reef","Yang","Samantha"])

#Clue#4
problem.addConstraint(lambda x, y: x == y+2, ["Betty Beach","Rainbow Reef"])

#Clue#5
problem.addConstraint(lambda x: x != 5, ["Arno's Spit"])

#Clue#6
problem.addConstraint(lambda x, y: (x == 3 and y != 3) or (x != 3 and y == 3), ["Yang","Samantha"])

#Clue#7
problem.addConstraint(lambda x, y, z: (x == 3 and y == z) or (x == z and y == 3), ["Foxy Roxy","Betty Beach","Armstrong"])

#Clue#8
problem.addConstraint(lambda x, y: x == y, ["Samantha","Betty Beach"])

print("Solution Set:")
solution = problem.getSolutions()
print(solution)

print("\nSolution:")
for dict in solution:
   print ["3 manatees"] + [variable for variable, value in dict.iteritems() if value == 3]
   print ["4 manatees"] + [variable for variable, value in dict.iteritems() if value == 4]
   print ["5 manatees"] + [variable for variable, value in dict.iteritems() if value == 5]
   print ["6 manatees"] + [variable for variable, value in dict.iteritems() if value == 6]

print("\nRunning Time in seconds:")

end = time.time()
print(end-start)
