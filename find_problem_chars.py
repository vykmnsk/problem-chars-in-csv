from os import listdir
from os.path import isfile, join
# import re

CSV_DIR = 'data'
ENCODING = 'utf-16'

fnames = [f for f in listdir(CSV_DIR) if isfile(join(CSV_DIR, f))]
print('Checking files:', CSV_DIR, fnames)


def is_problem_char(char):
    is_ctrl_char = ord(char) < 32
    is_ext_ctrl_char = ord(char) > 8200 and ord(char) < 9000
    result = is_ctrl_char or is_ext_ctrl_char
    return result

# def check_via_regex(line):
    # found = re.search("^[\\x00-\\x1F\\x7F]$", line)
    # found = re.match(r'[\x00-\x1f\x7f-\x9f]', line)
    # found = re.search(r'[\x00-\x1f\x7f-\x9f]', line)
    # found = re.search(r'[\W]', line)
    # ctrl_chars = re.findall(r'[\x00-\x1f\x7f-\x9f]', line[0:-1])
    # ctrl_chars = re.findall(r'[\W]', line[0:-1])


found_stats: dict[int, int] = {}

for fname in fnames:
    found_chars = 0

    with open(join(CSV_DIR, fname), 'r', encoding=ENCODING) as f:
        print('----------------------------------')
        print(f'reading {fname}...')
        header = line = f.readline()
        # print(header)

        # for _ in range(1000):
        while line:
            line = f.readline()

            ctrl_chars = [ord(ch) for ch in line[0:-1] if is_problem_char(ch)]
            for ch in line[0:-1]:
                line_ctrl_chars = []
                if is_problem_char(ch):
                    line_ctrl_chars.append(f'{ord(ch)}: {ch}')
                    ch_code = ord(ch)
                    found_chars += 1
                    found_stats[ch_code] = found_stats.get(ch_code, 0) + 1

                if len(line_ctrl_chars) > 0:
                    print(f'found {line_ctrl_chars}:: {line}')

        print(f'{fname} - found chars: ', found_chars)


print('done! found stats:')
rows = (f'{k}: {v}' for k, v in found_stats.items())
# rows.sort()
for row in sorted(rows):
    print(row)
