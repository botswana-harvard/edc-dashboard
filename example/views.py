from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from edc_base.views.edc_base_view_mixin import EdcBaseViewMixin
from django.views.generic.base import TemplateView


class HomeView(EdcBaseViewMixin, TemplateView):

    template_name = 'example/home.html'
    success_url = '/'
    paginate_by = 5

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)
