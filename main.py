# Built-in imports

def reverse(text):
  """takes an string of text and returns it in reverse"""
  if len(text) <= 1:
    return text
  return reverse(text[1:]) + text[0]

def is_palindrome(string):
  """Takes in a string and returns boolean True or False depending on if the string is a palindrome"""
  string.strip()
  if len(string) <= 1:
    return True
  elif string[0] != string[-1]:
    return False
  return is_palindrome(string[1:-1])