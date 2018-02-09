def count(n):
    # + 2 for the first two statements
    # + n for the range statements
    # + Gauss's formula for calculating the sum of a range of numbers for
    #   the print statements, adapted for 0-indexing
    return 2 + n + (n+(n-1)/2)
