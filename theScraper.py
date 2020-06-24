
import requests
from bs4 import BeautifulSoup
import re


def sel_driver(link):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    options = Options()
    # change to chrome path on your device
    options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

    options.headless = True

    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    path = r"C:\Users\Iyanu\Documents\chromedriver_win32_83\chromedriver.exe"
    # Change path to chromedriver location on your device, to enable selenium webdriver
    driver = webdriver.Chrome(executable_path=path, options=options)

    driver.get(link)
    html = driver.page_source
    return html


def crawler(results):

    """

    Args:
        results: a Tag object

    Returns: The Link of a specific User based on the area

    """

    df = set()
    for tags in results.find_next_siblings('div'):
        each_link = tags.find_next('a').attrs['href']
        # print(each_link)
        while True:
            # new_page = sel_driver("https://www.airbnb.com" + str(each_link))
            new_page = requests.get("https://www.airbnb.com" + str(each_link)).text
            new_bs4 = BeautifulSoup(new_page, 'html.parser')

            answer = new_bs4.find('a', {'href': re.compile(r'/users/show/\d+')})
            # print(answer)
            if answer is not None:
                answer = answer.attrs['href']
                break
        if str(answer).startswith('/users'):
            link = "https://www.airbnb.com" + str(answer)
            df.add(f'{link}')
    return df


def pageCrawler(URL):

    """
    Returns the link of all the User's profile in a page

    """

    try:
        base = 'https://www.airbnb.com'
        search = base + URL
    except HTTPError as e:
        print(e)
    except URLError:
        print('The server could not be found')
    else:
        while True:
            page = requests.get(search)
            # print(page.raise_for_status())

            soup = BeautifulSoup(page.text, 'html.parser')

            result = soup.find('div', {'class': "_8ssblpx"})
            if result is not None:
                df = crawler(result)
                break
        return df


def eachPageLink(URL):

    """
    Returns the Sections of a Page

    """
    try:
        base = 'https://www.airbnb.com'
        search = base + URL
    except HTTPError as e:
        print(e)
    except URLError:
        print('The server could not be found')
    else:
        page_df = pageCrawler(URL)
        page = requests.get(search)
        # print(page.raise_for_status())

        soup = BeautifulSoup(page.text, 'html.parser')
        answer = soup.find('div', {"class": "_115zncnj"}).find_parent().find_next('a').attrs['href']

        # print(answer)
        return page_df, answer


if __name__ == '__main__':
    the_link = '/s/Melbourne--Victoria--Australia/homes'
    for i in range(15):
        print(the_link)
        details, the_link = eachPageLink(the_link)


