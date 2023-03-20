def roll_call_dwarves(dwarves):

    i = 0
    for dwarf in dwarves:
        i += 1
        print(f"{i}. {dwarf}")


def summon_captain_planet(elements):

    formatted_elements = [element.capitalize() + "!" for element in elements]
    print(formatted_elements)
    return formatted_elements

summon_captain_planet(["teutons", "japanese", "aztecs"])

def long_planeteer_calls(elements):
    long_found = False
    for element in elements:
        if len(element) > 4:
            long_found = True
    return long_found

def find_the_cheese(snacks):
    snack_found = False
    for snack in snacks:
        if snack == "cheddar" or snack == "gouda" or snack == "camembert":
            snack_found = True
            return snack
    if snack_found == False:
        return None
        
