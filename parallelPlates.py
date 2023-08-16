# Two parallel plates

x_coordinates = [
    [2, 2, 2, 2],
    [3.5, 3.7, 3.8, 4],
    [5.9, 5.95, 6, 6],
    [7.9, 7.95, 8, 7.96],
    [9.9, 9.85, 10, 9.95],
    [11, 11, 11, 11]
]

parallel_x_values = []
parallel_y_values = []

for coordinate in x_coordinates:
    y_coordinates = [2, 4, 6, 8]
    for coordx, coordy in zip(coordinate, y_coordinates):
        parallel_x_values.append(coordx)
        parallel_y_values.append(coordy)