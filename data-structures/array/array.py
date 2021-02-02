strings = ['a','b','c','d']

#push  
strings.append('z')                     # O(1)

#pop  
strings.pop()                           # O(1)

#add first 
strings.insert(0, 'x')                  # O(n)

#insert into
strings.insert(2, 'y')                  # O(n)

print(strings)