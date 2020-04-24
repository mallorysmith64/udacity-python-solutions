# Instructions:
# Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.

#solution
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)



#solution if you wanted lowercased first initials instead
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name[0].lower() for name in names]
print(first_names)

