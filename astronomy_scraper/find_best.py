import weather_sources as s
import datetime
from scrapy.crawler import CrawlerProcess

class BestFinder:
    '''
    Find the best time slot for astronomy given a lookahead period
    and/or time window.
    '''

    def find_best(
        lookahead_days=10,
        window_start=best_window()[0],
            window_end=best_window()[1]):
                lower_limit = datetime.datetime.now()

                # Set the search upper limit
                upper_limit = today
                upper_limit.date.day += lookahead_days

                print lower_limit
                print upper_limit

                return [1, 1]

    def best_window()
        best_start =
        return [best_start, best_end]

    def construct_sunset_url(day):
        pass

b = BestFinder()
b.find_best()

if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(WeatherSpider)
    process.start()
