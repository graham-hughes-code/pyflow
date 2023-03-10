from pyflow.parse import find_mermaid_from_docstring


def test_find_mermaid_from_docstring():
  assert 'A-->B' in find_mermaid_from_docstring(
    '''hello this is a function 

      Args:
        some args

      Returns:
        something

      flowchart:
        A-->B
    ''')

  assert 'C--D' in find_mermaid_from_docstring(
    '''hello this is a function 

      Args:
        some args

      Returns:
        something

      flowchart:
        A-->B
        C--D
    ''')