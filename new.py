import osmnx as ox
import networkx as nx

source = ox.geocode("Times Square, New York City, NY")
destination = ox.geocode("Central Park, New York City, NY")

G = ox.graph_from_address("New York City, NY", network_type="drive")

source_node = ox.distance.nearest_nodes(G, source[1], source[0])
destination_node = ox.distance.nearest_nodes(G, destination[1], destination[0])

route = nx.shortest_path(G, source_node, destination_node, weight="length")
print(G)

fig, ax = ox.plot_graph_route(G, route, route_linewidth=6, node_size=0)