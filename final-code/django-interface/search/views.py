#Written by Yuqian Gong

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django import forms
from .models import Rating, CompanyToBrand, Assessment, TransIndex, LabourRating, Evaluation
from django.db.models import Q 


class SearchForm(forms.Form):
    '''
    Purpose:
    This class is written to create a search form class to be displayed on the 
    homepage. I wrote this class in reference to a blogpost on rendering django forms
    and on Django documentation in creating forms.

    Type: Modified

    Reference:
    (1) How to Render Django Form Manually
        link: https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html?from=singlemessage&isappinstalled=0
    (2) Django documentation (Working with forms)
        link: https://docs.djangoproject.com/en/2.0/topics/forms/

    '''
    brand_name = forms.CharField(label = 'Brand name', 
        widget=forms.TextInput(
            attrs={
                'placeholder': '    Enter a brand name here',
                'size':90,
                'style': 'height:45px;'
            }
        ), max_length = 300, required = True)



    def clean(self):   
        brand_name = self.cleaned_data
        if not brand_name:
            raise forms.ValidationError('You have to enter a brand or company name')
        return brand_name


def search(request):
    '''
    Purpose: 
    This function is used to display the home search page if no user input is gathered. 
    If user input is collected, it will redirect a function called 'result'.
    
    Type: Modified 
    
    Reference: 
    (1) How to Render Django Form Manually
        link: https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html?from=singlemessage&isappinstalled=0
    (2) Python + Django page redirect
        link: https://stackoverflow.com/questions/523356/python-django-page-redirect
    '''
    template_name = 'search/search.html'
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            brand_name = form.cleaned_data["brand_name"]
            return redirect('result', brand_name)
    else:
        form = SearchForm()



    return render(request, template_name, {'form':form})


def result(request, brand_name):
    '''
    Purpose: 
    This function take key words from user inputs and search for any relevant brands or companies 
    from the database. If the input key word refers to a direct brand or company, then this function will 
    direct to the corresponding company page. Otherwise, it directs to a result page 
    which includes a list of available brands or company links are shown for users to choose from. 

    Type: Original
    '''
    key_word_list = brand_name.split()
    company_result= set()
    brand_result = set()
    context = {}
    company_id_set = set()
    for key_word in key_word_list: 
        result = Rating.objects.filter(company_name__icontains = key_word)
        company_result = company_result | set(result)
    for key_word in key_word_list:
        result = CompanyToBrand.objects.filter(brand_name__icontains = key_word)
        brand_result = brand_result | set(result)
    context["company_result"] = company_result 
    context["brand_result"] = brand_result
    for company in company_result:
        company_id_set.add(company.company_id)
    for brand in brand_result:
        company_id_set.add(brand.company_id)
    if len(company_id_set) == 1:
        company_id = company_id_set.pop()
        return redirect('detail', company_id)
    else:
        return render(request, 'search/result.html', context)


def detail(request, comp_id):
    '''
    Purpose: 
    This function takes a company id and render a html page containing 
    information about this company.

    The context to be passed to the html include the following variables:
        "Rating": The rating object of this company
        "brands": A dictionary with the brand name as the key and an information
        dictionary as its value. The value dictionary will contain 
        a brand's tranparency index objects and labour rating objects if exists.
        "envrionment": All environment assessment objects of this company 
        "business": All business ethics assessment objects of this company
        "social": All social ethics assessment objects of this company
        "animal": All animal treatment assessment objects of this company 
        "evluation": Any comment about living wages of this company (Would
        be an empty list if there is no comment)
        "information": All information objects of this company

    Type: Original
    '''
    template_name = 'search/detail.html'
    context = {}
    try:
        rating = Rating.objects.get(company_id = comp_id)

    except Rating.DoesNotExist:
        raise Http404("Question does not exist")

    context["rating"] = rating
    brands = CompanyToBrand.objects.filter(company_id = comp_id)
    brand_all = {}
    company_evaluation = []
    for brand in brands:
        brand_info = {} 
        brand_id = brand.brand_id
        trans_index = TransIndex.objects.filter(brand_id = brand_id + ".0")
        if len(trans_index) != 0:
            brand_info["trans_index"] =  trans_index[0]
        labour_rating = LabourRating.objects.filter(brand_id = brand_id + ".0")
        if len(labour_rating) != 0:
            brand_info["labour_rating"] = labour_rating[0]
        evaluation = Evaluation.objects.filter(brand_id = brand_id)
        if len(evaluation)  != 0:
            company_evaluation.append(evaluation[0])
        brand_all[brand] = brand_info
    
    if len(company_evaluation) == 0:
        context["evaluation"] = []
    else:
        context["evaluation"] = [company_evaluation[0]]



    context["brands"] = brand_all
    context["environment"] = Assessment.objects.filter(company_id = comp_id, aspect = "Environment")
    context["business"] = Assessment.objects.filter(company_id = comp_id, aspect = "Business Ethics")
    context["social"] = Assessment.objects.filter(company_id = comp_id, aspect = "Social")
    context["animal"] = Assessment.objects.filter(company_id = comp_id, aspect = "Animals")
    context["information"] = Assessment.objects.filter(company_id = comp_id, aspect = "Information")



    return render(request, template_name, context)





