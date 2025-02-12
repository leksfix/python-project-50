DIFF_TYPE_ADD = 'added'
DIFF_TYPE_DEL = 'deleted'
DIFF_TYPE_CNG = 'changed'
DIFF_TYPE_UNC = 'unchanged'


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
            same_diff.append({'type': DIFF_TYPE_UNC, 'name': k, 'value': v1})
        else:
            same_diff.append({'type': DIFF_TYPE_CNG, 'name': k, 
                'value_old': v1, 'value': v2}
            )

    res = added_diff + del_diff + same_diff
    res.sort(key=lambda x: x['name'])
    return res