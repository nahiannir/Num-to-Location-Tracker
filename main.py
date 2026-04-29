import phonenumbers
from phonenumbers import geocoder  # Used to get location info for a phone number

# Run the program in an infinite loop so user can check multiple numbers
while True:
    
    # Take phone number input from user (must include country code, e.g. +880...)
    phone_num1 = input('\nEnter phone number (or type "exit" to quit): ')
    
    if phone_num1.lower() == "exit":
        break
    
    # Parse the string input into a structured phone number object
    phone_num = phonenumbers.parse(phone_num1)

    # Print header for output
    print('\nPhone Number Location:')
    
    # Get and display the geographical location (country/region) of the number
    print(geocoder.description_for_number(phone_num, 'en') + '\n')