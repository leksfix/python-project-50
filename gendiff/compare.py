TYPE_ADDED = 'added'
TYPE_DELETED = 'deleted'
TYPE_CHANGED = 'changed'
TYPE_UNCHANGED = 'unchanged'
TYPE_NESTED = 'nested'


def get_diffs(dict1, dict2):
    """Assume that input parameters are dicts"""
    res = []
    for k in dict2.keys() | dict1.keys():
        if k not in dict1.keys():
            diff = {'type': TYPE_ADDED, 'name': k, 'value': dict2[k]}
        elif k not in dict2.keys():
            diff = {'type': TYPE_DELETED, 'name': k, 'value': dict1[k]}
        elif isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
            children = get_diffs(dict1[k], dict2[k])
            diff = {'type': TYPE_NESTED, 'name': k, 'value': children}
        elif dict1[k] == dict2[k]:
            diff = {'type': TYPE_UNCHANGED, 'name': k, 'value': dict1[k]}
        else:
            diff = {'type': TYPE_CHANGED, 'name': k,
                    'value': dict2[k], 'value_old': dict1[k]}
        res.append(diff)
    res.sort(key=lambda x: x['name'])
    return res
