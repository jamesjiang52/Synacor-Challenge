if __name__ == '__main__':

    grid = [['*', '8', '-', '1'], ['4', '*', '11', '*'], ['+', '4', '-', '18'], ['0', '-', '9', '*']]

    initial = 22
    goal = 30

    seen = [[0, 3, initial, '', []]]

    for coordinates in seen:
        if coordinates[0] < 3:
            new_coordinates = [coordinates[0] + 1, coordinates[1], coordinates[2], coordinates[3], coordinates[4][:] + ['east']]
            if coordinates[3] != '':
                if coordinates[3] == '+':
                    new_coordinates[2] += int(grid[new_coordinates[1]][new_coordinates[0]])
                elif coordinates[3] == '-':
                    new_coordinates[2] -= int(grid[new_coordinates[1]][new_coordinates[0]])
                elif coordinates[3] == '*':
                    new_coordinates[2] *= int(grid[new_coordinates[1]][new_coordinates[0]])
                new_coordinates[3] = ''
            else:
                new_coordinates[3] = grid[new_coordinates[1]][new_coordinates[0]]
            if (new_coordinates[2] == goal) and (grid[new_coordinates[1]][new_coordinates[0]] == '1'):
                print(new_coordinates[4])
                break
            if new_coordinates[:2] != [3, 0]:
                seen.append(new_coordinates)

        if (coordinates[0] > 0) and (coordinates[1] != 3):
            new_coordinates = [coordinates[0] - 1, coordinates[1], coordinates[2], coordinates[3], coordinates[4][:] + ['west']]
            if coordinates[3] != '':
                if coordinates[3] == '+':
                    new_coordinates[2] += int(grid[new_coordinates[1]][new_coordinates[0]])
                elif coordinates[3] == '-':
                    new_coordinates[2] -= int(grid[new_coordinates[1]][new_coordinates[0]])
                elif coordinates[3] == '*':
                    new_coordinates[2] *= int(grid[new_coordinates[1]][new_coordinates[0]])
                new_coordinates[3] = ''
            else:
                new_coordinates[3] = grid[new_coordinates[1]][new_coordinates[0]]
            if (new_coordinates[2] == goal) and (grid[new_coordinates[1]][new_coordinates[0]] == '1'):
                print(new_coordinates[4])
                break
            if new_coordinates[:2] != [3, 0]:
                seen.append(new_coordinates)

        if (coordinates[1] < 3) and (coordinates[0] != 0):
            new_coordinates = [coordinates[0], coordinates[1] + 1, coordinates[2], coordinates[3], coordinates[4][:] + ['south']]
            if coordinates[3] != '':
                if coordinates[3] == '+':
                    new_coordinates[2] += int(grid[new_coordinates[1]][new_coordinates[0]])
                elif coordinates[3] == '-':
                    new_coordinates[2] -= int(grid[new_coordinates[1]][new_coordinates[0]])
                elif coordinates[3] == '*':
                    new_coordinates[2] *= int(grid[new_coordinates[1]][new_coordinates[0]])
                new_coordinates[3] = ''
            else:
                new_coordinates[3] = grid[new_coordinates[1]][new_coordinates[0]]
            if (new_coordinates[2] == goal) and (grid[new_coordinates[1]][new_coordinates[0]] == '1'):
                print(new_coordinates[4])
                break
            if new_coordinates[:2] != [3, 0]:
                seen.append(new_coordinates)

        if coordinates[1] > 0:
            new_coordinates = [coordinates[0], coordinates[1] - 1, coordinates[2], coordinates[3], coordinates[4][:] + ['north']]
            if coordinates[3] != '':
                if coordinates[3] == '+':
                    new_coordinates[2] += int(grid[new_coordinates[1]][new_coordinates[0]])
                elif coordinates[3] == '-':
                    new_coordinates[2] -= int(grid[new_coordinates[1]][new_coordinates[0]])
                elif coordinates[3] == '*':
                    new_coordinates[2] *= int(grid[new_coordinates[1]][new_coordinates[0]])
                new_coordinates[3] = ''
            else:
                new_coordinates[3] = grid[new_coordinates[1]][new_coordinates[0]]
            if (new_coordinates[2] == goal) and (grid[new_coordinates[1]][new_coordinates[0]] == '1'):
                print(new_coordinates[4])
                break
            if new_coordinates[:2] != [3, 0]:
                seen.append(new_coordinates)

