from os import listdir
from os.path import isfile, join, dirname, abspath

working_dir = dirname(abspath(__file__))
src_dir = working_dir + '/src'
dst_dir = working_dir + '/dst'

print working_dir

file_list = [
  join(src_dir, file)
  for file in listdir(src_dir)
  if isfile(join(src_dir, file))
]