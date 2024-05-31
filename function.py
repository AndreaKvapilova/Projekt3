""" 
Engeto Online Python Akademie: Projekt3 - Elections Scraper 
author: Andrea Kvapilová 
email: a.ndrea@centrum.cz 
discord: andreakvapilova
"""
import re
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

def get_html_content(url:str):
    '''
    Function to download url and create beautiful soup.

    Args:
     url(str): string with url

    Returns:
    object from BeautifulSoup
    '''
    try:
        with requests.get(url) as response:
            response.raise_for_status()
            #source file splitting with Beautiful Soup
            soup = bs(response.text, features="html.parser")
        return soup
    except requests.RequestException as e:
        print("Unable to download website. Status code:{response.status_code}")
        return None
        
def create_bs_findall_list(soup,
                           element:str,
                           atribut_name:str,
                           atribut_value:str) -> list:
    '''
    The function creates from beautiful soup object a list with searched elements using attribut name.

    Args:
        soup(bs.element): BeautifulSoup object
        element (str): HTML element name (e.g. td, tr, a)
        atribut_name (str): atribut name (e.g. class, headers)
        atribut_value (str): atribut value (e.g. 'overlow_name', 't3sa1 t3sb1')
    
    Returns:
        list: List of matching elements
    '''
    try:
        list_bs = soup.find_all(element, attrs={atribut_name: atribut_value})
        return list_bs
    except ValueError as e:
        print(f"Error creating a list from Beautiful soup! {e}")
        return None

def get_text_from_soup(bs_list):
    '''
    The function gets the text from the Beautiful soup object.

    Args:
        bs_list (bs.element): Beautiful soup object
    
    Returns:
        list or single text depending on the number of bs elements in the list
    '''
    result = []

    if len(bs_list) == 1:
        return bs_list[0].get_text()
    else:
        result = [element.get_text() for element in bs_list]
        return result

def create_complete_url(base_url:str, attached_url:str) -> str:
    '''
    The function associates a base url address with a relative link

    Args:
        base_url (str): HTML address
        attached_url (str): relative link

    Returns:
        urljoin (str): absolute HTML address
    '''
    return urljoin(base_url, attached_url)

def process_municipality_soup(municipality_name, code, base_url, result_queue):
    '''
    The function generates from the Bs object search the names of the municipalities,
     their code and the ralative link to each municipality information for further webscraping
     (number of voters, envelopes, valid votes and the party names and the muber of votes they
      received in a given municipality).

    Args:
        municipality_name: Beautiful soup object
        code: Beautiful soup objects
        base_url: str
        result_queue: queue.Queue
    
    Return:
        municipality_record: list
    '''
    municipality_record = []
    location = municipality_name.get_text()
    code_location = code.get_text()
    relative_path = code.find('a')['href']
    complete_path = create_complete_url(base_url,relative_path)
    municipality_soup = get_html_content(complete_path)
    voters = create_bs_findall_list(municipality_soup, 'td', 'headers', 'sa2')
    text_voters = get_text_from_soup(voters)
    envelope = create_bs_findall_list(municipality_soup, 'td', 'headers', 'sa3')
    text_envelope = get_text_from_soup(envelope)
    valid_votes = create_bs_findall_list(municipality_soup, 'td', 'headers', 'sa6')
    text_valid = get_text_from_soup(valid_votes)
    party_name = create_bs_findall_list(municipality_soup, 'td', 'headers', re.compile(r't\d+sa1 t\d+sb2'))
    text_party_name = get_text_from_soup(party_name)
    party_value = create_bs_findall_list(municipality_soup, 'td', 'headers', re.compile(r't\d+sa2 t\d+sb3'))
    text_party_value = get_text_from_soup(party_value)

    #append to municipality record
    municipality_record.append(['code', code_location])
    municipality_record.append(['location', location])
    municipality_record.append(['registred voters', text_voters])
    municipality_record.append(['issued envelopes', text_envelope])
    municipality_record.append(['valid votes', text_valid])
    party = [list(pair) for pair in zip(text_party_name, text_party_value)]
    municipality_record += party
    result_queue.put(municipality_record)
