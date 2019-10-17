import os

path = r"path1"
filenames = os.listdir(path)
print(filenames)


def delete(in_filename, out_filename):
    with open(in_filename, 'r', encoding='utf-8') as r:
        lines = r.readlines()
        # print(lines)
    with open(out_filename, 'w', encoding='gbk') as w:
        i = 1
        for line in lines:

            b = line.split(',')
            del b[0]
            c = ''
            j = 1
            for bs in b:
                c += bs
                if j != 6:
                    c += ','
                j = j + 1
            # print(c)
            if i == 1:
                w.write(c)
            if '日期' not in line and i > 1:
                # print(c)
                w.write(c)
            i = i + 1


for filename in filenames:
    in_filename = path + '\\' + filename
    out_filename = r"path2" + filename
    print(in_filename, out_filename)
    delete(in_filename, out_filename)
