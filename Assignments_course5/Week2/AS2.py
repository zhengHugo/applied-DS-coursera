import networkx as nx


def answer_one():
    G = nx.read_edgelist('Assignments_course5/Week2/email_network.txt',
                         delimiter='\t', data=[('time', int)], create_using=nx.MultiDiGraph())
    return G


def answer_two():
    G = answer_one()
    return len(G.nodes()), len(G.edges())
