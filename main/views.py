from django.views.generic.base import TemplateView

# My Imports
from main.models import WDMCity, WDMCityMap, WDMCityMapItemType
from main.engine import map_data, initializeRandomMap

# Create your views here.


class IndexView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        initializeRandomMap(40, 40)
        context = super(IndexView, self).get_context_data(**kwargs)
        context['map_data'] = map_data
        return context


index = IndexView.as_view()
