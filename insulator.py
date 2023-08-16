# Two parallel plates with insulator in between

insulator_x_values = []
insulator_y_values = []

x_coordinates = [
    [2, 2, 2, 2],
    [4, 4.5, 4.7, 4.25],
    [6.1, 6.05, 6.2, 6.1],
    [7.8, 7.6, 7.7, 7.8],
    [9.8, 9.4, 9.5, 9.7],
    [11, 11, 11, 11]
]

for x_coords in x_coordinates:
    for x_coord in x_coords:
        insulator_x_values.append(x_coord)

y_coordinates = [
    [2, 4, 6, 8],
    [2, 4, 6, 8],
    [2, 3, 7, 8],
    [2, 3, 7, 8],
    [2, 4, 6, 8],
    [2, 4, 6, 8]
]

for y_coords in y_coordinates:
    for y_coord in y_coords:
        insulator_y_values.append(y_coord)