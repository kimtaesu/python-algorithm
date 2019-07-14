# Python program to multiply any
# positive number to 7

# Function to mutiply any number with 7
def multiplyBySeven(n):
    # Note the inner bracket here.
    # This is needed because
    # precedence of '-' operator is
    # higher than '<<'
    return ((n << 3) - n)


# Driver code
n = 5
print(multiplyBySeven(n))

# This code is contributed by Danish Raza
