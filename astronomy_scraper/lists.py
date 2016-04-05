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
