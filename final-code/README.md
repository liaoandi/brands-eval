## (CAPP 30122)Final Group Project on Ethical Consumerism
--------------------------------------------------------

**Name:**capp-project  
**Members:** Yuqian Gong, Andi Liao & Xiuyuan Zhang  
**Group Git Repo:** https://github.com/liaoandi/brands-eval

## Project Objective 
----------------------------------------------
Our project is created to provide a user-friendly web application where users can search for a fashion clothing brand and get feedback on this brand and its mother company's ethical practice conduct evaluations from various third-party reports and agencies. The term "ethical" here broadly include the following aspects: environment, workers' right, handling and sourcing of animal product, policy transparency, and commitment to promote positive social changes.

## Instruction for Running Project
----------------------------------------------
Language used: Python3, JavaScript, HTML
Package needed to run the project: Django (2.0.1), pandas(0.22.0), jellyfish (0.5.6), BeautifulSoup(), 
Built-in Modules imported to run python3 code: csv, re, os 

To get our final code, please run the following git command in the command line:  
`$ git clone https://github.com/liaoandi/brands-eval.git`  


To access our web application, please make sure you are in the correct directory,then enter in the command line:
` $ cd brand-eval/final-code/django-interface`
` $ python3 manage.py runserver 9999`  

Then you can open a browser, and put in your address: `127.0.0.1:9999/search/`

**Suggested inputs:**  
	1. (1) h&m  
	2. (2) x  
	3. (3) nike   

The above suggested inputs covers three scenarios, where (1) is when a user knows exactly the brand she wants to look up, and we have the information for the brand. The user will be led to the result page directly. For (2), it is the case that perhaps the user does not remember the entire brand name, we handle this kind of search by taking user input and direct them to a page where they are given suggested brands that starts with their input letters. Since we have data for both brands and their mother companies, we present suggestions to both categories. In the case of (3), if a brand from user inputs does not match anything we have from our database, we return the message to inform the user that we currently do not have this information.

## Code Structure & Task Division
-----------------------------------------------
data 
1. data source/ cleaning
The data of our projet comes from two parts, the first part comes from web crawling, and the second part comes from pdf reports.

1.1 Web Crawling
We observed the website structure of Shop Ethical, and then used request and beautifulsoup to download all the company tables under "clothes" category.
We didn't take extra protection measures, such as, setting waiting time between visiting different companies, as Shop Ethical is a realtively small website.

1.2 pdf reports
To deal with pdf reports, we first converted them into unstructured txt data, and then using pandas, regular expression and helper function to extract the 
information from txt files. Then we reorganized the information into pandas dataframe.

2. data merging
As we collected data from multiple data sources, we needed to connect all of them in some way to make full use of all the data. Therefore, we chose to give
priority to web crawling data and label companies and brands using company_id and brand_id as unique idientifiers if they appear in the web crawling data.
Then we used map function to distibute ids for companies and brands from other sources, which works for companies and brands have the exactly same names.

For those companies and brands have similiar but not the same names, we utilized jellyfish package to calculate the similarity score between them. And, after several trials, we set the threshold to be 0.9, and set the value of companiy_id and brand_id to their most similar counterparts.

After completing all the matches, we outputed the pandas dataframe into csv files, which were ready for database input.


Django

1. Database Build_up
After we failed to replace the default with imported database(we posted this question on piazza but didn't figure out in the end), we switched to write six model classes(one for each of our data tables). 
These models are:
     (1)Rating: contain a company's overall rating information
     (2)TransIndex: contain a brand's transparency score information it has 
     (3)LabourRating: contain rating on a brand's treatment to labour workers 
     (4)Evaluation: contain evaluation on brand's attitudes and actions in improving living wages
     (5)CompanyToBrand: a table linking all brands to their mother companies
     (6)Assessment: Assessment on five dimensions including 'Eco-friendly', 'Treatment of Workers', 'Policy Ethics', 'Treatment of Animals', 'Other Information'
After creating empty tables, we import our data row by row in shell through a for loop(We foresee the problem with this method if we have large datasets)

2. Create URL paths and views functions
We created the following three types of URL:
    (1) Suffix is '/search': The main search page, the function in view is 'search' and it directs to the result function. 
    (2) Suffix is '^result/(?P<brand_name>\w+?)/$': The result page created based on user inputs. The function in view is 'result'. 
    (3) Suffix is 'company/<int:comp_id>/': This is the url to every company's information page. The corresponding function in view is 'detail'

If there is only one brand or company result relevant to a user's inputs, then our function will direct him or her to that specific company page. If there is more than one brand or companies, we will direct them to the result page where users can choose which specific brand or company they are interested in. Each brand will link to its parent company's page.

3. Website design and layouts 
We desinged three html files:
(1) search.html: This is the search homepage. 
(2) detail.html: This is the detailed information page for each company. 
(3) result.html: This is the result page to display all relevant brands or companies based on user inputs.

The codes in the three html files are mainly original. We modified highcharts demo templates and used W3School fonts to provide better visualization. 


Andi Liao - (Backend Data Collection) Data Processing
Yuqian Gong - (Intermediate Django Structure) Data Scraping, Django views and classes, HTML, JavaScript Highchart
Xiuyuan Zhang - (Frontend Design and Integration)Django templates

## External Reference
-----------------------------------------------
**Data Sources:**  
https://www.ethical.org.au/3.4.2/  
https://www.tearfund.org.nz/getmedia/135135c5-9701-4245-964b-e50864170bff/EthicalFashionReport_2017.pdf.aspx  
http://fashionrevolution.org/wp-content/uploads/2016/04/FR_FashionTransparencyIndex.pdf  
 
**Main Code Sources:**  
https://www.w3schools.com/  
https://www.highcharts.com/

We have further included detailed documentation listing the specific reference we used in each .py, .html, or .js files. 
