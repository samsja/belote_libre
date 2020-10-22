def get_path_card(color,value):

    color = color[0]

    values = {}
    values["SEVEN"]="7"
    values["HEIGHT"]="8"
    values["NINE"]="9"
    values["TEN"]="10"


    letter = True
    for key in values.keys():
        if value == key:
            value = values[key]
            letter = False
            break

    if letter:
        value = value[0]

    return value+color
