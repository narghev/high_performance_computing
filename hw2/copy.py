from shutil import copy
from helper import file_list, dst_dir

for file in file_list:
  copy(file, dst_dir)