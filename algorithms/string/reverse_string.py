def reverse(str):
  lst =[]

  for i in reversed(range(len(str))):
    lst.append(str[i])

  return ''.join(lst)

# Special for Python array slicing
def slicing_reverse(str):
    return str[: : -1]


str = reverse('I am a programmer')              # O(n)
str2 = slicing_reverse('I am a programmer')     # O(n)

print(str) 
print(str2)