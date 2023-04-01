import ast


def pull_doc_string_from_file(file_name):
  '''
  Pulls docstring from functions in file

  FIXME: does not pull docstrings from classes or class functions

  Args:
    file_name (str): The name of the file to pull from.

  Returns:
    Dict: Map of function name to the doc string.
  '''
  with open(file_name) as fd:
   file_contents = fd.read()

  module = ast.parse(file_contents)

  function_definitions = [node for node in module.body if isinstance(node, ast.FunctionDef)]

  func_name_to_docstring_map = {}
  for f in function_definitions:
    func_name_to_docstring_map[f.name] = ast.get_docstring(f)

  return func_name_to_docstring_map


def create_mermaid_map(func_name_to_docstring_map):
  '''
  Pulls out mermaid chart from docstring map

  Args:
    func_name_to_docstring_map (Dict): a Dict with that contains function name: docstring

  Return:
    Dict: map of function name: mermaid chart
  '''

  mermaid_map = {}

  for func_name, docstring in func_name_to_docstring_map.items():
    mermaid_map[func_name] = find_mermaid_from_docstring(docstring)

  return mermaid_map


def find_mermaid_from_docstring(docstring):
  '''
    finds mermaid in docstring.
    The format is as follows:
    flowchart:
      everything after

    FIXME: very hacky

    Arg:
      str (string): The string to find the mermaid chart from.
    
    Returns:
      string: return string if found None if not found
  '''

  if not docstring:
    return None

  if 'flowchart:' not in docstring:
    return None

  flowchart = docstring.split('flowchart:')[1]

  flowchart = '\n'.join(line.strip(' \n\t') for line in flowchart.split('\n'))

  return flowchart


def build_full_chart(mermaid_map, orientation):
  '''
  combines individual flow charts

  Args:
    mermaid_map (Dict): function name: flow chart
    orientation (str): the orientation of the chart

  Returns:
    complied flow chart
  '''

  header = f'flowchart {orientation}\n'

  function_names = list(mermaid_map.keys())

  strip_joins_mermaid_map = {}
  function_joins = []

  for fn, fc in mermaid_map.items():
    new_fc = []
    for line in fc.splitlines():
      skip_line = False
      for function_name in function_names:
        if function_name in line and f'{function_name}()' not in line:
          skip_line = True
          function_joins.append(line)
      if not skip_line:
        new_fc.append(line)
    strip_joins_mermaid_map[fn] = '\n'.join(new_fc)

  mermaid_map = strip_joins_mermaid_map

  subgraphs = [
    f'subgraph {fn}{fc}\nend'
    for fn, fc in mermaid_map.items()
  ]

  subgraphs_str = "\n".join(subgraphs)

  function_joins_str = '\n'.join(function_joins)

  return f'{header}{subgraphs_str}\n{function_joins_str}'
