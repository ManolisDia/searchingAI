maze = [
    [2, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 3]
]

def calculate_manhattan_distance(current_x, current_y, goal_x, goal_y):
    return abs(current_x - goal_x) + abs(current_y - goal_y)

# Goal node location
goal_x, goal_y = 4, 5

# Calculate Manhattan distance for each node
manhattan_distances = [[calculate_manhattan_distance(x, y, goal_x, goal_y) for y in range(len(maze[0]))] for x in range(len(maze))]


[[9, 8, 7, 6, 5, 4], 
 [8, 7, 6, 5, 4, 3], 
 [7, 6, 5, 4, 3, 2], 
 [6, 5, 4, 3, 2, 1], 
 [5, 4, 3, 2, 1, 0]]
