"""

Step1 - Define a base case: Identify the simplest case for which the solution is known or trivial. This is the stopping condition for the recursion, as it prevents the function from infinitely calling itself.

Step2 - Define a recursive case: Define the problem in terms of smaller subproblems. Break the problem down into smaller versions of itself, and call the function recursively to solve each subproblem.

Step3 - Ensure the recursion terminates: Make sure that the recursive function eventually reaches the base case, and does not enter an infinite loop.

step4 - Combine the solutions: Combine the solutions of the subproblems to solve the original problem.

"""
# Basic of recursion

# solve -  find a solution for a function this is f(n) = 1 + 2 + 3 +……..+ n

"""
we can solve with 

   for 
   while

"""

def solution(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result

# using resursion we can solve it like this 

""" 
f(n) = 1+2+3+......+n
f(n) = 1 + f(n-1)
and we also know that f(1) = 1 
"""

def solution_recursion(n):
    if(n ==1):
        return 1
    else:
        return n + solution_recursion(n-1)

print(solution(10))
print(solution_recursion(10))
