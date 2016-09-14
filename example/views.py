import json
from datetime import date
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from edc_base.views.edc_base_view_mixin import EdcBaseViewMixin
from edc_dashboard.views import SubjectDashboardView as SubjectDashboardViewParent
from edc_example.models import SubjectConsent
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from edc_dashboard.forms import SubjectForm


class HomeView(EdcBaseViewMixin, FormView):

    template_name = 'example/home.html'
    form_class = SubjectForm
    success_url = '/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        print(context)
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(request, form)
        else:
            return self.form_invalid(request, form)

#     def form_invalid(self, request, form):
#         if request.is_ajax():
#             response_data = {}

    def form_valid(self, request, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        if request.is_ajax():
            response_data = {}
            if form.cleaned_data['subject_identifier']:
                subject_identifier = form.cleaned_data['subject_identifier']
                try:
                    subject_consent = SubjectConsent.objects.get(subject_identifier=subject_identifier)
                    subject_consent = json.dumps(
                        {'subject_identifier': subject_consent.subject_identifier,
                         'first_name': subject_consent.first_name,
                         'initials': subject_consent.initials,
                         'version': subject_consent.version})
                except SubjectConsent.DoesNotExist as e:
                    subject_consent = None
                response_data.update({
                    'subject_consent': subject_consent,
                    'subject_identifier': subject_identifier,
                    'first_name': 'Erik',
                    'initials': 'EW',
                    # 'dob': date.today() - relativedelta(years=25),
                    # 'consent_datetime': timezone.now(),
                    'gender': 'Male'})
                response_data.update(**form.cleaned_data)
                print(response_data)
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        return HttpResponseRedirect(self.get_success_url())


class MySubjectDashboard(SubjectDashboardViewParent):

    def subject_demographics(self):
        obj = SubjectConsent.objects.get(subject_identifier=self.subject_identifier)
        return {
            'first_name': obj.first_name,
            'last_name': obj.lastname,
            'initials': obj.initials,
            'dob': obj.dob}
