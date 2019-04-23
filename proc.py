#!/usr/bin/env python3

import csv
import sys


def main():
    with open(sys.argv[1], newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        print("""insert into donations (donor, donee, amount, donation_date, donation_date_precision, donation_date_basis, cause_area, url, notes) values""")
        first = True

        for row in reader:
            print(("    " if first else "    ,") + "(" + ",".join([
                mysql_quote("Andrea & Charles Bronfman Philanthropies"),  # donor
                mysql_quote(row["organization"]),  # donee
                "10000",  # amount
                mysql_quote("2016-01-01"),  # donation_date
                mysql_quote("year"),  # donation_date_precision
                mysql_quote("donation log"),  # donation_date_basis
                mysql_quote(""),  # cause_area
                mysql_quote("http://www.acbp.net/grant-directory.php"),  # url
                mysql_quote(row["description"]),  # notes
            ]) + ")")
            first = False
        print(";")


def mysql_quote(x):
    """Quote the string x using MySQL quoting rules. If x is the empty string,
    return "NULL". Probably not safe against maliciously formed strings, but
    our input is fixed and from a basically trustable source."""
    if not x:
        return "NULL"
    x = x.replace("\\", "\\\\")
    x = x.replace("'", "''")
    x = x.replace("\n", "\\n")
    return "'{}'".format(x)

if __name__ == "__main__":
    main()
