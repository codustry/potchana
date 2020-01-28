url = "https://sites.google.com/site/thaidictproject/"

from requests_html import HTMLSession

session = HTMLSession()

r = session.get(url)

sel1 = '#sites-canvas-main-content > table > tbody > tr > td > div > div:nth-child(11) > div:nth-child(4) > div > div > div:nth-child(11) > table > tbody > tr > td:nth-child(2)'
sel2 = '#sites-canvas-main-content > table > tbody > tr > td > div > div:nth-child(11) > div:nth-child(4) > div > div > div:nth-child(11) > table > tbody > tr:nth-child(3) > td:nth-child(2) > div:nth-child(2) > b > a'

download_links = r.html.find(f"{sel1} a")

for dl in download_links:
    print(dl, dl.text)