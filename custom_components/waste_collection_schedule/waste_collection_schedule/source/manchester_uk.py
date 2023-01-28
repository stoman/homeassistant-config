import logging
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from waste_collection_schedule import Collection  # type: ignore[attr-defined]

TITLE = "Manchester City Council"
DESCRIPTION = "Source for bin collection services for Manchester City Council, UK."
URL = "https://www.manchester.gov.uk"
TEST_CASES = {
    "domestic": {"uprn": "000077065560"},
}

API_URL = "https://www.manchester.gov.uk/bincollections/"
ICON_MAP = {
    "Black / Grey Bin": "mdi:trash-can",
    "Blue Bin": "mdi:recycle",
    "Brown Bin": "mdi:glass-fragile",
    "Green Bin": "mdi:leaf",
}

_LOGGER = logging.getLogger(__name__)


class Source:
    def __init__(self, uprn: int):
        self._uprn = uprn

    def fetch(self):
        entries = []

        r = requests.post(
            API_URL,
            data={"mcc_bin_dates_uprn": self._uprn, "mcc_bin_dates_submit": "Go"},
        )

        soup = BeautifulSoup(r.text, features="html.parser")
        results = soup.find_all("div", {"class": "collection"})

        for result in results:
            date = result.find("p", {"class": "caption"})
            dates = []
            dates.append(str(date.text).replace("Next collection ", "", 1))
            for date in result.find_all("li"):
                dates.append(date.text)
            img_tag = result.find("img")
            collection_type = img_tag["alt"]
            for current_date in dates:
                date = datetime.strptime(current_date, "%A %d %b %Y").date()
                entries.append(
                    Collection(
                        date=date,
                        t=collection_type,
                        icon=ICON_MAP[collection_type],
                    )
                )

        return entries
