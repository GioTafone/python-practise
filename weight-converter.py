input_weight = input('Weight: ')
weight = int(input_weight)

input_unit = input('(L)bs or (K)g: ')
uppercase_conversion = input_unit.upper()

lbs_to_kg = weight / 2.2


if uppercase_conversion == 'K':
    weight_kg = weight * 2.2
    print(f'You are {weight_kg} pounds')
elif uppercase_conversion == 'L':
    weight_lbs = weight / 2.2
    print(f'You are {weight_lbs} kilos')
else:
    print('Invalid input. Use only "K" or "k" for Kilos and "L" or "l" for pounds')

