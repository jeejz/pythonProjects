class SudokuRefListClass:
    defAllPossibleValues = '123456789'

    allPossList = []

    def __init__(self):
        self.allPossList = [self.defAllPossibleValues for i in range(100)]
        for i in range(0, 10):
            self.allPossList[i] = None
        for i in range(10, 100, 10):
            self.allPossList[i] = None

    def print_matrix(self):
        for i in range(len(self.allPossList)):
            print(self.allPossList[i], end='\t')
            if i % 10 == 0:
                print("")

    def remove_invalid_number_from_location(self, num, loc):
        """ To remove a non possible number from the possiblities."""
        f, s, t = self.allPossList[int(loc)].rpartition(str(num))
        self.allPossList[int(loc)] = f + t

    def generate_group_keys_for_key(k):
        group_keys = []
        for i in [1, 4, 7]:
            if i <= int(k[0]) < i + 3:
                kx = int((i + i + 2) / 2)
            if i <= int(k[1]) < i + 3:
                ky = int((i + i + 2) / 2)
        for k in [kx - 1, kx, kx + 1]:
            for l in [ky - 1, ky, ky + 1]:
                group_keys.append(str(k) + str(l))
        return group_keys

    def generate_row_keys_for_key(k):
        return [k[0] + str(i) for i in range(1, 10)]

    def generate_col_keys_for_key(k):
        return [str(i) + k[0] for i in range(1, 10)]

    def apply_value_at_position(self,v,pos):
        [self.remove_invalid_number_from_location(v, e) for e in SudokuRefListClass.generate_col_keys_for_key(pos)]
        [self.remove_invalid_number_from_location(v, e) for e in SudokuRefListClass.generate_row_keys_for_key(pos)]
        [self.remove_invalid_number_from_location(v, e) for e in SudokuRefListClass.generate_group_keys_for_key(pos)]
        self.allPossList[int(pos)] = ''

s = SudokuRefListClass()


s.print_matrix()
s.apply_value_at_position(3,'34')
s.apply_value_at_position(6,'62')
s.apply_value_at_position(9,'99')
print("after")
s.print_matrix()

