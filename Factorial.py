# Define a procedure, factorial, that takes a natural number as its input, and
# returns the number of ways to arrange the input number of items.

#loop version

def factorial_loop(n):
    m = 1
    for i in range(1, n+1):
        m = m * i
    return m


print factorial_loop(0)
#>>> 1

print factorial_loop(5)
#>>> 120

print factorial_loop(10)
#>>> 3628800

def factorial_recursive(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial_recursive(n-1)


print factorial_recursive(0)
#>>> 1

print factorial_recursive(5)
#>>> 120

print factorial_recursive(10)
#>>> 3628800
