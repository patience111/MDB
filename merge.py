#!/usr/bin/env python
import xlrd, glob, sys, csv

for globs, output_path in [
        ('download/H*.xls', "A.csv"),
        ('download/B*.xls', "B.csv"),
        ('download/C*.xls', "C.csv"),
        ]:
    first_line = False
    outputs = []
    lines = 0
    with open(output_path, "w") as f:
        writer = csv.writer(f)
        for path in glob.glob(globs):
            with xlrd.open_workbook(path) as s:
                sheet1 = s.sheet_by_index(0)
                for row in range(sheet1.nrows):
                    if row == 0 and first_line:
                        continue
                    else:
                        first_line = True
                    line = []
                    for col in range(sheet1.ncols):
                        data = sheet1.cell(row, col)
                        line.append(str(data.value))
                    writer.writerow(line)
                    lines += 1
    print(lines, file=sys.stderr)
