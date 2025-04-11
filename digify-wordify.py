# customer = {
#     "name": "Adeoluwa Adeleke",
#     "age": 27,
#     "is_verified": True
# }
# print(customer["age"])
# print(customer.get('birthyear', 1997))
# customer["location"] = "Ibadan"
# print(customer)


# to translate digits to numbers
phone = input('Phone: ')

digits_mapping = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'Zero'
}
output = ''
for character in phone:
    output += digits_mapping.get(character, '!') + ' '
print(output)
