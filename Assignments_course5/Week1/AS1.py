import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import bipartite


# This is the set of employees
employees = set(['Pablo',
                 'Lee',
                 'Georgia',
                 'Vincent',
                 'Andy',
                 'Frida',
                 'Joan',
                 'Claude'])

# This is the set of movies
movies = set(['The Shawshank Redemption',
              'Forrest Gump',
              'The Matrix',
              'Anaconda',
              'The Social Network',
              'The Godfather',
              'Monty Python and the Holy Grail',
              'Snakes on a Plane',
              'Kung Fu Panda',
              'The Dark Knight',
              'Mean Girls'])


# you can use the following function to plot graphs
# make sure to comment it out before submitting to the autograder
def plot_graph(G, weight_name=None):
    '''
    G: a networkx G
    weight_name: name of the attribute for plotting edge weights (if G is weighted)
    '''
    import matplotlib.pyplot as plt

    plt.figure()
    pos = nx.spring_layout(G)
    edges = G.edges()
    weights = None

    if weight_name:
        weights = [int(G[u][v][weight_name]) for u, v in edges]
        labels = nx.get_edge_attributes(G, weight_name)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw_networkx(G, pos, edges=edges, width=weights)
    else:
        nx.draw_networkx(G, pos, edges=edges)

    plt.show()


def answer_one():
    G = nx.read_edgelist(
        'Assignments_course5/Week1/Employee_Movie_Choices.txt', delimiter="\t")
    return G


def answer_two():
    G = answer_one()
    for node in G.nodes():
        if node in employees:
            G.add_node(node, type="employee")
        else:
            G.add_node(node, type="movie")
    return G


def answer_three():
    B = answer_two()
    P = bipartite.weighted_projected_graph(B, employees)
    return P


# Find the Pearson correlation ( using DataFrame.corr() ) between employee relationship scores and the number of movies they have in common.
def answer_four():
    rel = nx.read_edgelist(
        'Assignments_course5/Week1/Employee_Relationships.txt', data=[('relationship', int)])
    df_rel = pd.DataFrame(rel.edges(data=True), columns=[
                          'from', 'to', 'relation_score'])

    df_rel['relation_score'] = df_rel['relation_score'].apply(
        lambda x: x['relationship'])
    mov = answer_three()
    df_mov = pd.DataFrame(mov.edges(data=True), columns=[
                          'from', 'to', 'mov_common'])
    df_mov['mov_common'] = df_mov['mov_common'].apply(lambda x: x['weight'])
    df_mov_copy = df_mov.copy()
    df_mov_copy.columns = ['to', 'from', 'mov_common']
    df_mov_copy = df_mov_copy.reindex(columns=['from', 'to', 'mov_common'])
    df_mov = pd.concat([df_mov, df_mov_copy])

    df = pd.merge(df_rel, df_mov, how='outer', on=['from', 'to'])
    df = df[np.isfinite(df['relation_score'])]
    df = df.fillna(0)
    corr = df.corr(method='pearson')
    return corr


print(answer_four())
