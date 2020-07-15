# import sys
# print(sys.executable)

import os

# src_dir = './test_dir/1'
# dst_dir = './test_dir/one'
# try:
#     os.rename(src_dir, dst_dir)
# except Exception as e:
#     print(e)
#     print(False)
# else:
#     print(True)
#
# src_file = './test_dir/1.py'
# dst_file = './test_dir/one.py'
# try:
#     os.rename(src_file, dst_file)
# except Exception as e:
#     print(e)
#     print(False)
# else:
#     print(True)

path = 'pascal_voc'
for cls in os.listdir(path):
    cls_path = os.path.join(path, cls)
    if os.path.isdir(cls_path):
        print(cls, type(cls))
        continue
    else:
        new_name = cls[:-10] + '.pth'
        print(new_name)
        old_dir = cls_path
        new_dir = os.path.join(path, new_name)
        print(old_dir)
        print(new_dir)
        os.rename(old_dir, new_dir)
