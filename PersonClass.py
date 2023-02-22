class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def print_person(self):
        print("Name:", self.__name)
        print("Address:", self.__address)
        print("Phone #:", self.__phone)


class Customer(Person):
    def __init__(self, name, address, phone, cust_num, mail_pref):
        Person.__init__(self, name, address, phone)
        self.__cust_num = cust_num
        self.__mail_pref = mail_pref

    def print_person(self):
        Person.print_person(self)

        print(f"Customer Number: {self.__cust_num}")
        if self.__mail_pref:
            print("On Mailing List: Yes")
        else:
            print("On Mailing List: No")
