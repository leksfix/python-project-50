from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish

__all__ = (
    'get_formatter',
)


def get_formatter(format):
    match format:
        case 'stylish':
            return format_stylish
        case 'plain':
            return format_plain
        case 'json':
            return format_json
        case _:
            raise Exception("Unknown format")