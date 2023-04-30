# As normal conditional list comprehension
list1 = [ 1 if x % 2 else 0 for x in range(11)]
list1_generator = ( 1 if x % 2 == 0 else 0 for x in range(11))

print('Comprehension result:', list1)
print('Generator result:', list1_generator)

print('', 'Running the generator...', sep='\n')
for i in list1_generator:
    print(i, end=' ')
print()
