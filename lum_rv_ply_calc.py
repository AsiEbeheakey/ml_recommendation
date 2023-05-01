product_type_list = ["lumber", "plywood", "rotary veneer"]


def volume_calculator(thickness, width, length, pcs):
    '''
    A function to calculate the volume of lumber, plywood, and rotary veneer
    '''
    volume = (thickness*width*length*pcs) / 1_000_000
    return volume


user_input = input("What is the product type? ")
if user_input in product_type_list:
    user_input_thickness = int(input("What is the thickness? "))
    user_input_width = int(input("What is the width? "))
    user_input_length = float(input("What is the length? "))
    user_input_pcs = int(input("What are the number of pieces? "))
    print(volume_calculator(thickness=user_input_thickness,
          width=user_input_width, length=user_input_length, pcs=user_input_pcs))
else:
    print("Product not available.")
