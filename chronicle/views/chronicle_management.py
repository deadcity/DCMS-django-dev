from django.views import generic

from chronicle.models import Chronicle, Game


class ChronicleDetailView (generic.DetailView):
    model = Chronicle
    template_name = 'chronicle/chronicle_detail.html'


class ChronicleListView (generic.ListView):
    model = Chronicle
    template_name = 'chronicle/chronicle_list.html'
