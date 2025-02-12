from gendiff.compare import (
    DIFF_TYPE_ADD,
    DIFF_TYPE_CNG,
    DIFF_TYPE_DEL,
    DIFF_TYPE_UNC,
)


def format_val(val):
    if isinstance(val, bool):
        return str(val).lower()
    else:
        return str(val)
    

def format_stylish(diff):
    """Returns diff result as string in 'stylish' format"""

    def format_node(node, ds, lvl):
        ds.append(f"{' ' * 2 * lvl}{{")
        indent = ' ' * 2 * (lvl + 1)
        for i in node:
            tp = i['type']
            name = i["name"]
            val = format_val(i["value"])
            val_old = format_val(i.get("value_old", "?"))
            if tp == DIFF_TYPE_ADD:
                ds.append(f'{indent}+ {name}: {val}')
            elif tp == DIFF_TYPE_DEL:
                ds.append(f'{indent}- {name}: {val}')
            elif tp == DIFF_TYPE_CNG:
                ds.append(f'{indent}- {name}: {val_old}')
                ds.append(f'{indent}+ {name}: {val}')
            elif tp == DIFF_TYPE_UNC:
                ds.append(f'{indent}  {name}: {val}')
            else:
                ds.append('?')
        ds.append(f"{' ' * 2 * lvl}}}")
    
    lst = []
    format_node(diff, lst, 0)
    return '\n'.join(lst)

