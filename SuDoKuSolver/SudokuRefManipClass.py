class SudokuRefListClass:
    defAllPossibleValues = '123456789'

    allPossList = []

    def __init__(self):
        self.allPossList = [self.defAllPossibleValues for i in range(100)]
        for i in range(0, 10):
            self.allPossList[i] = None
        for i in range(10, 100, 10):
            self.allPossList[i] = None

    def __str__(self):
        val = ''
        for row in range(10):
            if row == 0:
                val = val.join([('{0:12d}').format(x) for x in range(1,10)])
                val = val + '\n'
            if row > 0:
                val = val +('\n {} \t'.format(row))
            for col in range(10):
                x = self.allPossList[int(str(row)+str(col))]
                if x is not None:
                    val = val + ('{0:12s}').format(x)
        return val

    def remove_invalid_number_from_location(self, num, loc):
        """ To remove a non possible number from the possiblities."""
        f, s, t = self.allPossList[int(loc)].rpartition(str(num))
        self.allPossList[int(loc)] = f + t

    def generate_group_keys_for_key(self, k):
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

    def generate_row_keys_for_key(self, k):
        return [k[0] + str(i) for i in range(1, 10)]

    def generate_col_keys_for_key(self, k):
        return [str(i) + k[1] for i in range(1, 10)]

    def generate_positional_search_keys_list(self,pos):
        all_keys = []
        all_keys.extend(self.generate_col_keys_for_key(pos))
        all_keys.extend(self.generate_row_keys_for_key(pos))
        all_keys.extend(self.generate_group_keys_for_key(pos))
        return all_keys

    def apply_value_at_position(self,pos,val):
        [self.remove_invalid_number_from_location(val, e) for e in self.generate_positional_search_keys_list(pos)]
        print(self)

    def update_sudoku_with_event_value(self,e,v):
        for key, value in v.items():
            if value is None or value is '' :
                pass
            else:
                [self.remove_invalid_number_from_location(value, e) for e in self.generate_positional_search_keys_list(key)]
                self.allPossList[int(key)] = ''
        print(self)

if __name__ == '__main__':
    s = SudokuRefListClass()
    print(s)
    s.apply_value_at_position(3,'34')
    print(s)
    s.apply_value_at_position(6,'62')
    print(s)
    s.apply_value_at_position(9,'99')
    print("after")
    print(s)

