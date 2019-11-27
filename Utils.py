from os import listdir, path
def get_file_path_list(directory, extension):
  result = []
  for file in listdir(directory):
    if file.endswith('.' + extension):
      result.append(path.join(directory, file))
  return result