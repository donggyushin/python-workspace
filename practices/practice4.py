string = "a:b:c:d"
string_list = string.split(':')
transformed_string = '#'.join(string_list)
print(transformed_string)
