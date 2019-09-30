from shutil import copy
from multiprocessing import Pool
from helper import file_list, dst_dir

def copy_helper(file_name):
  copy(file_name, dst_dir)

p = Pool(10)
p.map(copy_helper, file_list)