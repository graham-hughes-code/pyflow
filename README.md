# pyflow
An experiment in compiling flowcharts(mermaid) in docstrings together.

All text after `flowchart:` should be [mermaid flowchart syntax](https://mermaid.js.org/syntax/flowchart.html).

Example:
for the given file palindrome.py
```python

def isPalindrome(str):
  """
  check if string is isPalindrome

  Args:
    str (String):
  

  Returns:
    Boolean: True if the str is a Palindrome

  flowchart:
    S[reverse input str] --> X{reversed_str == str}
    X -- true --> N[return True]
    X -- false --> M[return False]
  """
  str_reversed = str[::-1]
  return str == str_reversed


def main():
  """
  main of program
  
  flowchart:
    A((Start)) --> B[\Get user input\]
    B --> C[Check if Palindrome]
    C -.-> isPalindrome
    C -- true --> D[Write str is a Palindrome]
    C -- false --> E[Write str is not a Palindrome]
  """
  s = input('Enter string\n')
  ans = isPalindrome(s)
  
  if ans:
    print(f"{s} is a Palindrome")
  else:
    print(f"{s} is not a Palindrome")

if __name__ == "__main__":
  main()
```

If you run `python pyflow .\palindrome.py`

The output will be:
```
flowchart TD
subgraph isPalindrome
S[reverse input str] --> X{reversed_str == str}
X -- true --> N[return True]
X -- false --> M[return False]
end
subgraph main
A((Start)) --> B[\Get user input\]
B --> C[Check if Palindrome]
C -- true --> D[Write str is a Palindrome]
C -- false --> E[Write str is not a Palindrome]
end
C -.-> isPalindrome
```

```mermaid
flowchart TD
subgraph isPalindrome
S[reverse input str] --> X{reversed_str == str}
X -- true --> N[return True]
X -- false --> M[return False]
end
subgraph main
A((Start)) --> B[\Get user input\]
B --> C[Check if Palindrome]
C -- true --> D[Write str is a Palindrome]
C -- false --> E[Write str is not a Palindrome]
end
C -.-> isPalindrome
```

Output can be view by using the [mermaid Live Editor](https://mermaid.live/) or 
[the mermaid cli](https://github.com/mermaid-js/mermaid-cli) or rendered in a github README.