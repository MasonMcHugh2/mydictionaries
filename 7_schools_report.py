"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 50%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""

import json

infile = open('school_data.json', 'r')

list_of_schools = json.load(infile)

#print(type(list_of_schools))

conference_schools = [372,108,107,130]

for row in list_of_schools:
    if row['NCAA']['NAIA conference number football (IC2020)'] in conference_schools:
        if row['Graduation rate  women (DRVGR2020)'] > 50:
            print(f"University: {row['instnm']}")
            print(f"Graduation Rate for Women: {row['Graduation rate  women (DRVGR2020)']}%")
            print(f"")
            print()
            print()

for row in list_of_schools:
        if  row['NCAA']['NAIA conference number football (IC2020)'] in conference_schools:
            if row['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)']:
                if row['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'] > 50000:
                    print(f"University: {row['instnm']}")
                    print(f"Total price for in-state students living off campus : ${row['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)']:,.2f}")
                    print()
                    print()