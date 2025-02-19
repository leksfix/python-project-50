from gendiff.compare import (
    DIFF_TYPE_ADD,
    DIFF_TYPE_CNG,
    DIFF_TYPE_DEL,
    DIFF_TYPE_UNC,
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


def format_val(val, lvl):
    if isinstance(val, dict):
        return format_complex_value(val, lvl)
    else:
        return format_simple_value(val)


def format_stylish(diff_list):
    """Returns diff result as string in 'stylish' format"""

    def format_stylish_int(diff_list, fmt_lst, lvl):
        indent = make_indent(lvl)[:-2]
        for i in diff_list:
            tp = i['type']
            name = i["name"]
            if 'children' in i:
                fmt_lst.append(f'{indent}  {name}: {{')
                format_stylish_int(i['children'], fmt_lst, lvl + 1)
                fmt_lst.append(f"{indent}  }}")
            else:
                val = format_val(i["value"], lvl)
                val = ' ' + val if val else ''
                if tp == DIFF_TYPE_ADD:
                    fmt_lst.append(f'{indent}+ {name}:{val}')
                elif tp == DIFF_TYPE_DEL:
                    fmt_lst.append(f'{indent}- {name}:{val}')
                elif tp == DIFF_TYPE_CNG:
                    val_old = format_val(i["value_old"], lvl)
                    val_old = ' ' + val_old if val_old else ''
                    fmt_lst.append(f'{indent}- {name}:{val_old}')
                    fmt_lst.append(f'{indent}+ {name}:{val}')
                elif tp == DIFF_TYPE_UNC:
                    fmt_lst.append(f'{indent}  {name}:{val}')

    lst = ['{']
    format_stylish_int(diff_list, lst, 1)
    lst.append('}')
    return '\n'.join(lst)

