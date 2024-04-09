import datetime

def age_checker(date_of_birth):
    dob = date_of_birth.split("-")
    dob_format = ("%Y-%m-%d")
    res = True
    try:
        res = bool(datetime.datetime.strptime(date_of_birth,"%Y-%m-%d"))
    except ValueError:
        raise Exception("Incorrect date format")
    dob_date = datetime.date(int(dob[0]), int(dob[1]), int(dob[2]))
    today = datetime.date.today()
    year = today.year - dob_date.year
    if today.month < dob_date.month or (today.month == dob_date.month and today.day < dob_date.day):
        year -= 1
    if year >= 16:
        return "Access Granted"
    else:
        return f"You are too young, you are {year}. You need to be 16"
