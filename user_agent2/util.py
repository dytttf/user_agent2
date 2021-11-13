import re
import requests
from bs4 import BeautifulSoup


def show_chrome_version():
    url = "https://google_chrome.zh.downloadastro.com/old_versions/"
    text = requests.get(url).text
    soup = BeautifulSoup(text, "html.parser")

    version_date_info = {}

    for item in soup.select("table.versions > tbody > tr"):
        tds = [x.text.strip() for x in item.select("td")]
        version, date = tds[0], tds[2]
        version = re.search("(\d+\.\d+\.\d+\.\d+)", version)
        if not version:
            continue
        version = version.group(1).split(".")
        date = date.split(".")
        date.reverse()
        date = "-".join(date)
        version_date_info[date] = version

    dates = list(version_date_info.keys())
    dates.sort()

    for date in dates:
        version = version_date_info[date]
        print("({}, {}, {}),  # {}".format(version[0], version[2], version[2], date))

    return


# show_chrome_version()


def test():
    from user_agent2 import generate_user_agent

    for i in range(100):
        ua = generate_user_agent(navigator="chrome")
        print(ua)

    return


test()
