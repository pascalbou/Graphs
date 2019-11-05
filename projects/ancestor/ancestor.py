from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # MASTER PLAN
    # add all ancestors to graph
    # one individual is a vertex
    # add parents as edges

    # use dfs to find earliest ancestor
    # if no parent return -1


    # create the graph
    graph = Graph()
    
    # fill the graph with individuals
    for i in range(len(ancestors)):
        parent = ancestors[i][0]
        child = ancestors[i][1]
        graph.add_vertex(parent)
        graph.add_vertex(child)
        # add edges(relations between individuals)
        graph.add_edge(child, parent)

    # print(graph.vertices)

    # create list of result in case there are several earliest ancestors
    result = []
    result.append(graph.earliest(starting_node))
    # print(result)

    # if no ancestor if found return -1
    if result[0] == starting_node:
        return -1
    # else return lowest ancestor id
    else:
        return min(result)
