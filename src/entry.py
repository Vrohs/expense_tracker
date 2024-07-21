from datetime import datetime

d_format = "%d-%m-%Y"

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(d_format)
    
    try:
        valid_date = datetime.strptime(date_str, d_format)
        return valid_date.strftime(d_format)
    except ValueError:
        print("Invalid input format, pls. enter in dd-mm-yyyy")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Enter valid amount")
        return amount
    except ValueError as e:
        print(e)
        return get_amount() 

def get_category():
    pass


def get_description():
    pass

