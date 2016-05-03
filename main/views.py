from django.views.generic.base import TemplateView

# My Imports
from main.models import WDMCity, WDMCityMap, WDMCityMapItemType
from main.engine import map_data, initializeRandomMap, UserCityMap

# Create your views here.


class IndexView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        initializeRandomMap(20, 20)
        user_map = UserCityMap(20, 20)
        context = super(IndexView, self).get_context_data(**kwargs)
        context['map_data'] = [[y for y in x.itervalues()] for x in map_data.itervalues()]
        context['user_map'] = user_map.citymap
        context['user_map_inf'] = user_map.citymapinf
        import ipdb; ipdb.set_trace()
        return context

index = IndexView.as_view()
