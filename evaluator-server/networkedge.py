import networkx as nx
import matplotlib.pyplot as plt
import json

with open('testdata/nodes.json') as f:
    data = json.loads(f.read())

newdata = []
nodes = []
for k,y in data.items():
    fixed = k.split('_')
    nodes.append(fixed[0])
    nodes.append(fixed[1])
    newdata.append((fixed[0], fixed[1], float(y)))

g = nx.DiGraph()
# g.add_node("USD")
# g.add_node("JPY")
# g.add_edge("USD","JPY", {"weight": 91.9943456})
# g = nx.cycle_graph(nodes, create_using=nx.DiGraph())
g.add_nodes_from(nodes)
g.add_weighted_edges_from(newdata)
options = {
    'node_color': 'yellow',
    'node_size': 330,
    'width': 1,
    'arrowstyle': '-|>',
    'arrowsize': 32,
    'with_labels': True,
    'font_size': 10
}
# pos = nx.circular_layout(g)
# nx.draw(g, with_labels=True, node_color='y')
layout = nx.circular_layout(g)
nx.draw_networkx_edge_labels(g, layout, label_pos=0.3)
nx.draw_networkx_nodes(g,layout, node_color='yellow', node_size=500)
nx.draw_networkx_edges(g, layout, edge_color='r', arrows = True, arrowstyle = '-|>', arrowsize = 20)
nx.draw_networkx_labels(g, layout, font_size=10, font_family="sans-serif")

# nx.draw_networkx(g, arrows=True, **options)

print(nx.negative_edge_cycle(g))
print(nx.single_source_bellman_ford_path(g, "USD"))
plt.show()