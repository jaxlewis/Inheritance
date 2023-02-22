import PersonClass as p

name = "John"
address = "1234 Main St"
phone = "123-456-7890"
cust_num = 1234
mail_pref_flag = True


person1 = p.Person(name, address, phone)


customer1 = p.Customer(name, address, phone, cust_num, mail_pref_flag)


person1.print_person()

print()
print()
print()

customer1.print_person()
