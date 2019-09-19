print('%s is %d years old' % ("Mary", 30))

print('{0} is {1} years old'.format("Mary", 30))
print('{1} is {0} years old'.format(30, "Mary"))
print('{} is {} years old'.format("Mary", 30))
print('{name} is {age} years old'.format(name="Tom", age=30))
print('{name} is {age} years old'.format(age=30, name="Tom"))
print('{0} is {age} years old'.format('Tom', age=30))

print('{0} {1} {2}'.format(123, 12345.678, 'Python'))
print('{0:d} {1:.2f} {2:s}'.format(123, 12345.678, 'Python'))
print('{0:d} {1:10.2f} {2:s}'.format(123, 12345.678, 'Python'))
print('{0:d} {1:<10.2f} {2:s}'.format(123, 12345.678, 'Python'))
print('{} {:.2f} {}'.format(123, 12345.678, 'Python'))
