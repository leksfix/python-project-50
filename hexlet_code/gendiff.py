import json

DIFF_TYPE_ADD = 'A'
DIFF_TYPE_DEL = 'D'
DIFF_TYPE_EQ = 'E'
DIFF_TYPE_NEQ = 'U'


def parse_json(filename):
    return json.load(open(filename))


def get_diff(dict1, dict2):
    """Asume that input parameters are dicts"""
    added_keys = dict2.keys() - dict1.keys()
    added_list = list(filter(lambda x: x[0] in added_keys, dict2.items()))
    added_diff = list(
        map(lambda x: {'type': DIFF_TYPE_ADD, 'name': x[0], 'value': x[1]},
             added_list
        )
    )

    del_keys = dict1.keys() - dict2.keys()
    del_list = list(filter(lambda x: x[0] in del_keys, dict1.items()))
    del_diff = list(
        map(lambda x: {'type': DIFF_TYPE_DEL, 'name': x[0], 'value': x[1]}, 
            del_list
        )
    )

    same_keys = dict1.keys() & dict2.keys()
    same_diff = []
    for k in same_keys:
        v1 = dict1[k]
        v2 = dict2[k]
        if v1 == v2:
            same_diff.append({'type': DIFF_TYPE_EQ, 'name': k, 'value': v1})
        else:
            same_diff.append({'type': DIFF_TYPE_NEQ, 'name': k, 
                'value_old': v1, 'value': v2}
            )

    res = added_diff + del_diff + same_diff
    res.sort(key=lambda x: x['name'])
    return res


def format_stylish(diff):
    """Rerurns diff result as string in 'stylish' format"""

    def format_node(node, ds, lvl):
        ds.append(f"{' ' * 2 * lvl}{{")
        indent = ' ' * 2 * (lvl + 1)
        for i in node:
            tp = i['type']
            if tp == DIFF_TYPE_ADD:
                ds.append(f'{indent}+ {i["name"]}: {i["value"]}')
            elif tp == DIFF_TYPE_DEL:
                ds.append(f'{indent}- {i["name"]}: {i["value"]}')
            elif tp == DIFF_TYPE_NEQ:
                ds.append(f'{indent}- {i["name"]}: {i["value_old"]}')
                ds.append(f'{indent}+ {i["name"]}: {i["value"]}')
            else:
                ds.append(f'{indent}  {i["name"]}: {i["value"]}')
        ds.append(f"{' ' * 2 * lvl}}}")
    
    lst = []
    format_node(diff, lst, 0)
    return '\n'.join(lst)


def generate_diff(format, filename1, filename2):
    """Generates diff string using 'format' argument"""
    file1 = parse_json(filename1)
    file2 = parse_json(filename2)
    diff = get_diff(file1, file2)
    match format:
        case 'stylish':
            return format_stylish(diff)
        case _:
            return format_stylish(diff)

    
