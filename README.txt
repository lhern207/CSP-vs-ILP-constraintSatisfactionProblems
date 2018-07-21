Quizzles are constraint satisfaction problems in which some premises are known 
and we must reach a conclusion for which no premise is contradictory.

Here we solve 4 quizzles using the basic ARC-3 CSP algorithm implemented by the pulp library.
The main goal is to define the constraints in python code. The actual calculations of the constraints
are executed by the library for us.

The 4 quizzles are then solved using Integer Linear Programming(ILP). In this case the constraints are
more difficult to define.

CSP results in a faster execution time than ILP.
This indicates that when solving a CSP, the efficiency of an algorithm is as important as the complexity 
of the constraints needed for the algorithm to solve the problem.