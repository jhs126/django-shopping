# coding=utf-8
from haystack import indexes
from .models import GoodsInfo



class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):#获取某个对象
        return GoodsInfo

    def index_queryset(self, using=None):#基于哪些数据进行检索
        return self.get_model().objects.all()