from gendiff.compare import (
    DIFF_TYPE_ADD,
    DIFF_TYPE_CNG,
    DIFF_TYPE_DEL,
    DIFF_TYPE_UNC,
)


def format_val(val):
    if val is None:
        return 'null'
    elif isinstance(val, dict):
        return '[complex value]'
    elif isinstance(val, bool):
        return str(val).lower()
    elif isinstance(val, str):
        return f"'{val}'"
    else:
        return str(val)


def format_plain(diff_list):
    """Returns diff result as string in 'plain' format"""

    def format_plain_int(diff_list, fmt_lst, path):
        for i in diff_list:
            tp = i['type']
            name = f"{path}.{i['name']}" if path else i['name']
            if 'children' in i:
                format_plain_int(i['children'], fmt_lst, name)
            else:
                val = format_val(i['value'])
                if tp == DIFF_TYPE_ADD:
                    fmt_lst.append(
                        f"Property '{name}' was added with value: {val}"
                    )
                elif tp == DIFF_TYPE_DEL:
                    fmt_lst.append(f"Property '{name}' was removed")
                elif tp == DIFF_TYPE_CNG:
                    val_old = format_val(i['value_old'])
                    fmt_lst.append(
                        f"Property '{name}' was updated. \
From {val_old} to {val}"
                    )
                elif tp == DIFF_TYPE_UNC:
                    pass

    lst = []
    format_plain_int(diff_list, lst, '')
    return '\n'.join(lst)
