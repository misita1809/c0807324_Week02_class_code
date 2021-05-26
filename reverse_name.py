# Function which accepts the user's first and last name and print them in reverse order with a space between them (week02)
def reverse(first_name, last_name):
     name = first_name+" "+last_name
     return name[-1::-1]