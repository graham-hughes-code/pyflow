from pyflow.parse import pull_doc_string_from_file, create_mermaid_map, build_full_chart
import argparse
import os
from fnmatch import fnmatch

root = '/some/directory'


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('path', nargs='*', help='The path of the file(\'s) to pull flowchart from.')
  parser.add_argument('-o',
                      '--orientation',
                      default='TB',
                      help='The orientation of the flowchart can '
                           'be Possible FlowChart orientations are: '
                           'TB - top to bottom. '
                           'TD - top-down same as top to bottom. '
                           'BT - bottom to top. '
                           'RL - right to left. '
                           'LR - left to right.')
  args = parser.parse_args()

  if not args.path:
    print('Error: file not given.')
    return 1

  path = args.path[0]

  if (orientation := args.orientation.upper()) not in ['TB', 'TD', 'BT', 'RL', 'LR']:
    print(f'Error: {args.orientation} is not a valid orientation.')
    return 1

  if os.path.isdir(path):
    files = []
    pattern = "*.py"
    for c_path, subdirs, c_files in os.walk(path):
        for name in c_files:
          if fnmatch(name, pattern):
            files.append(os.path.join(c_path, name))
    func_name_to_docstring_map = {}
    for f in files:
      func_name_to_docstring_map = {**pull_doc_string_from_file(f),
                                    **func_name_to_docstring_map}

  elif os.path.isfile(path):
    func_name_to_docstring_map = pull_doc_string_from_file(path)
  else:
     print('Error: there was a problem with the path entered.')
     return 1
  
  if not func_name_to_docstring_map:
    print('Error: no flowcharts in docstrings')
    return 1

  mermaid_map = create_mermaid_map(func_name_to_docstring_map)

  print(build_full_chart(mermaid_map=mermaid_map, orientation=orientation))

  return 0
