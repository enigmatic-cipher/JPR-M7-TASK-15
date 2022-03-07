"""
Given a String as input, move all the digits to the end of the string. Use recursion. Do not use loops. Do a dry run for each test case.
Input-> "123#check#456#done"
Output-> #check#done#123456
"""

def recur(st):
  ln = len(st)
  if ln == 0:
    return ""
  ch = st[0]
  st1 = st[1:]
  if not (ch>='0' and ch<='9'):
    return ch + recur(st1)
  elif (ch>='0' and ch<='9'):
    return ch + recur(st1)

st = "123#check#456#done"
print(recur(st))
