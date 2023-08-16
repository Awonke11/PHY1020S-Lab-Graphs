# One plate and one circular ring

circular_x_values = []
circular_y_values = []

x_coordinates = [
    [2, 2, 2, 2],
    [4.3, 4.35, 4.4, 4.5],
    [6.75, 6.7, 6.6, 6.8],
    [9.3, 8.6, 8.55, 9.1],
    [12, 10.2, 10.2, 11],
    [12, 11.5, 11, 12],
]

for x_coords in x_coordinates:
    for x_coord in x_coords:
        circular_x_values.append(x_coord)

y_coordinates = [
    [2, 4, 6, 8],
    [2, 4, 6, 8],
    [2, 4, 6, 8],
    [2, 4, 6, 8],
    [3, 4, 6, 7],
    [5, 6, 4, 6],
]

for y_coords in y_coordinates:
    for y_coord in y_coords:
        circular_y_values.append(y_coord)