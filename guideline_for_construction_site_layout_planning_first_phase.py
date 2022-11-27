#########################################################################
#
# Guideline for the construction site layout planning in the first phase
#
#########################################################################

# Calculate laydown area's size

def string_to_bool(string):
    if string == "True":
        return True
    else:
        return False

def laydown_area_size(area):
    # The laydown area's size is 115 sq.m. + 1% of the site area 
    # but should not exceed 300 sq.m.
    return 115 + 1/100 * area

# Check if the store has to be moved.
def check_store_move():
    moved = input("Is the store moved? (True/False)")
    moved = string_to_bool(moved)
    if moved:
        print ("Build the prefabricated store at the exact size (45-70 sq.m.)")
    else:
        print ("Move the store into the constucting building or place it over the site office to form a 2-floor site office and store.")

def check_office_movement():
    inside = input("Is the site office has to be moved inside the building? (True/False) : ")
    inside = string_to_bool(inside)
    if inside:
        print ("Use the prefabricated site office.")
    else:
        have_components = input("The user has the prefabricated site office in stock.(True/False) : ")
        have_components = string_to_bool(have_components)
        if have_components:
            print("Can use either the prefabricated one or the newly built one.")
        else:
            print("Use the newly built site office.")

# Calculate free space and percentage between the amount of the free sapce and construction site
def calculate_free_space(free_space, area):
    # if free space is more than 1600 sq.m.
    if (free_space > 1600):
        # if free space is less than 2000 sq.m. or 25% of the site area
        if free_space < 2000 or free_space < 25/100 * area:
            print ("Move site offices and the store into the constucting building or place them over each other to form a 2-floor site office and store.")
            check_store_move()
            check_office_movement()
        else:
            print ("The store's size is around 45-70 sq.m. The size of the site office is judged from the staff's number.")

        # Check if free space is still > 1600 sq.m. after the usage of other components.
        more = input("Is the free space still > 1600 sq.m. after the usage of other components? (True/False) : ")
        more = string_to_bool(more)
        if more:
            print("Consider the usage of the batching plant.")
        else:
            print("Cannot use the batching plant.")

    elif(free_space < 1600):
        print("Cannot use the batching plant.")
        steel_yard_size = (area + 5*free_space)/100
        if(steel_yard_size < 100):
            print("Consider to do the cutting and bending from outside, then, transport to the site.")
        else:
            print("Consider to do the cutting and bending on the site.")

construction_site_size = float(input("Enter the construction site size in sq.m. : "))
free_space = float(input("Enter the free space in sq.m. : "))

print("---------------------")
print("laydown area's size =", laydown_area_size(construction_site_size), "sq.m.")
calculate_free_space(free_space, construction_site_size)
print("---------------------")