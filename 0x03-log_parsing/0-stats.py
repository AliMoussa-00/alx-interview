#!/usr/bin/python3
'''Log parsing'''

import re
import signal
from sys import stdin
import sys
from typing import Dict, List


def calculate_stats(i: int, total_size: List, codes: Dict[str, int]) -> int:
    line_pattern = re.compile(
        r"(\d{1,4})\.(\d{1,4})\.(\d{1,4})\.(\d{1,4}) "
        r"\- \[(\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}\:\d{2}\.\d+)\] "
        r"\"GET \/projects\/260 HTTP\/1\.1\" (\d{3}) (\d+)")

    for line in stdin:
        match = line_pattern.match(line)

        if match:

            status_code = match.groups()[-2]
            file_size = int(match.groups()[-1])

            if status_code in codes.keys():
                codes[status_code] = codes[status_code] + 1

            total_size[0] = total_size[0] + file_size

        if i == 10:
            return
        i += 1


def print_stats(total_size: List, codes: Dict[str, int]) -> None:
    print('File size: {}'.format(total_size[0]))

    for code, value in codes.items():
        if value != 0:
            print('{}: {}'.format(code, value))


# I used 'list' instead of 'int' because int are immutable
total_size = [0]
codes: Dict[str, int] = {'200': 0, '301': 0, '400': 0, '401': 0,
                         '403': 0, '404': 0, '405': 0, '500': 0}

try:
    while True:
        i = 1

        calculate_stats(i, total_size, codes)

        print_stats(total_size, codes)

except KeyboardInterrupt:
    pass

finally:
    print_stats(total_size, codes)
