def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """

    # варианты ходов
    move_row = [2, 1, -1, -2, -2, -1, 1, 2]
    move_col = [1, 2, 2, 1, -1, -2, -2, -1]
    count = 0
    for i in range(8):

        starting_x = 0
        starting_y = 0
        new_x = starting_x + move_row[i]
        new_y = starting_y + move_col[i]

        condition_1 = new_x >= 0 and new_y >= 0
        condition_2 = new_x <= point[0] and new_y <= point[1]
        if condition_1 and condition_2:
            count += 1

    return count

