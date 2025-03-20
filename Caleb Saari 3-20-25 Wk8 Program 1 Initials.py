# Write a program that gets a string containing a person's first, middle, and last names,
# displays their first, middle, and last initials.
# For example, if the user enters John William Smith, the program should display J. W. S.

def get_initials(full_name):
    names = full_name.split()
    initials = [name[0].upper() for name in names]
    return ' '.join(initials)


full_name = input("Enter your full name (first, middle, last): ")
print("Your initials are:", get_initials(full_name))

# Caleb Saari 3/20/25 Wk8 Program 1: Initials