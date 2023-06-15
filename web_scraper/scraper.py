import requests
from  bs4 import BeautifulSoup


URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    all_paragraphs = soup.find_all('p')

    paragraphs_that_contain_citations = ''
    for paragraph in all_paragraphs:
        citations = paragraph.find_all('sup',class_='noprint Inline-Template Template-Fact')
        if citations :
            paragraphs_that_contain_citations += paragraph.text

    return paragraphs_that_contain_citations.count('citation needed')



def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    all_paragraphs = soup.find_all('p')

    list_of_paragraphs_that_contain_citations = []
    for paragraph in all_paragraphs:
        citations = paragraph.find_all('sup',class_='noprint Inline-Template Template-Fact')
        if citations :
            list_of_paragraphs_that_contain_citations.append(paragraph.text)

    return list_of_paragraphs_that_contain_citations
        


print(get_citations_needed_count(URL))
print(get_citations_needed_report(URL))