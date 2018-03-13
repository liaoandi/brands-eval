from django.db import models

# Create your models here.
class Rating(models.Model):
    '''
    This class is for overall Rating for all the companies.
    Variables include:
    - company_id: int
    - companu_name: str
    - rating: str
    '''
    company_id = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'rating'

  


class TransIndex(models.Model):
    '''
    This class is for Transparency Index for brands.
    Variables include:
    - brand: str
    - policy: int
    - tracking: int
    - social: int
    - engage: int
    - governance: int
    - score: int
    - brand_id: int
    '''
    brand = models.TextField(blank=True, null=True)
    policy = models.TextField(blank=True, null=True)
    tracking = models.TextField(blank=True, null=True)
    social = models.TextField(blank=True, null=True)
    engage = models.TextField(blank=True, null=True)
    governance = models.TextField(blank=True, null=True)
    score = models.TextField(blank=True, null=True)
    brand_id = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'trans_index'


class LabourRating(models.Model):
    '''
    This class is for labour Rating for all the brands.
    Variables include:
    - brand_name: str
    - labour_rating: str
    - brand_id: int
    '''
    brand_name = models.TextField(blank=True, null=True)
    labour_rating = models.TextField(blank=True, null=True)
    brand_id = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'labour_rating'




class Evaluation(models.Model):
    '''
    This class is for Evaluation for brands.
    Variables include:
    - brand_name: str
    - evaluation: int
    - brand_id: int
    '''
    brand_name = models.TextField(blank=True, null=True)
    evaluation = models.TextField(blank=True, null=True)
    brand_id = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'evaluation'



class CompanyToBrand(models.Model):
    '''
    This class is linking the brand to their mother companies.
    Variables include:
    - brand_id: int
    - brand_name: int
    - company_name: str
    - company_id = models.TextField(blank=True, null=True)
    '''
    brand_id = models.TextField(blank=True, null=True)
    brand_name = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    company_id = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'company_to_brand'

   


class Assessment(models.Model):
    '''
    This class is for assessment of companies.
    - abstract: str
    - detail: str
    - company_name: str
    - aspect: str
    - post_nega: str
    - company_id: int
    '''
    abstract = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    aspect = models.TextField(blank=True, null=True)
    post_nega = models.TextField(blank=True, null=True)
    company_id = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'assessment'






