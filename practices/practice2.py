# Print number showing gender from pin-number
pin = "881120-1068234"
pin_list = pin.split("-")
number_showing_gender = pin_list[1][:1]
print('number showing gender is ', number_showing_gender)
