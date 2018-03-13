### This file is for data cleaning and preprocessing.

### The goal is to generate
### csv file from txt file with nice pandas formats for building databases.

### Without additional notes, the code is original or modified based
### on official documents of Pandas.

### coding: utf-8

import re
import csv


def common_cleaning(filename):
    '''
    Common function for every txt file preprocessing.
    '''
    ### use stackflows to help determine the encoding
    f = open(filename, 'r', encoding = 'utf-8-sig')

    data = f.read()
    f.close()

    temp = re.split('\n', data)
    clean = []
    for t in temp:
        clean += re.split('[ ][ ]+', t)

    return clean


### This section is for Slavery_Labour_2016
clean = common_cleaning('Slavery_Labour_2016.txt')

### Really special case to be treated
special = clean[202].split('* ')
del clean[202]
clean.insert(202, special[0])
clean.insert(203, special[1])

brand = [clean[n] for n in range(len(clean)) if n % 2 == 0]
rating = [clean[n] for n in range(len(clean)) if n % 2 == 1]
result = list(map(lambda b, r : [b, r], brand, rating))

with open('Slavery_Labour_2016.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['brand', 'ranking'])
    writer.writerows(result)

f.close()


### This section is for Increase_wages
clean = common_cleaning('Increase_wages.txt')

result = [[c] for c in clean]

with open('Increase_wages.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['brand'])
    writer.writerows(result)

f.close()


### This section is for Slavery_Labour_2017
clean = common_cleaning('Slavery_Labour_2017.txt')

brand = [clean[n] for n in range(len(clean)) if n % 2 == 0]
rating = [clean[n] for n in range(len(clean)) if n % 2 == 1]
result = list(map(lambda b, r : [b, r], brand, rating))

with open('Slavery_Labour_2017.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['brand', 'ranking'])
    writer.writerows(result)

f.close()


### This section is for Transparency_index
clean = common_cleaning('Transparency_index.txt')
clean = [c for c in clean if c != '']

parent = []
child = []

### Really special case to be treated
n0 = clean.index('LVMH')
child0 = (clean[n0 + 1][2:] + clean[n0 + 2]).split(',')
child0 = [c.strip() for c in child0]

child += child0
parent += ['LVMH'] * len(child0)

del clean[(n0 + 1):(n0 + 3)]

n1 = clean.index('Arcadia Group')
child1 = (clean[n1 + 1][2:] + clean[n1 + 2]).split(',')
child1 = [c.strip() for c in child1]

child += child1
parent += ['Arcadia Group']* len(child1)

del clean[(n1 + 1):(n1 + 3)]

for c in clean:
    ### Get rid of special symbols
    if '*' in c:
        n_c = clean.index(c) - 1
        if '\x07' in c:
            child_c = c[2:].split(',')
        else:
            child_c = c[1:].split(',')
        child_c = [cc.strip() for cc in child_c]
        child += child_c
        parent += [clean[n_c]] * len(child_c)
        del clean[(n_c + 1)]


result_pc = list(map(lambda p, c : [p, c], parent, child))

with open('Parent_child.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['parent', 'child'])
    writer.writerows(result_pc)

f.close()

component = []

for i in range(len(clean)):
    if i % 7 == 0:
        component += [clean[i: (i + 7)]]

with open('Transparency_index.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['brand', 'policy', 'tracking', 'social', \
                     'engage', 'governance', 'score'])
    writer.writerows(component)

f.close()



### This section is for Brand_index
clean = common_cleaning('Brand_index.txt')
clean = [c for c in clean if c != '']

parent = [clean[n] for n in range(len(clean)) if n % 3 == 0]
brand = [clean[n] for n in range(len(clean)) if n % 3 == 1]
rating = [clean[n] for n in range(len(clean)) if n % 3 == 2]
result = list(map(lambda p, b, r : [p, b, r], parent, brand, rating))

with open('Brand_index.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['parent', 'brand', 'rating'])
    writer.writerows(result)

f.close()


### This section is for TailoredWagesEurope-Web-Pages
f = open('TailoredWagesEurope-Web-Pages.txt', 'r', encoding = 'utf-8-sig')
data = f.read()
f.close()

### This regular expresssion is inspired by stackflows posts
brands = re.findall("([^.]\n*?Brands:[\S,\n ]*[\n ])(WORKER EMPOWERMENT)", str(data))

brand_result = []
for b in brands:
    test = b[0].splitlines()
    test = [t.split() for t in test if len(t) >= 2]
    test = [' '.join(t) for t in test if t not in [[], ["INFO"]]]
    test = ' '.join(test)

    if "\x07" in test:
        test.replace("\x07 lease", " Please")
        test = test[:test.find("\x07")]
    if "Please" in test:
        test = test[:test.find("P")]
    brand_result += [test]


### This regular expression used help of TA Nick and stackflows posts
what_we_say = re.findall("([^.]*?What we say([^.]*\.)*?\n\n)", str(data))

what_result = []
for w in what_we_say:
    test = w[0].splitlines()
    test = [t.split() for t in test]
    test = [' '.join(t) for t in test if t not in [[], ['”'], ['’”']]]
    test = ' '.join(test)
    test = test[test.find("What we say"):test.find("Commitment and practices:")]\
                + "."
    what_result += [test]

### Special cases need to be overwriten
what_result[22] ='''
What we say: This company did not respond to our request for information and
makes little data available on its website about labour rights or living wages.
Charitable work to patch up holes caused by the extreme poverty that exists in
the fashion industry is not the kind of response that is needed from global
buyers. Help for education and healthcare projects in Bangladesh is all very
well, but only in addition to serious engagement in improving low wages for
workers. The need to pay a living wage is the primary responsibility of global
buyers, and information on how Kik is progressing towards this goal is the sort
of thing we would hope to read on the ‘responsibility’ page of its website in
the future. The fact that there is no information available about work to
increase wages currently leads us to assume the worst: that none is being
undertaken.
'''

what_result[44] ='''
What we say: Tesco’s approach of aiming to pay more than the minimum wage and
above average for the industry is a far cry from a living-wage plan. Work on
improving factory efficiency will only improve wages so far. Bigger thinking is
needed from a buyer with this sort of market power.
'''

with open('What_we_say.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['Brands', 'what_we_say'])
    writer.writerows(zip(brand_result, what_result))
f.close()


### This section is for processing web scrawling data
import os
import pandas as pd
### This os operation is modified from stackflows posts
path = "C:\\Users\\liaoa\\Desktop\\project\\company information"
file_list = os.listdir(path)

assess = pd.DataFrame()
rating = pd.DataFrame()
product = pd.DataFrame()

### Somehow the web scrawling data format is messy, so I used try-except to
### treat every case respectively.
for k in range(len(file_list)):
    f = path + "\\" + file_list[k]

    try:
        part_1 = pd.read_csv(f, header = None)
    except:
        part_1 = pd.read_csv(f, header = None, error_bad_lines = False)
        part_2 = pd.read_csv(f, header = None, skiprows = 2)
        rating = rating.append(part_1[0])
        part_2["brand"] = part_1[0][0]

        try:
            part_2.columns = ["type", "abstract", "temp", "detail", "brand"]
        except:
            part_2.columns = ["type", "abstract", "aspect", "brand"]
            product = product.append(part_2)
        else:

            try:
                part_2["aspect"], part_2['post_nega'] = part_2["temp"].str.\
                split(":", 1).str
            except:
                part_2["aspect"] = part_2["temp"]
                part_2 = part_2.drop(columns = ["temp","detail"])
                product = product.append(part_2[part_2["type"] == "product"])
            else:
                part_2 = part_2.drop(columns = ["temp"])
                assess = assess.append(part_2[part_2["type"] == "assess"])
                part_2 =  part_2.drop(columns = ["detail", "post_nega"])
                product = product.append(part_2[part_2["type"] == "product"])

    else:
        rating = rating.append(part_1[0][0:2])
        brand = part_1[0][0]
        part_1 = part_1[:][2:]

        part_1["brand"] = brand
        part_1.columns = ["type", "abstract", "temp", "detail", "brand"]
        part_1["aspect"], part_1['post_nega'] = part_1["temp"].\
            str.split(":", 1).str
        part_1 = part_1.drop(columns = ["temp"])

        assess = assess.append(part_1[part_1["type"] == "assess"])
        part_1 =  part_1.drop(columns = ["detail", "post_nega"])
        product = product.append(part_1[part_1["type"] == "product"])


### This subsection is for generating rating csv
rating.columns = ["company_name", "rating"]
new_index = range(0, len(rating))
rating.index = new_index
color_to_rating = {"green": "A", "ltgreen": "B", "yellow": "C", "orange": "D",\
    "red": "F", "grey": "Not rated" }

### This map function is modified from stackflows posts
rating["rating"] = rating["rating"].map(color_to_rating)

for r in range(len(rating)):
    row = rating.iloc[r]
    s = row["company_name"]

    if s[-1] == " ":
        s = s[:-1]
    s = s.replace(" Australia", "")
    row["company_name"] = s[:1].upper() + s[1:]

rating.reset_index(level = 0, inplace = True)
rating = rating.rename(columns = {"index":"company_id"})

company_to_id = {}
for r in range(len(rating)):
    row = rating.iloc[r]
    company_to_id[row["company_name"]] = row["company_id"]

rating.to_csv("rating.csv", index = False)


### This subsection is for generating product csv
product = product.drop(columns = ["type", "aspect"])
product = product.rename(columns = {"abstract":"brand_name", \
    "brand": "company_name"})

for p in range(len(product)):
    row = product.iloc[p]
    s = row["company_name"]

    if s[-1] == " ":
        s = s[:-1]
    s = s.replace(" Australia", "")
    row["company_name"] = s[:1].upper() + s[1:]

    if pd.isnull(row["brand_name"]):
        row["brand_name"] = row["company_name"]

product.drop_duplicates(inplace = True)

new_index = range(0, len(product))
product.index = new_index
product.reset_index(level = 0, inplace = True)
product = product.rename(columns = {"index":"brand_id"})

brand_to_id = {}
for p in range(len(product)):
    row = product.iloc[p]
    brand_to_id[row["brand_name"]] = row["brand_id"]

product["company_id"] = product["company_name"].map(company_to_id)
product.to_csv("company_to_brand.csv", index = False)


### This subsection is for generating assess csv
assess = assess.rename(columns = {"brand": "company_name"})

for a in range(len(assess)):
    row = assess.iloc[a]
    s = row["company_name"]

    if s[-1] == " ":
        s = s[:-1]
    s = s.replace(" Australia", "")
    row["company_name"] = s[:1].upper() + s[1:]

assess.reset_index(level = 0, inplace = True)
assess = assess.drop(columns = ["type", "index"])
assess["company_id"] = assess["company_name"].map(company_to_id)
assess.to_csv("assessment.csv", index = False)


### This section is for record_linkage
import jellyfish
labour_2016 = pd.read_csv("Slavery_Labour_2016.csv", encoding = "latin1")
labour_2016 = labour_2016.rename(columns = {"brand": "brand_name", \
    "ranking": "labour_rating"})


for l in range(len(labour_2016)):
    row = labour_2016.iloc[l]
    labour_2016.at[l, "brand_name"] = row["brand_name"].replace("*", "")

labour_2016["brand_id"] = labour_2016["brand_name"].map(brand_to_id)


for l in range(len(labour_2016)):
    row = labour_2016.iloc[l]
    if pd.isnull(row["brand_id"]):
        target = row["brand_name"].lower()
        score_max = 0
        for key, value in brand_to_id.items():
            score = jellyfish.jaro_winkler(target, str(key).lower())
            if score > score_max:
                score_max = score
                score_name = key
                score_id = value
        if score_max > 0.9:
            labour_2016.at[l, "brand_name"] = score_name
            labour_2016.at[l, "brand_id"] = score_id
            print(target, score_name, score_max)

labour_2016.to_csv("labour_rating.csv", index = False)


### This section is for adding brand_id to Transparency_index
trans = pd.read_csv("Transparency_index.csv")
trans["brand_id"] = trans["brand"].map(brand_to_id)
trans.to_csv("trans_index.csv", index = False)


### This section is for adding brand_id to what_we_say
what = pd.read_csv("what_we_say.csv", encoding = "latin1")
what.columns = ["brands", "say"]

evals = pd.DataFrame(columns = ["brand_name", "eval"])

i = 0
for w in range(len(what)):
    row = what.iloc[w]
    temp_brand = row["brands"].replace("Brands: ", "")
    temp_say = row["say"].replace("What we say: ", "")
    brand_list = temp_brand.split(",")

    for b in brand_list:
        brand = b.strip()
        evals.loc[i] = [brand, temp_say]
        i += 1

evals["brand_id"] = evals["brand_name"].map(brand_to_id)

for e in range(len(evals)):
    row = evals.iloc[e]
    if pd.isnull(row["brand_id"]):
        target = row["brand_name"].lower()
        score_max = 0
        for key, value in brand_to_id.items():
            score = jellyfish.jaro_winkler(target, str(key).lower())
            if score > score_max:
                score_max = score
                score_name = key
                score_id = value
        if score_max > 0.9:
            evals.at[l, "brand_name"] = score_name
            evals.at[l, "brand_id"] = score_id
evals.to_csv("evaluation.csv", index = False)


### This section is an attempt to generate word-word_cloud
f = open('report-factory-pledge.txt', 'r', encoding = 'utf-8-sig')
data = f.read()
f.close()

import re
string = re.findall("[A-Za-z ]+", data)

stop = set(['a', 'also', 'an', 'and', 'are', 'as', 'at', 'be','but', 'by',
            'for', 'from','how', 'i', 'ii', 'iii', 'in', 'include', 'is',
            'not', 'of', 'on', 'or', 's', 'so', 'such', 'that', 'the', 'their',
            'this', 'through', 'to', 'we', 'were', 'which', 'will', 'with',
            'yet', 'need', 'then', 'them', 'what', 'about', 'some', 'among',
            'those'])


clean = []
for s in string:
    s = s.lower().split( )
    clean += [word for word in s if word not in stop and len(word) > 3]

import random
index = random.sample(range(1, len(clean)), 2700)

with open('word_cloud.txt', 'w') as f:
    for i in index:
        f.write(clean[i] + " ")
f.close()
