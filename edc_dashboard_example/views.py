from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from edc_base.views.edc_base_view_mixin import EdcBaseViewMixin
from edc_dashboard.views import SubjectDashboardView as SubjectDashboardViewParent

from .models import Subject


class HomeView(EdcBaseViewMixin, TemplateView):

    template_name = 'edc_dashboard_example/home.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)


class MySubjectDashboard(SubjectDashboardViewParent):

    def subject_demographics(self):
        obj = Subject.objects.get(subject_identifier=self.subject_identifier)
        return {
            'first_name': obj.first_name,
            'last_name': obj.lastname,
            'initials': obj.initials,
            'dob': obj.dob}
