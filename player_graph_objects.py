#Graph --> Nodes, Edges

#Players --> Start, end, route

#Creates a graph object

import math

'''
1. Instead of having a function to create an edge, we have classes to define edges as individual objects (DONE)
2. Route should be edges, not nodes (DONE)
3. Incorporate Djikstra's algorithm into the player class
4. Players + congestion (DONE)
'''

class Edge:
    def __init__(self, start_node, end_node, weight_fun, congestion):
        self.start_node = start_node
        self.end_node = end_node
        self.weight_fun = weight_fun
        self.congestion = congestion
        self.weight = weight_fun(congestion)

    def add_congestion(self, congestion):
        self.congestion = self.congestion + congestion
        self.weight = self.weight_fun(congestion)

#    add_congestion
#    change_weight
#
#    def modify(self,player)
#    for edge in player.route:
#       edge.add_congestion(+1)


class Graph:
    def __init__(self, edges_set):
        self.edges_set = edges_set
        self.node_set = []
        for i in edges_set:
            if (i.start_node not in self.node_set):
                self.node_set.append(i.start_node)
            if (i.end_node not in self.node_set):
                self.node_set.append(i.end_node)

#Connects nodes with an edge
    def connect_nodes(self, edge):
        if (edge not in self.edges_set and edge.start_node in self.node_set and edge.end_node in self.node_set):
            self.edges_set.append(edge)

#Adds a node to the graph
    def add_nodes(self, node):
        if (node not in self.node_set):
            self.node_set.append(node)

#Removes nodes from the graph. If a node is removed, all edges connected to that node are removed as well

    def remove_nodes(self, node):
        if (node in self.node_set):
            del self.node_set[self.node_set.index(node)]
            new = []
            for i in range (0, len(self.edges_set)):
                if (node != self.edges_set[i].start_node and node != self.edges_set[i].end_node):
                    new.append(self.edges_set[i])
            self.edges_set = new

#Disconnects nodes, thereby removing an edge
    def disconnect_nodes(self, edge):
        if (edge in self.edges_set):
            del self.edges_set[self.edges_set.index(edge)]

    def add_player_congestion(self, player):
        for i in player.route:
            self.edges_set[self.edges_set.index(i)].add_congestion(1)



'''
#Checks if the graph is completely connected (no disjoint sections of the graph)
    def check_connectivity(self):
        counter = 0
        branching_values = [self.node_set[0]]
        for value in self.edges_set:
            if (value[0] in branching_values and value[1] not in branching_values):
                branching_values.append(value[1])
        if (len(branching_values) == len(self.node_set)):
            return True
        else:
            return False
'''

'''
Algorithm to check connectivity:
1. Choose an arbitrary node x of the graph G as the starting pointself.
2. Determine the set A of all nodes which can be reached from x.
3. If A is equal to the set of all nodes of G, the graph is connected; otherwise it is disconnected.
'''

#Defines a player object

class Player:
# Route should be the list of edges, not nodes
    #def __init__(self, route, graph): #Route includes a start point and an end point, therefore there is no need to define these
    def __init__(self, graph, route):
        self.route = route
        #Returns list containing the nodes that comprise the shortest path
#       for playtesting - tell the route
        self.graph = [graph.node_set, graph.edges_set]

    #Changes the route of a player

    def change_route(self, route):
        self.change_route = route

#Checks if the route that the player is taking is a subgraph of the larger, previously defined graph network

    def check_legal_route(self):
        for i in range(0, len(self.route)-1):
            if (self.route[i].start_node in self.graph[0] and self.route[i].end_node in self.graph[0]):
                return True
            else:
                return False



    def dijkstra(self, start_node, end_node):

        one = []
        two = []

        least_path_nodes = [start_node]

        all_nodes = self.graph[0]

        removed_nodes = [start_node]

        all = []

        distances = []
        distances.append(0)
        for k in range(0, len(all_nodes)-1):
            distances.append(math.inf)

        #Update the distance parameters
        while (end_node not in removed_nodes):
            pathfinder = []

            for g in removed_nodes:
                for i in range(0, len(self.graph[1])):
                    if (self.graph[1][i].start_node == g):
                        pathfinder.append(self.graph[1][i].start_node)
                    if (self.graph[1][i].start_node == g and self.graph[1][i].end_node not in removed_nodes):
                        new_distance = self.graph[1][i].weight
                        if (new_distance < distances[all_nodes.index(self.graph[1][i].end_node)]):
                            distances[all_nodes.index(self.graph[1][i].end_node)] = distances[all_nodes.index(g)]+new_distance

        #Remove the lowest distance from the graph
            minimum = math.inf
            holder = []
            for h in all_nodes:
                if (h not in removed_nodes and distances[all_nodes.index(h)] < minimum):
                    minimum = distances[all_nodes.index(h)]
                    holder = h
            removed_nodes.append(holder)
            #print(pathfinder[all_nodes.index(holder)])
            one.append(pathfinder[removed_nodes.index(holder)])
            two.append(holder)

        path = [end_node]
        v = end_node
        while (v != start_node):
            temp = []
            path.append(one[two.index(v)])
            if (one[two.index(v)] == start_node):
                break
            path.append(two[two.index(one[two.index(v)])])
            v = two[two.index(one[two.index(v)])]
        path.reverse()


        return path

'''
e = [Edge(1, 2, lambda x: x, 0), Edge(2, 3, lambda x: x, 0), Edge(3, 4, lambda x: x, 0), Edge(1, 3, lambda x: x, 0), Edge(1, 3, lambda x: 0, 0)]
g = Graph(e)
p = Player(g, e)
g.add_player_congestion(p)
print(p.dijkstra(1, 4))
'''



#W = weights
#V = vertices
#E = edges
#G = Graph.make

# players = []
#number of players = N
#for i = 1:N:
#   start = 0
#   end = 1
#   new_player = Player(start,end,graph)
#   players.append(new_player)
#   graph.modify(new_player)
