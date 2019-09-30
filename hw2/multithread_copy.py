from shutil import copy
from threading import Thread
from helper import file_list, dst_dir

for file_name in file_list:
  t = Thread( target=copy, args=[file_name, dst_dir] )
  t.start()