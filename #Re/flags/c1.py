import re

content = '''Hello 132465789 World_This
is Regex Demo
'''
pattern = '^He.*?(\d+).*Demo$'
result = re.match(pattern, content)
print(result)  #None