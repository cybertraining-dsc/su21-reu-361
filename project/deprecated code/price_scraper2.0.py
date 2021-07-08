#This code was taken from
#https://medium.com/c%C3%B3digo-ecuador/how-to-scrape-cryptocurrency-data-prices-volume-percent-change-dbb77c11fd82
#but it is broken. Yay!



from datetime import datetime, timedelta
import time, requests, pandas, lxml
from lxml import html

date_timetuple = date_datetime.timetuple()

date_mktime = time.mktime(date_timetuple)

date_int = int(date_mktime)

date_str = str(date_int)


def format_date(date_datetime):
    date_timetuple = date_datetime.timetuple()
    date_mktime = time.mktime(date_timetuple)
    date_int = int(date_mktime)
    date_str = str(date_int)
    return date_str

datetime_start = datetime.today() - timedelta(days=1000)
datetime_end = datetime.today() #Define end date as today's date

start = format_date(dt_start)
end = format_date(dt_end)

subdoma="/quote/{0}/history?period1={1}&period2={2}&interval=1d&filter={3}&frequency=1d"

subdomain = subdoma.format(symbol, start, end, filter)


def subdomain(symbol, start, end, filter='history'):
subdoma="/quote/{0}/history?period1={1}&period2={2}&interval=1d&filter={3}&frequency=1d"
subdomain = subdoma.format(symbol, start, end, filter)


def subdomain(symbol, start, end, filter='history'):
    subdoma = "/quote/{0}/history?period1={1}&period2={2}&interval=1d& filter = {3} & frequency = 1d"
    subdomain = subdoma.format(symbol, start, end, filter)
    return subdomain

symbol = 'BTC-USD'
sub = subdomain(symbol, start, end)
#We do not need to include the filter argument because arguments with default values are optional.base_url = 'https://finance.yahoo.com'
url = base_url + sub


def header_function(subdomain):
    hdrs = {"authority": "finance.yahoo.com",
            "method": "GET",
            "path": subdomain,  # path key assigned as subdomain
            "scheme": "https",
            "accept": "text/html",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "cookie": "Cookie:identifier",
            "dnt": "1",
            "pragma": "no-cache",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64)"}
    return hdrs

page = requests.get(url, headers=header)
element_html = html.fromstring(page.content)
table = element_html.xpath('//table')
table_tree = lxml.etree.tostring(table[0], method='xml')
panda = pandas.read_html(table_tree)


def scrape_page(url, header):
    page = requests.get(url, params=header)
    element_html = html.fromstring(page.content)
    table = element_html.xpath('//table')
    table_tree = lxml.etree.tostring(table[0], method='xml')
    panda = pandas.read_html(table_tree)
    return panda