import json

json_string = '''{"array_of_nums":[{"number":0},{"number":1},{"number":2}],
                  "array_of_fruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'''
json_obj = json.loads(json_string)

print(json_obj.get('array_of_nums'))
print(json_obj.get('array_of_nums')[1])
print(json_obj.get('array_of_nums')[1].get('number') + json_obj.get('array_of_nums')[2].get('number'))
print(json_obj.get('array_of_fruits')[2].get('fruit'))
