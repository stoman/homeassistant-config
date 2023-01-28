from datetime import datetime

import requests
from bs4 import BeautifulSoup
from waste_collection_schedule import Collection  # type: ignore[attr-defined]

TITLE = "East Herts Council"
DESCRIPTION = "Source for www.eastherts.gov.uk services for East Herts Council."
URL = "https://www.eastherts.gov.uk"
TEST_CASES = {
    "Example": {
        "address_postcode": "SG9 9AA",
        "address_name_numer": "1 Trove House",
        "address_street": "Baldock Road",
    },
    "Example No Postcode Space": {
        "address_postcode": "SG99AA",
        "address_name_numer": "1 Trove House",
        "address_street": "Baldock Road",
    },
}
ICON_MAP = {
    "Refuse": "mdi:trash-can",
    "Recycling": "mdi:recycle"
}

API_URL = "https://uhte-wrp.whitespacews.com/"


class Source:
    def __init__(
        self,
        address_name_numer=None,
        address_street=None,
        street_town=None,
        address_postcode=None,
    ):
        self._address_name_numer = address_name_numer
        self._address_street = address_street
        self._street_town = street_town
        self._address_postcode = address_postcode

    def fetch(self):
        session = requests.Session()

        # get link from first page as has some kind of unique hash
        r = session.get(
            API_URL,
        )
        r.raise_for_status()
        soup = BeautifulSoup(r.text, features="html.parser")

        alink = soup.find("a", text="Find my bin collection day")

        if alink is None:
            raise Exception("Initial page did not load correctly")

        # greplace 'seq' query string to skip next step
        nextpageurl = alink["href"].replace("seq=1", "seq=2")

        data = {
            "address_name_numer": self._address_name_numer,
            "address_street": self._address_street,
            "street_town": self._street_town,
            "address_postcode": self._address_postcode,
        }

        # get list of addresses
        r = session.post(nextpageurl, data)
        r.raise_for_status()

        soup = BeautifulSoup(r.text, features="html.parser")

        # get first address (if you don't enter enough argument values this won't find the right address)
        alink = soup.find("div", id="property_list").find("a")

        if alink is None:
            raise Exception("Address not found")

        nextpageurl = API_URL + alink["href"]

        # get collection page
        r = session.get(
            nextpageurl,
        )
        r.raise_for_status()
        soup = BeautifulSoup(r.text, features="html.parser")

        if soup.find("span", id="waste-hint"):
            raise Exception("No scheduled services at this address")

        u1s = soup.find("section", id="scheduled-collections").find_all("u1")

        entries = []

        for u1 in u1s:
            lis = u1.find_all("li", recursive=False)
            entries.append(
                Collection(
                    date=datetime.strptime(
                        lis[1].text.replace("\n", ""), "%d/%m/%Y"
                    ).date(),
                    t=lis[2].text.replace("\n", ""),
                    icon=ICON_MAP.get(
                        lis[2].text.replace("\n", "").replace(" Collection Service", "")
                    ),
                )
            )

        return entries
