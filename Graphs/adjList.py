def create_adjacency_list():
    adjacency_list = {}
    
    while True:
        print("Enter 'q' to quit.")
        source = input("Enter source node: ")
        
        if source == 'q':
            break
        
        destination = input("Enter destination node: ")
        
        if destination == 'q':
            break
        
        if source not in adjacency_list:
            adjacency_list[source] = []
        
        if destination not in adjacency_list:
            adjacency_list[destination] = []
        
        adjacency_list[source].append(destination)
        adjacency_list[destination].append(source)
    
    return adjacency_list

def display_adjacency_list(adjacency_list):
    for node, neighbors in adjacency_list.items():
        print(f"{node}: {neighbors}")

print("Create an undirected graph:")
my_adjacency_list = create_adjacency_list()
    
print("\nAdjacency List:")
display_adjacency_list(my_adjacency_list)
