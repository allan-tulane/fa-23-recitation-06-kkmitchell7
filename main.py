def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)
    

    
def fib_top_down(n, fibs):
    if fibs[n] != -1:
        return fibs[n]

    if n <= 1:
        return n
    else:
        fibs[n] += 1
        return fib_recursive(n-1, fibs) + fib_recursive(n-2, fibs)

#In the first one, we'll keep an additional list called `fibs`, where `fibs[i] = F_i`, to store each value we encounter 
# during the recursive solution. When the function is called for input $i$, we first check if $F_i$ is in `fibs`. 
# If so, we simply return it. Otherwise, we proceed with the recursive calls. Note that we initialize `fibs` with -1's 
# so we can tell if $F_i$ has been computed or not. Complete `fib_top_down` and test with `test_fib_top_down`. 



def fib_bottom_up(n):
    fibnums = [0] * (n+1)
 
    num1,num2 = 0,1
    for i in range(n):
        fibnums[i] = num2
        num1,num2 = num2,num1+num2
    
    return fibnums[n-1]

#This is a non-recursive solution that starts at $F_0$ and iteratively computes subsequent values of $F_i$ until $F_n$ is reached. 
# To do so, store a list of $n+1$ values, initialized to 0's, which will store the Fibonacci sequence up from $F_0$ to $F_n$. 
# Write a for loop to fill it in, then return the last value. Complete `fib_bottom_up` and test with `test_fib_bottom_up`.


def fib_bottom_up_better(n):
    ###TODO
    pass
