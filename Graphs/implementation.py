def create_graph():
    graph = {}
    
    while True:
        print("Enter 'q' to quit.")
        source = input("Enter source node: ")
        
        if source == 'q':
            break
        
        destination = input("Enter destination node: ")
        
        if destination == 'q':
            break
        
        if source not in graph:
            graph[source] = []
        
        if destination not in graph:
            graph[destination] = []
        
        graph[source].append(destination)
        graph[destination].append(source)
    
    return graph

def display_graph(graph):
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

print("Create an undirected graph:")
my_graph = create_graph()
    
print("\nGraph:")
display_graph(my_graph)
