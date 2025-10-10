# Alpha-Beta Pruning Algorithm
def alpha_beta(node, depth, alpha, beta, maximizingPlayer, game_tree, values):
    # Base condition: leaf node or depth limit reached
    if depth == 0 or node not in game_tree:
        return values[node]
    
    # If current player is MAX
    if maximizingPlayer:
        value = float('-inf')
        for child in game_tree[node]:
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False, game_tree, values))
            alpha = max(alpha, value)
            if beta <= alpha:
                print(f"Beta cut-off at node {node}")
                break  # β cut-off
        return value
    
    # If current player is MIN
    else:
        value = float('inf')
        for child in game_tree[node]:
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True, game_tree, values))
            beta = min(beta, value)
            if beta <= alpha:
                print(f"Alpha cut-off at node {node}")
                break  # α cut-off
        return value


# ----------------------------
# Example Game Tree
# ----------------------------
game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

# Heuristic values for leaf nodes
values = {
    'D': 3,
    'E': 5,
    'F': 6,
    'G': 9
}

# Run Alpha-Beta Pruning
print("Alpha-Beta Pruning Result:\n")
best_value = alpha_beta('A', 3, float('-inf'), float('inf'), True, game_tree, values)
print("\nOptimal Value (Best Score):", best_value)

