DIFF_TYPE_ADD = 'added'
DIFF_TYPE_DEL = 'deleted'
DIFF_TYPE_CNG = 'changed'
DIFF_TYPE_UNC = 'unchanged'


def get_diff(dict1, dict2):
    """Assume that input parameters are dicts"""
    res = []
    for k in dict2.keys() | dict1.keys():
        if not k in dict1.keys():
            res.append({'type': DIFF_TYPE_ADD, 'name': k, 'value': dict2[k]})
        elif not k in dict2.keys():
            res.append({'type': DIFF_TYPE_DEL, 'name': k, 'value': dict1[k]})
        elif dict1[k] == dict2[k]:
            res.append({'type': DIFF_TYPE_UNC, 'name': k, 'value': dict1[k]})
        else:
            res.append({'type': DIFF_TYPE_CNG, 'name': k, 'value': dict2[k],
                        'value_old': dict1[k]})
    
    res.sort(key=lambda x: x['name'])
    return res
