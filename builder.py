from typing import Optional, Callable

import functions

CMD_TO_FUNCTION: dict[str, Callable] = {
    'filter': functions.filter_query,
    'map': functions.map_query,
    'unique': functions.unique_query,
    'sort': functions.sort_query,
    'limit': functions.limit_query,
    'regex': functions.regex_query,

}
FILE = 'data/apache_logs.txt'


def build_query(cmd: str, param: str, data: Optional[list[str]]) -> list[str]:
    if data is None:
        with open(FILE, 'r') as f:
            prepared_data: list[str] = list(map(lambda x: x.strip(), f))
    else:
        prepared_data = data

    return CMD_TO_FUNCTION[cmd](param=param, data=prepared_data)
