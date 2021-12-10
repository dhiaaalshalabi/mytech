from django.shortcuts import render
from django.views.generic import CreateView

from main.models import Carousel, CarouselAction, WhyChose


class IndexView(CreateView):
    template_name = 'site/index.html'

    def get(self, request, *args, **kwargs):
        carousels = Carousel.objects.filter(enabled=True)
        carousels_list = []
        for carousel in carousels:
            carousel_actions = CarouselAction.objects.filter(
                carousel=carousel, enabled=True)
            carousels_list.append({'carousel': carousel, 'carousel_actions': carousel_actions})
        why_chose = WhyChose.objects.filter(enabled=True)
        context = {'carousels': carousels_list, 'why_chose': why_chose}
        return render(request, self.template_name, context)
