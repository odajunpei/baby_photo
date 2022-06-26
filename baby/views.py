from django.views.generic import ListView

from .models import Baby

class BabyListView(ListView):
  model = Baby