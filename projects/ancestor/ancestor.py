from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # MASTER PLAN
    # add all ancestors to graph
    # one individual is a vertex
    # add parents as edges

    # use dfs to find earliest ancestor
    # if no parent return -1

    graph = Graph()
    for i in range(len(ancestors)):
        parent = ancestors[i][0]
        child = ancestors[i][1]
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)

    print(graph.vertices)