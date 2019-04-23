#!/usr/bin/env python3

import csv
import requests
import sys
from bs4 import BeautifulSoup

def main():
    fieldnames = ["organization", "location", "description", "website"]
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    writer.writeheader()

    url = "http://www.acbp.net/grant-directory.php"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    for row in soup.find("div", {"class": "grant_list_outer"}).find_all("div", {"class": "wrapper_div"})[1:]:
        organization = row.find("div", {"class": "grant_bdy_organization"}).text
        location = row.find("div", {"class": "grant_bdy_location"}).text
        description = row.find("div", {"class": "grant_bdy_description"}).text
        website = row.find("div", {"class": "grant_bdy_website"}).text.strip()

        writer.writerow({
            "organization": organization,
            "location": location,
            "description": description,
            "website": website,
        })


if __name__ == "__main__":
    main()
