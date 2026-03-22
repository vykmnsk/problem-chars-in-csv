from os import listdir
from os.path import isfile, join

CSV_DIR = 'data/'
ENCODING = 'utf-16le'
FIELD_DELIMITER = '||'

fnames = [f for f in listdir(CSV_DIR) if isfile(join(CSV_DIR, f))]
print('Checking files:', CSV_DIR, fnames)


for fname in fnames:
    found_chars = 0

    with open(join(CSV_DIR, fname), 'r', encoding=ENCODING) as f:
        print('----------------------------------')
        print(f'reading {fname}...')
        header = line = f.readline()
        expect_columns = header.split(FIELD_DELIMITER)
        expect_columns_cnt = len(expect_columns)
        print("Expecting columns:", expect_columns_cnt, expect_columns)

        bad_lines_cnt = 0
        while line:
            line = f.readline()
            if not line:
                continue
            line_columns = line.split(FIELD_DELIMITER)
            line_columns_cnt = len(line_columns)
            if expect_columns_cnt != line_columns_cnt:
                print('Unexpected columns count=', line_columns_cnt)
                print('line: ', line)
                bad_lines_cnt += 1

        print(fname, 'found bad lines=', bad_lines_cnt)
