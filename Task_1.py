my_list = [123, 1000.0, (5 + 5j), 'simply string', [1, 2, 3, ], (4, 5, 6),
           {'key': 'value'}, {'one,two,three'}, frozenset('one,two,three'),
           b'1, 2, 3',bytearray(b'1,2,3'), False, None]
for i, item in enumerate(my_list, 1):
    print(f'{i}){item} - {type(item)}')
