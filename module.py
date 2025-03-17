import converter

while True:
    command = input("Do you wish to convert Kgs(K/k) or Lbs(L/l)? ")
    if command == 'l':
        weight = int(input("Your weight in Lbs: "))
        print(converter.lbs_to_kg(weight))
    elif command == 'k':
        weight = int(input("Your weight in Kgs: "))
        print(converter.kg_to_lbs(weight))
