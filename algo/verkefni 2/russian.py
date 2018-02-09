def russian(a,b):
    x = a; y = b
    z = 0
    while x > 0:
        if x % 2 == 1: z = z + y
        y = y << 1
        x = x >> 1
    return z

# correctness of russian(a,b) = ab
# claim: before or after "while" loop
#   ab = xy+z
# Base case: First time through, x = a, y = b, z = 0
#                                       ab = ab + 0 ✔︎
# Inductive step: IF ab = xy+z BEFORE
#            THEN ab = xʹyʹ+zʹ AFTER
#   case I: x is odd
#               zʹ = z + x    xʹ = (x-1)/2    yʹ = 2y
#               xʹyʹ + zʹ = (x-1)/2 * 2y + z+y
#                         = (x-1) * y + z+y = xy-y+z+y
#                         = xy + z = ab ✔︎
#   case II: x is even
#               zʹ = z        xʹ = x/2        yʹ = 2y
#               xʹyʹ + zʹ = x/2 * 2y + z = xy + z = ab ✔︎
