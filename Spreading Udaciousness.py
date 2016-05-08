# Spreading Udaciousness
 
# One of our modest goals is to teach everyone in the world to program and
# understand computer science. To estimate how long this will take we have
# developed a (very flawed!) model:

# Everyone answering this question will convince a number, spread, (input to 
# the model) of their friends to take the course next offering. This will 
# continue, so that all of the newly recruited students, as well as the original
# students, will convince spread of their
# friends to take the following offering of the course.
# recruited friends are unique, so there is no duplication among the newly
# recruited students. Define a procedure, hexes_to_udaciousness(n, spread,
# target), that takes three inputs: the starting number of Udacians, the spread
# rate (how many new friends each Udacian convinces to join each hexamester),
# and the target number, and outputs the number of hexamesters needed to reach 
# (or exceed) the target.

# Recursion version

def hexes_to_udaciousness_recursive(n, spread, target):
    if n >= target:
        return 0
    else:
        return 1 + hexes_to_udaciousness_recursive(n * (1 + spread), spread, target)
       

# 0 more needed, since n already exceeds target
print hexes_to_udaciousness_recursive(100000, 2, 36230) 
#>>> 0

# after 1 hexamester, there will be 50000 + (50000 * 2) Udacians
print hexes_to_udaciousness_recursive(50000, 2, 150000) 
#>>> 1 

# need to match or exceed the target
print hexes_to_udaciousness_recursive(50000, 2, 150001)
#>>> 2 

# only 12 hexamesters (2 years) to world domination!
print hexes_to_udaciousness_recursive(20000, 2, 7 * 10 ** 9) 
#>>> 12 

# more friends means faster world domination!
print hexes_to_udaciousness_recursive(15000, 3, 7 * 10 ** 9)
#>>> 10 

# Loop version

def hexes_to_udaciousness_loop(n, spread, target):
    count = 0
    while n < target:
        n = n * (1 + spread) 
        count += 1
    return count
    
print hexes_to_udaciousness_loop(100000, 2, 36230)
print hexes_to_udaciousness_loop(50000, 2, 150000)
print hexes_to_udaciousness_loop(50000, 2, 150001)
print hexes_to_udaciousness_loop(20000, 2, 7 * 10 ** 9)
print hexes_to_udaciousness_loop(15000, 3, 7 * 10 ** 9)


