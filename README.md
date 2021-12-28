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

# Algorithm:

The function below receives "graph" object of the DiGraph type and initializes it within the graph of the algorithm:

     def __init__(self, graph=DiGraph()) -> None:
        self.graph = graph
        self.mc = 0
    
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

        def farthest_node_from_src(self, src):
        max = 0
        dis = 0
        for Node in self.graph.vertices:
            dis = self.shortest_path(src, Node)[0]
            if dis > max:
                max = dis
        return max

    def centerPoint(self):
        min = float("inf")
        N = None
        for Node in self.graph.vertices:
            dis = self.farthest_node_from_src(Node)
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
        try:
            file = open(file_name, 'w')
            file.write(json.dumps(self.savefile()))
            file.close()
            return True
        except IOError:
            return False

    def savefile(self):
        tip = []
        for e in self.graph.Lines:
            src = e[0]
            dest = e[1]
            w = self.graph.Lines[e]
            tip.append({"src": src, "w": w, "dest": dest})
        List = {}
        List["Edges"] = tip
        ver = []
        for n in self.graph.vertices.values():
            if n.dist is not None:
                r = n.value
                x = n.dist[0]
                y = n.dist[1]
                z = n.dist[2]
                pos = f'{x},{y},{z}'
                ver.append({"id": r, "pos": pos})
            else:
                ver.append({"id": n.value, "pos": None})
        List["Nodes"] = ver
        return List

_________________________________________________________________________________________________________________________________________________________________________________ 
The function below loads a graph to this graph algorithm.if the file was successfully loaded - the underlying graph of this class will be changed (to the loaded one), in case the graph was not loaded the original graph should remain "as is":
    
    def load_from_json(self, file_name: str):
        file = file_name
        s = file[-4:]
        if s != "json":
            file_name = file_name+".json"
        try:
            self.graph = DiGraph()
            with open(file_name, "r") as a:
                obj = json.load(a)
                for n in obj["Nodes"]:
                    t = int(n["id"])
                    if "pos" in n:
                        m = n["pos"].split(',')
                        x = float(m[0])
                        y = float(m[1])
                        z = float(m[2])
                        self.graph.add_node(t,(x, y, z))
                    else:
                        self.graph.add_node(t)
                for e in obj["Edges"]:
                    src = int(e["src"])
                    dest = int(e["dest"])
                    w = float(e["w"])
                    self.graph.add_edge(src, dest, w)
        except IOError:
            return False

        return True

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

