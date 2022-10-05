import datetime
import terminal_banner
from application import salary
from application.db import people

if __name__ == '__main__':
    today = datetime.datetime.today().strftime("%d-%m-%Y %H:%M")

    print(f'Hello world! Now time is {today}')
    print(salary.calculate_salary(23))
    print(people.get_employees())

    banner_text = "This is my banner text.\n\nThis is a second line of text."
    my_banner = terminal_banner.Banner(banner_text)
    print(my_banner)
