my_list = [123, 1000.0, (1, 2, 3),{'key' : 'value'},{'one,two,three'},
           frozenset('one,two,three'),False, None, 'string']
for i, item in enumerate(my_list, 1):
    print(f'{i}){item} - {type(item)}')
