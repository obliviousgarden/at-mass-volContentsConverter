# It is a tool to search the information of all elements.
# It is from International Atomic Energy Agency (IAEA) using Livechart Data Download API.
# The information includes:
# half life [s]
# main decay mode
# Q beta- [keV]
# Q alpha [keV]
# Q beta- n [keV]
# n separation [keV]
# p separation [keV]
# radius [fm]
# mass excess [keV]
# binding en. [keV]
# atomic mass [AMU]
# elec. quadrup. [barn]
# magn. dipole [nm]
# mean b- en. [keV]
# mean b+ en. [keV]
# 233U ther.cum.FY
# 235U ther.cum.FY
# 239PU ther.cum.FY
# ther. (n,g) cs [barn]
# capt. res. int. [barn]
# Refer to : https://www-nds.iaea.org/relnsd/vcharthtml/api_v0_guide.html#service
import requests


def livechart_csv_reader(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0"
    }
    response = requests.get(url,headers = headers)
    print("Status Code: " + str(response.status_code))
    print(response.content)

    content =response.content
    return content


if __name__ == "__main__":
    url_base = "https://nds.iaea.org/relnsd/v1/data?"
    url = url_base + "fields=ground_states&nuclides=all"
    url = "https://nds.iaea.org/relnsd/v1/data?fields=ground_states&nuclides=all"
    url = "https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=Co"
    content = livechart_csv_reader(url)
    print(content)