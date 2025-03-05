def merge_lists_to_dict(keys, values):
    return dict(zip(keys, values))


keys = ['a', 'b', 'c']
values = [1, 2, 3]


result = merge_lists_to_dict(keys=keys, values=values)
print(result)

result2 = merge_lists_to_dict(['x', 'y'], values=[10, 20])
print(result2) 
