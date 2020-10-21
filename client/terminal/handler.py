import os
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')


from unicards import unicard

def show_card(color,value):

    color = color[0].lower()

    values = {}
    values["SEVEN"]="7"
    values["HEIGHT"]="8"
    values["NINE"]="9"

    lower = True
    for key in values.keys():
        if value == key:
            value = values[key]
            lower = False
            break

    if lower :
        value = value[0]

    str =  unicard(value+color, color=True)

    return str
