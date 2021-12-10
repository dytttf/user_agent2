from user_agent import base
from datetime import datetime

#
base.OS_PLATFORM.update(
    {
        "win": base.OS_PLATFORM["win"]
        + (
            "Windows NT 10.0",  # Windows 10
            "Windows NT 11.0",  # Windows 11
        ),
        "mac": base.OS_PLATFORM["mac"]
        + (
            "Macintosh; Intel Mac OS X 10.13",
            "Macintosh; Intel Mac OS X 10.14",
            "Macintosh; Intel Mac OS X 10.15",
        ),
        "android": base.OS_PLATFORM["android"]
        + (
            "Android 7.1.2",  # 2016-12-05
            "Android 8.0",  #
            "Android 8.1",  #
            "Android 9",  #
            "Android 10",  #
            "Android 11",  #
        ),
    }
)
# https://zh.wikipedia.org/wiki/Firefox%E7%89%88%E6%9C%AC%E5%8E%86%E5%8F%B2
base.FIREFOX_VERSION = base.FIREFOX_VERSION + (
    ("52.0", datetime(2017, 3, 7)),
    ("53.0", datetime(2017, 4, 19)),
    ("54.0", datetime(2017, 6, 13)),
    ("55.0", datetime(2017, 8, 8)),
    ("56.0", datetime(2017, 9, 28)),
    ("57.0", datetime(2017, 11, 14)),
    ("58.0", datetime(2018, 1, 23)),
    ("59.0", datetime(2018, 3, 13)),
    ("60.0", datetime(2018, 5, 9)),
    ("61.0", datetime(2018, 6, 26)),
    ("62.0", datetime(2018, 9, 5)),
    ("63.0", datetime(2018, 10, 23)),
    ("64.0", datetime(2018, 12, 11)),
    ("65.0", datetime(2019, 1, 29)),
    ("66.0", datetime(2019, 3, 19)),
    ("67.0", datetime(2019, 5, 21)),
    ("68.0", datetime(2019, 7, 13)),
    ("69.0", datetime(2019, 9, 3)),
    ("70.0", datetime(2019, 10, 22)),
    ("71.0", datetime(2019, 12, 3)),
    ("72.0", datetime(2020, 1, 7)),
    ("73.0", datetime(2020, 2, 11)),
    ("74.0", datetime(2020, 3, 10)),
    ("75.0", datetime(2020, 4, 7)),
    ("76.0", datetime(2020, 5, 5)),
    ("77.0", datetime(2020, 6, 2)),
    ("78.0", datetime(2020, 6, 30)),
    ("79.0", datetime(2020, 7, 28)),
    ("80.0", datetime(2020, 8, 25)),
    ("81.0", datetime(2020, 9, 22)),
    ("82.0", datetime(2020, 10, 20)),
    ("83.0", datetime(2020, 11, 17)),
    ("84.0", datetime(2020, 12, 15)),
    ("85.0", datetime(2021, 1, 26)),
    ("86.0", datetime(2021, 2, 23)),
    ("87.0", datetime(2021, 3, 23)),
    ("88.0", datetime(2021, 4, 20)),
    ("89.0", datetime(2021, 6, 1)),
    ("90.0", datetime(2021, 7, 13)),
    ("91.0", datetime(2021, 8, 10)),
    ("92.0", datetime(2021, 9, 7)),
    ("93.0", datetime(2021, 10, 5)),
    ("94.0", datetime(2021, 11, 2)),
)

# https://google_chrome.zh.downloadastro.com/old_versions/
base.CHROME_BUILD = base.CHROME_BUILD + [
    "87.0.4280.66",  # 2020-11-20
    "87.0.4280.88",  # 2020-12-02
    "87.0.4280.141",  # 2021-01-10
    "89.0.4389.82",  # 2021-03-06
    "89.0.4389.90",  # 2021-03-14
    "89.0.4389.114",  # 2021-04-09
    "90.0.4430.72",  # 2021-04-16
    "90.0.4430.85",  # 2021-04-23
    "90.0.4430.212",  # 2021-05-12
    "91.0.4472.77",  # 2021-05-27
    "91.0.4472.101",  # 2021-06-11
    "91.0.4472.114",  # 2021-06-18
    "91.0.4472.124",  # 2021-06-24
    "91.0.4472.164",  # 2021-07-15
    "92.0.4515.107",  # 2021-07-21
    "92.0.4515.131",  # 2021-08-05
    "92.0.4515.159",  # 2021-08-20
    "93.0.4577.63",  # 2021-09-03
    "94.0.4606.61",  # 2021-09-25
    "94.0.4606.81",  # 2021-10-07
    "95.0.4638.54",  # 2021-10-22
]
#
base.MACOSX_CHROME_BUILD_RANGE.update(
    {
        "10.13": (0, 6),
        "10.14": (0, 6),
        "10.15": (0, 7),
        "11.0": (0, 2),
    }
)

generate_user_agent = base.generate_user_agent
generate_navigator = base.generate_navigator
generate_navigator_js = base.generate_navigator_js
