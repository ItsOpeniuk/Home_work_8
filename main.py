from datetime import date, datetime
from collections import defaultdict


def get_birthdays_per_week(users):
    birth_weekday = defaultdict(list)
    today = date.today()
    if len(users) == 0:
        return {}
    for user_data in users:
        user = user_data["name"]
        value = user_data["birthday"]
        delta_days = (value - today).days
        if 0 <= delta_days < 7:
            if value.weekday() in [5, 6]:
                weekday = 'Monday'
            else:
                weekday = value.strftime('%A')
            birth_weekday[weekday].append(user)
        else:
            value = value.replace(year=today.year + 1)
            delta_days = (value - today).days
            if 0 <= delta_days < 7:
                if value.weekday() in [5, 6]:
                    weekday = 'Monday'
                else:
                    weekday = value.strftime('%A')
                birth_weekday[weekday].append(user)
    return birth_weekday


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Выводим результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
