# Built-in imports

def reverse(text):
  """
  Takes input and reverses it
  Parameter
  text: str
      a string of text provided by the user
  
  Return
  string: str
      a reversed version of the input text
  """
  if len(text) <= 1:
    return text
  return reverse(text[1:]) + text[0]

def is_palindrome(string):
  """
  Takes in a string and returns boolean True or False
  depending if the string is a palindrome
  Parameters
  string: str
      a string of alphanumeric characters
  
  Return
  boolean True or False
  """
  string.strip()
  if len(string) <= 1:
    return True
  elif string[0] != string[-1]:
    return False
  return is_palindrome(string[1:-1])