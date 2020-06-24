
import requests
from bs4 import BeautifulSoup
import re


def calc(regex, text):
    """
    Makes use of regex to get a search pattern in a text

    Args:
        regex: re pattern object
        text: A text, an iterable et.c

    Returns: str

    """

    matches = re.search(regex, text)
    if matches is None:
        return
    return matches.group()


def get_review(URL):
    """

    It takes an Airbnb user profile link and returns the number of reviews

    Args:
        URL: HTTP Link e.g 'https://www.airbnb.com/users/show/99824610'

    Returns: A value, string

    """
    try:
        URL
    except HTTPError as e:
        print(e)
    except URLError:
        print('The server could not be found')
    else:
        driver = requests.get(URL)
        html = driver.text
        soup = BeautifulSoup(html, 'html.parser')
        results = soup.findAll('div', {'class': "_czm8crp"})

        new_results = calc(r'(\d+ reviews|\d+ review)+', str(results))

        if new_results is None:
            return 0

        answer = calc(r'\d+', new_results)
        return answer
        # return results[1].text[:-7]


if __name__ == '__main__':
    link = 'https://www.airbnb.com/users/show/99824610'
    print(get_review(link))

# results = soup.find(class_="_1ekkhy94")
# print(results.text)
