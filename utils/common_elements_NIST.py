# It is a tool to search the information of all elements.
# Refer to : https://www.nist.gov/pml/atomic-weights-and-isotopic-compositions-relative-atomic-masses
import requests,re
from bs4 import BeautifulSoup
from requests.exceptions import Timeout


def search_atomic_mass(element_str:str)->float:
    url = "https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele="+element_str
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0"
    }
    #超时重发，上限3次
    retries = 0
    while retries < 3:
        try:
            response = requests.get(url,headers = headers)
            response.raise_for_status()
            break
        except Timeout:
            print('Time out, retrying...')
            retries += 1
    if retries == 3:
        return 0.01
    else:
        soup = BeautifulSoup(response.content, 'html.parser')
        atomic_mass_tag_list = soup.find_all('td')
        if atomic_mass_tag_list == []:
            return 0.01
        else:
            atomic_mass_withspace = re.sub(r'\([^)]*\)', '', atomic_mass_tag_list[11].text)
            atomic_mass = atomic_mass_withspace.replace(' ', '').replace(' ','')
            if atomic_mass.startswith("[") and atomic_mass.endswith("]"):
                atomic_mass = atomic_mass[1:-1].split(",")[0]
            return float(atomic_mass)


if __name__ == "__main__":
    content = search_atomic_mass('Fe')
    print(content)