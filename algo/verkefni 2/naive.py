def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

# correctness of naive(a,b) = ab
# claim: before or after "while" loop
#   ab = xy+z
# Base case: First time through, x = a, y = b, z = 0
#                                       ab = ab + 0 ✔︎
# Inductive step: IF ab = xy+z BEFORE
#            THEN ab = xʹyʹ+zʹ AFTER
#                 xʹ = x-1 , yʹ = y , zʹ = z+y
#                 xʹyʹ+zʹ = (x-1)(y)+(z+y)
#                         = xy - y + z + y
#                         = xy + z
#                         = ab ✔︎
# End case: x = 0
#           ab = xy + z
#           ab = 0 *y + z
#           ab = z ✔︎
