# Written by Yuqian Gong 
# Type: Original 
# This part of code is to scrap data from a website called ethical consumer and
# we scraped company information from company pages that belong to the Fashion 
# category.
# Source: Shop Ethical 
# link: https://guide.ethical.org.au/guide/browse/categories/?cat=700&subcat=&ptype=
import requests
import bs4
import certifi
import re
import csv
import pandas as pd

session = requests.Session()

def get_company(myurl):
    '''
    Purpose:
    This function takes a url link and returns a soup object using beautifulsoup
    library.

    Inputs: 
        -myurl: A url string
    Outputs: 
        -soup: A beautifulsoup object ready for text parsing

    '''
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"}
    req = session.get(myurl, headers = headers)
    soup = bs4.BeautifulSoup(req.text, "html5lib")
    return soup



def get_company_info(soup, brand_filename):
    '''
    Purpose: 
    Scrap all the companies and their page links from an index page 
    and write them to csv files

    Inputs: 
        -soup: A beautifulsoup object 
        -brand_filename: A csv file to store company names their 
        url links
    '''
    brand_dict = dict()
    table = soup.find("table", attrs = {"id": "tablepress-1"})
    t_body = table.find("tbody")
    row_list = t_body.find_all("tr")
    for row in row_list:
        text = row.find("td", attrs = {"class":"column-1"}).text
        brand = re.search('([\w.&+\s]+)\xa0', text).group(1)
        link = row.find("td", attrs = {"class":"column-2"}).find("a")["href"]
        brand_dict[brand] = link

    with open(brand_filename, 'w') as f:
        c = csv.writer(f)
        for key, value in brand_dict.items():
            c.writerow([key, value])
        f.close()




def get_comp_table(soup):
    '''
    This function scrapped data from a company's information page,
    specifically including assessment evluations on this company in 
    five dimemsions as well as list of brands that belong to this 
    company. 

    Input: 
        -soup: A beautifulsoup object
    Output: 
        -a tuple: 
            rate: company's rating (denoted in color)
            comp_dict: a dictionary containing all assessment evaluations;
            the key is the issue name, and the value is a tuple of title
            and description.
            pro_list: A list of all the brands belonging to the company
            name: the name of the company
    '''
    comp_dict  = dict()
    pro_list = list()
    name = re.search("([\w.\s&+'-]+) |", soup.find("title").text).group(1)
    img_s = soup.find("td", text = "Rating").parent.find("img")["src"]
    rate = re.search("icon_([a-zA-Z]+).png", img_s).group(1)
    table = soup.find("div", attrs= {"class":"boxCompanyInfo"})
    div_list = table.find_all("div")
    len_div = len(div_list)
    table_pro = soup.find("table", attrs = {"class":"marginBottom"})
    if table_pro != None:
        a_list = table_pro.find("tr").find_all("a")
        for a in a_list:
            brand = a.previous_sibling.strip()
            catego = a.text.strip()
            one_product = ["product", brand, catego]
            pro_list.append(one_product)

    for i in range(0, len_div -1, 2):
        td_list = div_list[i].find_all("td")
        title = td_list[0].find("img")["title"]
        issue = td_list[1].text
        desc = div_list[i+1].text.strip("\n")
        comp_dict[issue] = [title, desc]
    
    return (rate, comp_dict, pro_list, name)



def write_comp_dict(info_tuple, filename):
    '''
    This function writes each company's information to a csv file 
    named by the company. 

    Inputs:
        -info_tuple: A tuple storing company information
        returned by the function get_comp_table
        -filename: A csv filename for a company's information to be
        written to.
    '''
    with open(filename, "w") as f:
        c = csv.writer(f)
        name = info_tuple[3]
        c.writerow([name])
        c.writerow([info_tuple[0]])
        for key, value in info_tuple[1].items():
            r = ["assess", key] +value
            c.writerow(r)
        for product in info_tuple[2]:
        	c.writerow(product)

        f.close()



company_code = set()
def create_brand_file(cate_filename):

'''
This function take in a csv file containing the links of 
all the company pages we want to scrap and scrap
from each link and write them to a corresponding csv file 
named by the company name:

Input:
    -cate_filname: A csv file contaning the urls of all companies.
'''
    f = pd.read_csv(cate_filename, names = ["brand", "link"])
    for i, row in f.iterrows():
        link = row["link"]
        code = re.search('company=([0-9]+)', link)
        if code not in company_code:
            company_code.add(code)
            soup = get_company(link)
            info_tuple = get_comp_table(soup)
            name = info_tuple[3]
            brand_filename = name + ".csv"
            write_comp_dict(info_tuple, brand_filename)


    








