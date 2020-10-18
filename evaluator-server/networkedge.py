import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()
g.add_node("USD")
g.add_node("JPY")
g.add_edge("USD","JPY", weight = 91.9943456)
options = {
    'node_color': 'blue',
    'node_size': 30,
    'width': 3,
    'arrowstyle': '-|>',
    'arrowsize': 12,
    'with_labels': True,
    'font_size': 12
}
# pos = nx.circular_layout(g)
# nx.draw(g, with_labels=True, node_color='y')
layout = nx.spring_layout(g)
nx.draw_networkx_edge_labels(g, layout)
nx.draw_networkx_nodes(g,layout)
nx.draw_networkx_edges(g, layout, edge_color='r', arrows = True, arrowstyle = '-|>')
nx.draw_networkx_labels(g, layout, font_size=12, font_family="sans-serif")

# nx.draw_networkx(g, arrows=True, **options)
plt.show()