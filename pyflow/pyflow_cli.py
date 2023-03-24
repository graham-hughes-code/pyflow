from pyflow.parse import pull_doc_string_from_file, create_mermaid_map, build_full_chart
import argparse


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('path', nargs='*', help='The path of the file to pull flowchart from.')
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

  func_name_to_docstring_map = pull_doc_string_from_file(path)

  mermaid_map = create_mermaid_map(func_name_to_docstring_map)

  print(build_full_chart(mermaid_map=mermaid_map, orientation=orientation))

  return 0
