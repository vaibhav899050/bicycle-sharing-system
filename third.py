import numpy as np
import pandas as pd
import osmnx as ox
import networkx as nx
from itertools import combinations
import time

# Part 3 of question 1

filename = "bike_data_new.csv"
starting = time.time()

bike_data = pd.read_csv(filename)
unique1 = bike_data.iloc[:100]
unique = unique1.drop_duplicates(subset=['start_lat', 'start_lng'])

print("number of unique depots: ", len(unique))




latitudes = unique['start_lat']
longitudes = unique['start_lng']



G = ox.graph_from_point((latitudes[0], longitudes[0]), network_type='drive')

for lat, lon in zip(latitudes[1:], longitudes[1:]):
    G = ox.graph_from_point((lat, lon), network_type='drive')
# ox.plot_graph(G)

depot_nodes = {}


for i, row in unique.iterrows():
    name = row["trip_id"]
    lat = row['start_lat']
    lon = row['start_lng']
    point = (lat, lon)
    nearest_node = ox.distance.nearest_nodes(G, lon, lat)
    depot_nodes[name] = nearest_node

print(depot_nodes)

num_depots = len(unique)
distances = np.zeros((num_depots, num_depots))


for i in range(num_depots):
    for j in range(num_depots):
        if i != j:
            try:
                start_node = depot_nodes[unique.iloc[i]['trip_id']]
                end_node = depot_nodes[unique.iloc[j]["trip_id"]]
                shortest_path = nx.shortest_path_length(G, start_node, end_node, weight='length')
                distances[i, j] = shortest_path
            except nx.NetworkXNoPath:
                distances[i, j] = -1


distances = pd.DataFrame(distances)
# distances.to_csv('data.csv', index=False)
print("Shortest path distances between all depots:")
print(distances)
print("Maximum distance:", np.max(distances[distances > 0]))
print("Minimum distance:", np.min(distances[distances > 0]))
ending = time.time()
print("Time Tkae: ", ending-starting)















