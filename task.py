first_name=input("Enter First Name:\t")
middle_name=input("Enter Middle Name:\t")
last_name=input("Enter Last Name:\t")

#sol 1 - string.format()
output="{}.{} {}".format(first_name[0].title(),middle_name[0].title(),last_name.title())
print(output)