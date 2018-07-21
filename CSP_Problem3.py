#!/usr/bin/python
from constraint import *
import time

start = time.time()

problem = Problem()
problem.addVariables(["Cavalo","Fierro","Grandero","Injitsu",
                     "FRZ-192","GGZ-007","MRT-628","YGA-441", 
                     "Alaska","Colorado","Hawaii","Louisiana"], [25,50,75,100])

problem.addConstraint(AllDifferentConstraint(), ["Cavalo","Fierro","Grandero","Injitsu"])
problem.addConstraint(AllDifferentConstraint(), ["FRZ-192","GGZ-007","MRT-628","YGA-441"])
problem.addConstraint(AllDifferentConstraint(), ["Alaska","Colorado","Hawaii","Louisiana"])

#Clue1
problem.addConstraint(lambda x, y: x == y+25, ["YGA-441","Hawaii"])

#Clue#2
problem.addConstraint(lambda x, y: x < y, ["Fierro","GGZ-007"])

#Clue#3
problem.addConstraint(AllDifferentConstraint(), ["Colorado","Grandero","Fierro","Injitsu"])

#Clue#4
problem.addConstraint(lambda x, y: x != 50 and y != 50 and x != y, ["Grandero","Injitsu"])

#Clue#5
problem.addConstraint(lambda x, y: x == y+25, ["Alaska","Fierro"])

#Clue#6
problem.addConstraint(lambda x, y: x > y, ["Grandero","FRZ-192"])

#Clue#7
problem.addConstraint(lambda x: x != 100, ["GGZ-007"])

print("Solution Set:")
solution = problem.getSolutions()
print(solution)


print("\nSolution:")
for dict in solution:
   print ["$25"] + [variable for variable, value in dict.iteritems() if value == 25]
   print ["$50"] + [variable for variable, value in dict.iteritems() if value == 50]
   print ["$75"] + [variable for variable, value in dict.iteritems() if value == 75]
   print ["$100"] + [variable for variable, value in dict.iteritems() if value == 100]

print("\nRunning Time in seconds:")
end = time.time()
print(end-start)
