import re

def uezguem_check(text):
  return 1 if re.search('^(u+|w+)e+\s+z+s*(g+|k+)(u+e+|o+)m+$', text, re.IGNORECASE) else 0
