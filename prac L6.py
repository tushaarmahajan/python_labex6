import re
from datetime import datetime
def validate_travel_booking_form(name, passport_number, phone_number, email, departure_date, payment_method):
   #Here we'll verify the name
    if not re.fullmatch(r"[A-Za-z\s]+", name):
        return "Invalid name: Only alphabetic characters and spaces are allowed."
    
    #passport (alphanumeric and exactly 9 characters)
    if not re.fullmatch(r"[A-Za-z0-9]{9}", passport_number):
        return "Invalid passport number: Must be alphanumeric and exactly 9 characters long."
    
    #phone number
    if not re.fullmatch(r"\d{10}", phone_number):
        return "Invalid phone number: Must be a valid 10-digit number."
    
    #email address 
    if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
        return "Invalid email address: Must be in the correct format (e.g., example@example.com)."
    
    #departure date (format "dd/mm/yyyy")
    try:
        datetime.strptime(departure_date, "%d/%m/%Y")
    except ValueError:
        return "Invalid departure date: Must be in the format 'dd/mm/yyyy'."
    
    #payment method (either 'credit', 'debit', or 'netbanking')
    if payment_method.lower() not in ['credit', 'debit', 'netbanking']:
        return "Invalid payment method: Must be either 'credit', 'debit', or 'netbanking'."
    
    return "All inputs are valid!"

name = input("Enter your name: ")
passport_number = input("Enter your passport number: ")
phone_number = input("Enter your phone number: ")
email = input("Enter your email address: ")
departure_date = input("Enter your departure date (dd/mm/yyyy): ")
payment_method = input("Enter your payment method (credit, debit, netbanking): ")

# Validating the inputs
validation_result = validate_travel_booking_form(name, passport_number, phone_number, email, departure_date, payment_method)
print(validation_result)
