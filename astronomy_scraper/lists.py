class Country:
    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation


class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country


class Countries:
    uk = Country('united kingdom', 'uk')


class Locations:
    london = Location('london', Countries.uk)


class TimeAndDateCom:
    images = {
        1: 'Sunny',
        2: 'More sun than clouds.',
        3: 'Sunny',
        4: 'Sunny',
        5: 'Sunny',
        6: 'Sunny',
        7: 'Sunny',
        8: 'Sunny',
        9: 'Sunny',
        10: 'Sunny',
        18: 'Sprinkes early. Morning Clouds.',

    }
