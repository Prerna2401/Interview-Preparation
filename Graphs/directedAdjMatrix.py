def create_adjacency_matrix(num_nodes):
    matrix = [[0] * num_nodes for _ in range(num_nodes)]
    
    while True:
        print("Enter 'q' to quit.")
        source = input("Enter source node: ")
        
        if source == 'q':
            break
        
        destination = input("Enter destination node: ")
        
        if destination == 'q':
            break
        
        source = int(source) - 1
        destination = int(destination) - 1
        
        matrix[source][destination] = 1
    
    return matrix

def display_adjacency_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
        
num_nodes = int(input("Enter the number of nodes: "))
print("Create a directed graph:")
adjacency_matrix = create_adjacency_matrix(num_nodes)
    
print("\nAdjacency Matrix:")
display_adjacency_matrix(adjacency_matrix)
