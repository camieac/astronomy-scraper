from spiders.moon import MoonPhaseSpider
from items import MoonPhaseSnippet
from datetime import datetime



def moon_phase(data, day):
    '''
    Given a MoonPhaseSnippet, work out the moon phase percentage for a given
    day.
    '''
    if not isinstance(data, MoonPhaseSnippet):
        raise TypeError
    if not isinstance(day, datetime):
        raise TypeError

if __name__ == "__main__":
    spider = MoonPhaseSpider()
    print moon_phase()
