# Fibonacci number: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584

# the Fibonacci function which is function to find order of fibonacci number 
# recursion function 
def fibonacci(n):
    # count = 0

    # the inner function 
    def fi1(n):
        # nonlocal count 
        # count += 1
        if n < 2:
            return n
        else:
            return fi1(n-1) + fi1(n-2)

    return fi1(n)

# recursion function 
def opt_fibonacci(n):
    # the dictionary is the keys-values which cache repeatedly calculated values for saving memory from computing iteration
    collect = {}
    # count = 0

    # the inner function
    def fi2(n):
        # nonlocal count 
        # count += 1
 
        # if the dictionary don't have the value, move to compute the suborder Fibonacci
        if n in collect:
            return collect[n]
        else:
            if n < 2:
                return n
            else:
                # add the value to the dictionary
                collect[n] = fi2(n-1) + fi2(n-2)
                return collect[n]

    return fi2(n)

print(fibonacci(5))
print(opt_fibonacci(5))
