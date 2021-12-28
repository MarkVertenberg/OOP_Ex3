# Ex.3: Directed and Edge-Weighted Graphs
# introduction:
This task is dedicated to the design and implementation of data structures and algorithms on graphs (directed and weighted) in Python.

**Directed Graph:**

A directed graph is a graph, a set of objects (called vertices or nodes) that are connected together, where all the edges are directed from one **vertex*** to another. A directed graph is sometimes called a digraph or a directed network. A directed graph is a graph in which the edges have a direction. This is usually indicated with an arrow on the edge; more formally, if v and w are vertices, an edge is an unordered pair {v,w}, while a **directed edge***, called an arc, is an ordered pair (v,w) or (w,v). The arc (v,w) is drawn as an arrow from v to w. If a graph contains both arcs (v,w) and (w,v), this is not a "multiple edge'', as the arcs are distinct. It is possible to have multiple arcs, namely, an arc (v,w) may be included multiple times in the multiset of arcs. As before, a digraph is called simple if there are no loops or multiple arcs.

**Edge-Weighted Graphs:**

An edge-weighted graph is a graph in which each edge has been assigned a **weight***. Similarly, a vertex-weighted graph is a graph in which each vertex has been assigned a weight. In such graphs, the quantity represented by a weight depends on the application. In many applications, each edge of a graph has an associated numerical value, called a weight. Usually, the edge weights are nonnegative integers. Weighted graphs may be either directed or undirected. The weight of an edge is often referred to as the "cost" of the edge. In applications, the weight may be a measure of the length of a route, the capacity of a line, the energy required to move between locations along a route, etc.the combination of Directed Graphs and Edge-Weighted Graphs is called Edge-Weighted Digraphs.

______________________________________________________________________________________________________________________________________________________________________________
- **Vertex** – Is a node on a graph. 

- **Directed Edge** – Is a link between two vertices. Directed edge is always pointing the same way. It has a source and a destination. 

- **Weight** – Represents the cost of the edge.
______________________________________________________________________________________________________________________________________________________________________________
![](https://www.pngkit.com/png/detail/202-2024370_connections-png-nodes-png.png)

# Algorithm:

The function below receives "graph" object of the DiGraph type and initializes it within the graph of the algorithm:

    def __init__(self, graph=DiGraph()) -> None:
      self.graph = graph
      self.mc = 0
      self.list = [int]
    
_________________________________________________________________________________________________________________________________________________________________________________
The function below returns the graph(DiGraph type) of the algorithm:

     def get_graph(self):
         return self.graph
    
_________________________________________________________________________________________________________________________________________________________________________________
The function below Computes the length of the shortest path between src to dest:

    def shortest_path(self, id1: int, id2: int):
        try:
            return DIJKSTRA.shortest_path(self.graph, id1, id2)
        except ValueError as e:
            print(e)
        return float('inf'), []
    
_________________________________________________________________________________________________________________________________________________________________________________ 
The function below finds the NodeData which minimizes the max distance to all the other nodes. Assuming the graph isConnected, else return null:

    def centerPoint(self):
        min = float("inf")
        N = None
        for Node in self.graph.nodes:
          dis = self.farthest_neighbor_of_node(Node)
          if dis < min:
            min = dis
            N = Node
        return N, min
    
_________________________________________________________________________________________________________________________________________________________________________________ 
The function below computes a list of consecutive nodes which go over all the nodes in cities.
the sum of the weights of all the consecutive (pairs) of nodes (directed) is the "cost" of the solution - the lower the better:

    def TSP(self, node_lst: List[int]):
        sum = 0
        path = []
        if len(node_lst) > 0:
            path.append(node_lst[0])
            src = node_lst[0]
            for node in node_lst[1:]:
                algo = self.shortest_path(src, node)  # (dist, list(nodes))
                pa = algo[1]
                sum += algo[0]
                src = node
                for p in pa[1:]:
                    path.append(p)
        return path, sum
    
_________________________________________________________________________________________________________________________________________________________________________________
The function below saves this weighted (directed) graph to the given:

    def save_to_json(self, file_name: str):
        with open(str) as json_file:
            data = json.load(json_file)
            temp = data["Nodes"]
            for Node in self.graph.nodes.values():
                if Node is not None:
                    dist = f'{Node.pos[0]},{Node.pos[1]},{Node.pos[2]}'
                    e = {"id": Node.key, "pos": dist}
                    temp.append(e)
            temp1 = data["Edges"]
            for Edge in self.graph.edges:
                src = f'{Edge[0]}'
                dest = f'{Edge[1]}'
                w = f'{Edge[2]}'
                d = {"src": src, "dest": dest, "w": w}
                temp1.append(d)
        self.writejson(data, file_name)

        pass

    def writejson(data, file_name: str):
        with open(file_name, "w") as f:
            json.dump(data, f)

_________________________________________________________________________________________________________________________________________________________________________________ 
The function below loads a graph to this graph algorithm.if the file was successfully loaded - the underlying graph of this class will be changed (to the loaded one), in case the graph was not loaded the original graph should remain "as is":
    
     def load_from_json(self, file_name: str):
        try:
            with open(str) as f:
                obj = json.load(f)
                list = obj['Edges']
                for i in range(len(list)):
                    self.graph.add_edge(list[i].get("src"), list[i].get("w"), list.get("dest"))

                list1 = obj['Nodes']
                for i in range(len(list)):
                    self.graph.add_node(list1[i].get("id"), list1[i].get("pos"))

                    return True

        except:
            return False

 # UML:
![Untitled Diagram drawio (3)](https://user-images.githubusercontent.com/93255163/147592154-54adfe2f-5316-47ff-8d14-fc93b215339d.png)

# Report results:
**The results can be seen in the attached WIKI file.**
Link: https://github.com/MarkVertenberg/OOP_Ex3/wiki

# Helpful Links:

- OXFORD COLLEGE | Directed and Edge-Weighted Graphs: 
In this site you can find information about Directed and Edge-Weighted Graphs , and the best data structure for it.
    link:http://math.oxford.emory.edu/site/cs171/directedAndEdgeWeightedGraphs/

- Explanation of Dijkstra’s algorithm for finding the shortest path between one vertex in a graph and another.
This video helped us to implement our Dijkstra class.
    link:https://www.youtube.com/watch?v=pVfj6mxhdMw

- Explanation on performing Depth–first search (DFS) to check if A directed graph is strongly connected.
    link:https://www.techiedelight.com/check-given-graph-strongly-connected-not/

# Credits:
1. Mark vertenberg.
2. Mishell dubovitski.
3. Alina zakhozha.

