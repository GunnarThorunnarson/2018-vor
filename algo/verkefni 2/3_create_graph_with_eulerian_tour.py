def create_tour(nodes):
    edges = []
    for num, node in enumerate(nodes):
        if num+1 == len(nodes):
            edges.append((node, nodes[0]))
        else:
            edges.append((node, nodes[num+1]))

    return edges
