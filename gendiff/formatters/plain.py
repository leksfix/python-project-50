from gendiff.compare import (
    TYPE_ADDED,
    TYPE_CHANGED,
    TYPE_DELETED,
    TYPE_NESTED,
    TYPE_UNCHANGED,
)


def to_str(val):
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


def format_plain(diffs):
    """Returns diff result as string in 'plain' format"""

    def format_plain_int(diffs, fmt_lst, path):
        for i in diffs:
            tp = i['type']
            name = f"{path}.{i['name']}" if path else i['name']
            if tp == TYPE_NESTED:
                format_plain_int(i['value'], fmt_lst, name)
            else:
                val = to_str(i['value'])
                if tp == TYPE_ADDED:
                    fmt_lst.append(
                        f"Property '{name}' was added with value: {val}"
                    )
                elif tp == TYPE_DELETED:
                    fmt_lst.append(f"Property '{name}' was removed")
                elif tp == TYPE_CHANGED:
                    val_old = to_str(i['value_old'])
                    fmt_lst.append(
                        f"Property '{name}' was updated. \
From {val_old} to {val}"
                    )
                elif tp == TYPE_UNCHANGED:
                    pass

    lst = []
    format_plain_int(diffs, lst, '')
    return '\n'.join(lst)
