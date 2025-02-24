from gendiff.compare import (
    ADDED,
    CHANGED,
    DELETED,
    NESTED,
    UNCHANGED,
)


def make_indent(lvl):
    return ' ' * 4 * lvl


def format_simple_value(val):
    if val is None:
        return 'null'
    if isinstance(val, bool):
        return str(val).lower()
    return str(val)


def format_complex_value(val, lvl):
    
    def format_complex_value_int(lst, val, lvl):
        indent = make_indent(lvl)
        for k, v in val.items():
            if isinstance(v, dict):
                lst.append(f'{indent}{k}: {{')
                format_complex_value_int(lst, v, lvl + 1)
                lst.append(f'{indent}}}')
            else:
                lst.append(f'{indent}{k}: {format_simple_value(v)}')

    lst = ['{']
    format_complex_value_int(lst, val, lvl + 1)
    indent = make_indent(lvl)
    lst.append(f'{indent}}}')
    return '\n'.join(lst)


def to_str(val, lvl):
    if isinstance(val, dict):
        return format_complex_value(val, lvl)
    else:
        return format_simple_value(val)


def format_stylish(diffs):
    """Returns diff result as string in 'stylish' format"""

    def format_stylish_int(diffs, fmt_lst, lvl):
        indent = make_indent(lvl)[:-2]
        for i in diffs:
            tp = i['type']
            name = i["name"]
            if tp == NESTED:
                fmt_lst.append(f'{indent}  {name}: {{')
                format_stylish_int(i['value'], fmt_lst, lvl + 1)
                fmt_lst.append(f"{indent}  }}")
            else:
                val = to_str(i["value"], lvl)
                if tp == ADDED:
                    fmt_lst.append(f'{indent}+ {name}: {val}')
                elif tp == DELETED:
                    fmt_lst.append(f'{indent}- {name}: {val}')
                elif tp == CHANGED:
                    val_old = to_str(i["value_old"], lvl)
                    fmt_lst.append(f'{indent}- {name}: {val_old}')
                    fmt_lst.append(f'{indent}+ {name}: {val}')
                elif tp == UNCHANGED:
                    fmt_lst.append(f'{indent}  {name}: {val}')

    lst = ['{']
    format_stylish_int(diffs, lst, 1)
    lst.append('}')
    return '\n'.join(lst)

