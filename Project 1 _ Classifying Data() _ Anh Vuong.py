# Represent the data as a string
lobbyist_contributions_string = '''
Committee_Id	Committee_Name	Link_Image	\
Committee_Election_State	Committee_Election_District	Report_Type	Receipt_Date\
Coverage_Start_Date	Coverage_End_Date	Quarterly_Contribution	Semi_Annual_Contribution\

C00010603	DNC SERVICES CORP / DEMOCRATIC NATIONAL COMMITTEE	http://docquery.fec.gov/cgi-bin/fecimg/?_20200820926\
6412285+0   AUGUST MONTHLY	20-Aug-20	1-Jul-20	31-Jul-20	57935.95	0\
C00000935	DCCC	http://docquery.fec.gov/cgi-bin/fecimg/?_202007209250423730+0\
MONTHLY SEMI-ANNUAL (MY)	20-Jul-20	1-Jun-20	30-Jun-20	0	1069200\
C00010603	DNC SERVICES CORP / DEMOCRATIC NATIONAL COMMITTEE	http://docquery.fec.gov/cgi-bin/fecimg/?_2020072092606\
67327+0			JULY MONTHLY / SEMI-ANNUAL	20-Jul-20	1-Jan-20	30-Jun-20	172250	304655\
C00580100	DONALD J. TRUMP FOR PRESIDENT, INC.	http://docquery.fec.gov/cgi-bin/fecimg/?_202007209260156160+0\
JULY MONTHLY / SEMI-ANNUAL	20-Jul-20	1-Jun-20	30-Jun-20	19000	35500\
C00000935	DCCC	http://docquery.fec.gov/cgi-bin/fecimg/?_202007209250421233+0\
FEBRUARY MONTHLY	20-Jul-20	1-Jan-20	31-Jan-20	378800	0\
C00000935	DCCC	http://docquery.fec.gov/cgi-bin/fecimg/?_202007209250421616+0\
MARCH MONTHLY	20-Jul-20	1-Feb-20	29-Feb-20	336100	0\
C00743393	HILL FOR CONGRESS	http://docquery.fec.gov/cgi-bin/fecimg/?_202007179250376151+0\
JULY QUARTERLY / SEMI-ANNUAL	17-Jul-20	1-Jan-20	30-Jun-20	35973	35973\
C00618389	TRUMP VICTORY	http://docquery.fec.gov/cgi-bin/fecimg/?_202007179250397424+0\
QUARTERLY YEAR END / SEMI-ANN	17-Jul-20	1-Oct-19	31-Dec-19	1512592.61	2104626.26\
C00748178	VENA ALLIANCE TRIPLANETORIUM RELIGIOUS GLOBAL COUNTRY GOVERNMENT POLITICAL PARTY\
http://docquery.fec.gov/cgi-bin/fecimg/?_202007270300331831+0			JULY QUARTERLY	16-Jul-20\
15-Apr-20	15-Jul-20	0	0\

Source:https://www.fec.gov/data/browse-data/?tab=raising
'''
print(lobbyist_contributions_string)
print(type(lobbyist_contributions_string))

# Represent the data as a list of Tuple
list_of_tuple = [('C00010603', 'DNC SERVICES CORP / DEMOCRATIC NATIONAL COMMITTEE', 57935.95, 0),
                 ('C00000935', 'DCCC', 0, 1069200),
                 ('C00010603', 'DNC SERVICES CORP / DEMOCRATIC NATIONAL COMMITTEE', 172250, 304655),
                 ('C00580100', 'DONALD J. TRUMP FOR PRESIDENT, INC.', 19000, 35500),
                 ('C00000935', 'DCCC', 378800, 0),
                 ('C00000935', 'DCCC', 336100, 0),
                 ('C00743393', 'HILL FOR CONGRESS', 35973, 35973)
                 ]

print(list_of_tuple)
for i in list_of_tuple:
    print(i)


# Represent the data as a custom class

class Contribution:
    def __init__(self, committee_id: str, quarterly_contribution: int):
        self.id = committee_id
        self.quarter = quarterly_contribution


lobbyist_contribution = Contribution('C00743393', 35973)
print("Committee ID is: " + lobbyist_contribution.id)
print("Committee ID - ", lobbyist_contribution.id, " has ",
      str(lobbyist_contribution.quarter))
