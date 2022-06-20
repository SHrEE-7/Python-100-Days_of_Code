def format_function(f_name,l_name):
  if f_name=="" or l_name =="":
    return "You didn't provide valid inputs\n"
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"
print(format_function(input("enter your first name\n"),input("enter your last name\n")))