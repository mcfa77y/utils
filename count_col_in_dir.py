from os import getcwd, path
import sys
from pathlib import Path
from Utils import get_file_path_list

# directory = path.join(getcwd(), sys.argv[1])
directory = path.join(getcwd(), "../other")
extension = "csv"
# extension = sys.argv[2]
delimiter = ","

file_path_list = get_file_path_list(directory, extension)
for file_path in file_path_list:
  path = Path(file_path)
  count = -1
  with open(file_path) as f:
      count = next(f).count(delimiter)
      print(path.name + "\t" + str(count))