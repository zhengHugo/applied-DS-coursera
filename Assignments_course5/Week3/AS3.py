import networkx as nx

G1 = nx.read_gml('Assignments_course5/Week3/friendships.gml')


def answer_one():
    degree_centrality = nx.degree_centrality(G1)[100]
    closeness_centrality = nx.closeness_centrality(G1)[100]
    betweenness_centrality = nx.betweenness_centrality(
        G1, endpoints=False, normalized=True)[100]
    return degree_centrality, closeness_centrality, betweenness_centrality


def answer_two():
    degrees = nx.degree_centrality(G1)
    return max(degrees, key=degrees.get)
