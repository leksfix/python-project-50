
import copy
import json


def format_val(diff):
    res = copy.deepcopy(diff)
    del res['name']
    return res


def format_json(diff_list):
    
    def format_json_int(diff_list, out):
        for diff in diff_list:
            if 'children' in diff:
                children = {}
                format_json_int(diff['children'], children)
                out[diff['name']] = children
            else:
                out[diff['name']] = format_val(diff)
    
    out = {}
    format_json_int(diff_list, out)
    return json.dumps(out)