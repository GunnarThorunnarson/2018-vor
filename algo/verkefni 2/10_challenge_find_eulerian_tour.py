# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    # your code here
    return []


def test_tour(graph, tour):
    t = tour
    g = graph
    a = None
    b = None
    while len(t) > 2:
        a = t.pop(0)
        b = t[0]
        # print(a, "->", b)
    a = t.pop(0)
    b = t.pop(0)
    print (a, " -> ", b)

test_tour([], [1, 2, 3, 4])
