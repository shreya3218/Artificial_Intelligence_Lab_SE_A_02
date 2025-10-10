def minimax(node, depth, player, game_tree, values):
    # Base condition: If depth is 0 or node has no children
    if depth == 0 or node not in game_tree:
        return values[node]

    # MAX player's turn
    if player == "MAX":
        alpha = float('-inf')  # Initialize to negative infinity
        for child in game_tree[node]:
            value = minimax(child, depth - 1, "MIN", game_tree, values)
            alpha = max(alpha, value)
        return alpha

    # MIN player's turn
    else:
        alpha = float('inf')  # Initialize to positive infinity
        for child in game_tree[node]:
            value = minimax(child, depth - 1, "MAX", game_tree, values)
            alpha = min(alpha, value)
        return alpha


# Example Usage:
# Define the game tree as a dictionary
game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

# Define the values of leaf nodes
values = {
    'D': 3,
    'E': 5,
    'F': 6,
    'G': 9
}

# Call minimax on the root node 'A'
result = minimax('A', 3, 'MAX', game_tree, values)
print("The optimal value is:", result)

