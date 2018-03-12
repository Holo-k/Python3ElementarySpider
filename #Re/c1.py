import re

content = 'price is $5.00'
pattern = 'price is $5.00'
result = re.match(pattern, content)
print(result)  #None

pattern = 'price is \$5\.00'
result = re.match(pattern, content)
print(result.group())
