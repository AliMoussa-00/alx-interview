#!/usr/bin/python3
'''Log parsing'''

import re
from sys import stdin


def print_stats(total_size, codes):
    '''printing the stats'''
    print('File size: {:d}'.format(total_size), flush=True)

    for code, value in sorted(codes.items()):
        if value != 0:
            print('{:s}: {:d}'.format(code, value), flush=True)


def main():
    '''the main function'''

    i = 0
    total_size = 0
    codes = {'200': 0, '301': 0, '400': 0, '401': 0,
             '403': 0, '404': 0, '405': 0, '500': 0}

    line_pattern = re.compile(
        r"(\d{1,4})\.(\d{1,4})\.(\d{1,4})\.(\d{1,4}) "
        r"\- \[(\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}\:\d{2}\.\d+)\] "
        r"\"GET \/projects\/260 HTTP\/1\.1\" (\d{3}) (\d+)")

    try:

        for line in stdin:

            match = line_pattern.match(line)

            if match:

                status_code = match.groups()[-2]
                file_size = int(match.groups()[-1])

                if status_code in codes.keys():
                    codes[status_code] += 1

                total_size += file_size

                i += 1
            if i == 10:
                i = 0
                print_stats(total_size, codes)

    except Exception:
        pass

    finally:
        print_stats(total_size, codes)
        return


if __name__ == '__main__':
    main()
