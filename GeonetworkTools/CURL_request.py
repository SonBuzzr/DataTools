import requests
from bs4 import BeautifulSoup


def get_APA_style(link):
    headers = {
        'Accept': 'text/x-bibliography; style=apa',
    }

    response = requests.get(link, headers=headers)
    # print(response.text)
    soup = BeautifulSoup(response.text, 'lxml')

    soup.i.unwrap()
    return soup.text


value = get_APA_style("https://doi.org/10.26066/rds.36029")
print(value)