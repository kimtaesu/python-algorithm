# Python3 Program to Detect
# if two integers have
# opposite signs.
def oppositeSigns(x, y):
    return ((x ^ y) < 0)
# return ((x ^ y) >> 31)


x = 100
y = 1

if (oppositeSigns(x, y) == True):
    print("Signs are opposite")
else:
    print("Signs are not opposite")

# This article is contributed by Prerna Saini.

print(1 >> 31)