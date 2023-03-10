from pyflow.parse import pull_doc_string_from_file, create_mermaid_map, build_full_chart
import argparse


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('path', nargs='*')
  args = parser.parse_args()

  func_name_to_docstring_map = pull_doc_string_from_file(args.path[0])

  mermaid_map = create_mermaid_map(func_name_to_docstring_map)

  print(build_full_chart(mermaid_map=mermaid_map, orientation='TD'))

  return 0
