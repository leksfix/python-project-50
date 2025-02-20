from gendiff.compare import (
    ADDED,
    CHANGED,
    DELETED,
    NESTED,
    UNCHANGED,
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
            if tp == NESTED:
                format_plain_int(i['value'], fmt_lst, name)
            else:
                val = to_str(i['value'])
                if tp == ADDED:
                    fmt_lst.append(
                        f"Property '{name}' was added with value: {val}"
                    )
                elif tp == DELETED:
                    fmt_lst.append(f"Property '{name}' was removed")
                elif tp == CHANGED:
                    val_old = to_str(i['value_old'])
                    fmt_lst.append(
                        f"Property '{name}' was updated. From {val_old} to {val}"  # noqa: E501
                    )
                elif tp == UNCHANGED:
                    pass

    lst = []
    format_plain_int(diffs, lst, '')
    return '\n'.join(lst)
