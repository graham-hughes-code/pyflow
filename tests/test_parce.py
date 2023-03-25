import pytest
from pyflow.parse import (
  find_mermaid_from_docstring,
  pull_doc_string_from_file,
  build_full_chart)


@pytest.fixture()
def mermaid_map():
  return {
    'isPalindrome': 'check if string is isPalindrome\n\n'
                    'Args:\n  str (String):\n\n\nReturns:'
                    '\n  Boolean: True if the str is a Palindrome'
                    '\n\nflowchart:\n  S[revers input str] -->'
                    ' X{reversed_str == str}\n  X -- true --> '
                    'N[return True]\n  X -- false --> M[return False]',
    'main': 'main of program\n\nflowchart:\n  A((Start)) --> B[\\Get '
            'user input\\]\n  B --> C[Check if Palindrome]\n  C -.-> '
            'isPalindrome\n  C -- true --> D[Write str is a Palindrome]'
            '\n  C -- true --> E[Write str is a Palindrome]'}


@pytest.fixture()
def example_file():
  return r'''
def isPalindrome(str):
  """
  check if string is isPalindrome

  Args:
    str (String):

  Returns:
    Boolean: True if the str is a Palindrome

  flowchart:
    S[revers input str] --> X{reversed_str == str}
    X -- true --> N[return True]
    X -- false --> M[return False]
  """
  str_reversed = str[::-1]
  return str == str_reversed


def main():
  """
  main of program

  flowchart:
    A((Start)) --> B[\\Get user input\\]
    B --> C[Check if Palindrome]
    C -.-> isPalindrome
    C -- true --> D[Write str is a Palindrome]
    C -- true --> E[Write str is a Palindrome]
  """
  s = input('Enter string\n')
  ans = isPalindrome(s)

  if ans:
    print(f"{s} is a Palindrome")
  else:
    print(f"{s} is not a Palindrome")

if __name__ == "__main__":
  main()
'''


def test_pull_doc_string_from_file(tmp_path, example_file):
  tmp_dir = tmp_path / "sub"
  tmp_dir.mkdir()
  test_file = tmp_dir / "test.py"
  test_file.write_text(example_file)

  doc_strings = pull_doc_string_from_file(test_file)
  print(doc_strings)

  assert len(doc_strings) == 2


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


def test_build_full_chart(mermaid_map):
  excepted_output = r'''flowchart TD
subgraph isPalindrome
Args:
  str (String):


Returns:
  Boolean: True if the str is a Palindrome

flowchart:
  S[revers input str] --> X{reversed_str == str}
  X -- true --> N[return True]
  X -- false --> M[return False]
end
subgraph main
flowchart:
  A((Start)) --> B[\Get user input\]
  B --> C[Check if Palindrome]
  C -- true --> D[Write str is a Palindrome]
  C -- true --> E[Write str is a Palindrome]
end
check if string is isPalindrome
main of program
  C -.-> isPalindrome'''
  assert build_full_chart(mermaid_map, 'TD') == excepted_output
