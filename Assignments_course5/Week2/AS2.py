import networkx as nx


def answer_one():
    G = nx.read_edgelist('Assignments_course5/Week2/email_network.txt',
                         delimiter='\t', data=[('time', int)], create_using=nx.MultiDiGraph())
    return G


def answer_two():
    G = answer_one()
    return len(G.nodes()), len(G.edges())


def answer_three():
    G = answer_one()
    return nx.is_strongly_connected(G), nx.is_weakly_connected(G)


def answer_four():
    G = answer_one()
    wcc = nx.weakly_connected_components(G)
    return len(max(wcc, key=len))


def answer_five():
    G = answer_one()
    scc = nx.strongly_connected_components(G)
    return len(max(scc, key=len))


def answer_six():
    G = answer_one()
    sccg = nx.strongly_connected_component_subgraphs(G)
    G_sc = max(sccg, key=len)
    return G_sc


def answer_seven():
    G_sc = answer_six()
    return nx.average_shortest_path_length(G_sc)


def answer_eight():
    G_sc = answer_six()
    return nx.diameter(G_sc)


def answer_nine():
    G = answer_six()
    return set(nx.periphery(G))


def answer_ten():
    G = answer_six()
    return set(nx.center(G))


def answer_eleven():
    G_sc = answer_six()
    d = nx.diameter(G_sc)
    peripheries = nx.periphery(G_sc)
    max_count = 0
    for node in peripheries:
        count = 0
        sp = nx.shortest_path_length(G_sc, node)
        for _, value in sp.items():
            if value == d:
                count += 1
        if count >= max_count:
            ans_node = node
            max_count = count
    return ans_node, max_count


def answer_twelve():
    G = answer_six()
    center = nx.center(G)[0]
    node = answer_eleven()[0]
    return len(nx.minimum_node_cut(G, center, node))


def answer_thirteen():
    G = answer_six()
    G_un = nx.Graph(G.to_undirected())
    return G_un
