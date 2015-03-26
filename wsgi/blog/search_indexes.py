'''
Created on Sep 23, 2014
@author: hide
'''
import datetime
from haystack import indexes
from blog.models import Category


class CategoryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    category_title = indexes.CharField(model_attr='category_title')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Category

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
