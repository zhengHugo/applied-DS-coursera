'''
This assignment is not runnable at my local environment.
It seems like that the file 'A4_graphs', containing five serialized Graph objects, has some problems
The Graph object in it cannot be operated by my current version of networkx
'''
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
import pickle

P1_Graphs = pickle.load(open('Assignments_course5/Week4/A4_graphs', 'rb'))

G = P1_Graphs[0]
G.degree()


#     degree_values = sorted(set(degrees.value()))
#     histogram = [
# list(degrees.values()).count(i) / float(nx.number_of_nodes(G))
# for i in degree_values]

# plt.bar(degree_values, histogram)
# plt.show()

# def graph_identification():
