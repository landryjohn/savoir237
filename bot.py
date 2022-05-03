from lib2to3.refactor import get_all_fix_names
import requests

from bs4 import BeautifulSoup

BASE_URL = "https://epreuvesetcorriges.com"

def get_cameroon_BAC_tests() -> list : 
    # Number of pages for BAC Exam
    pages = 14
    # Number of test per pages 
    tests_per_pages = 10
    # Principal URI form cameroon BAC Tests
    URI = f"{BASE_URL}/categories/cameroun/examens/bac" 
    # Declare an empty list of tests 
    tests = []
    # Go trough all pages (14 pages)
    for page in range(0, (pages+1)*tests_per_pages, 10) : 
        print(f"--> [Pending] Reading page ... {page/10}")
        # Request the page
        response = requests.get(f"{URI}?start={page}")
        # initialize the soup object with HTML parser
        soup = BeautifulSoup(response.content, 'html.parser')
        # Select all tests link by class name
        tests_tag = soup.select(".edocman-document-title > a")
        for test in tests_tag : 
            print(f"{' '.join(test.text.split())} readed !")
            tests += [{'name': " ".join(test.text.split()), 'link': f"{BASE_URL}{test['href']}/download"}]
        print(f"--> [ok] Finished reading page {page/10}")

    return tests

if __name__ == "__main__" : 
    tests = get_cameroon_BAC_tests()
    with open('epreuves-bac-cameroun', 'w', encoding='utf-8') as f :
        for test in tests : 
            f.write(f"-{test['name']} : {test['link']}\n")
