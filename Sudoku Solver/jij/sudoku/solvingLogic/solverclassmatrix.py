defAllPossibleValues = '123456789'

matrix = [[defAllPossibleValues for i in range(9)] for j in range(9)]


def remove_invalid_number_from_location(num, loc):
    """ To remove a non possible number from the possiblities."""
    x, y = int(loc[0]), int(loc[1])
    f, s, t = matrix[x][y].rpartition(str(num))
    matrix[x][y] = f + t


def remove_value_at_position(num, loc):
    x, y = int(loc[0]), int(loc[1])
    matrix[x][y] = ''


def pretty_print_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


def identify_least_sized_elems(m):
    pass
    # lens = [max(map(len, col)) for col in zip(*s)]


print(min(matrix[1], key=len))

s = [[str(e) for e in row] for row in matrix]
lens = [min(map(len, col)) for col in zip(*s)]
print(lens)


def generate_group_keys_for_key(key):
    grpKeyList = []
    for i in [0, 3, 6]:
        if i <= int(key[0]) < i + 3:
            cKeyX = int((i + i + 2) / 2)
        if i <= int(key[1]) < i + 3:
            cKeyY = int((i + i + 2) / 2)
    for k in [cKeyX - 1, cKeyX, cKeyX + 1]:
        for l in [cKeyY - 1, cKeyY, cKeyY + 1]:
            grpKeyList.append(str(k) + str(l))
    return grpKeyList


def generate_col_keys_for_key(k):
    colGrpKeysList = []
    for i in range(0, 9):
        colGrpKeysList.append(k[0] + str(i))
    return colGrpKeysList


def generate_row_keys_for_key(key):
    rowGrpKeysList = []
    for i in range(0, 9):
        rowGrpKeysList.append(str(i) + key[1])
    return rowGrpKeysList


def conv_to_zero_base(key):
    return str((int(key[0]) - 1)) + str(int(key[1]) - 1)


def conv_to_one_base(key):
    return str((int(key[0]) + 1)) + str(int(key[1]) + 1)


def apply_value_at_position(v, pos):
    conv_key = conv_to_zero_base(pos)
    [remove_invalid_number_from_location(v, e) for e in generate_col_keys_for_key(conv_key)]
    [remove_invalid_number_from_location(v, e) for e in generate_row_keys_for_key(conv_key)]
    [remove_invalid_number_from_location(v, e) for e in generate_group_keys_for_key(conv_key)]
    remove_value_at_position(v, conv_key)


key = '24'

apply_value_at_position(3, '45')
apply_value_at_position(6, '89')
apply_value_at_position(7, '11')
apply_value_at_position(1, '29')
pretty_print_matrix(matrix)
