DIFF_TYPE_ADD = 'added'
DIFF_TYPE_DEL = 'deleted'
DIFF_TYPE_CNG = 'changed'
DIFF_TYPE_UNC = 'unchanged'


def get_diffs(dict1, dict2):
    """Assume that input parameters are dicts"""
    res = []
    for k in dict2.keys() | dict1.keys():
        if k not in dict1.keys():
            diff = {'type': DIFF_TYPE_ADD, 'name': k, 'value': dict2[k]}
        elif k not in dict2.keys():
            diff = {'type': DIFF_TYPE_DEL, 'name': k, 'value': dict1[k]}
        else:
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                children = get_diffs(dict1[k], dict2[k])
                diff = {'type': DIFF_TYPE_UNC, 'name': k, 'children': children}
            else:
                if dict1[k] == dict2[k]:
                    diff = {'type': DIFF_TYPE_UNC, 'name': k,
                            'value': dict1[k]}
                else:
                    diff = {'type': DIFF_TYPE_CNG, 'name': k,
                            'value': dict2[k], 'value_old': dict1[k]}
        res.append(diff)
    res.sort(key=lambda x: x['name'])
    return res
