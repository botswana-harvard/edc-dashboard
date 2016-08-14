# edc-dashboard

This is old code that desparately needs to be reworked / redesigned.

in urls.py

    from edc.dashboard.section.classes import site_sections
    site_sections.autodiscover()
    site_sections.update_section_lists()
    
    urlpatterns += patterns(
    '',
    url(r'^{app_name}/dashboard/'.format(app_name=APP_NAME),
        include('apps.{app_name}_dashboard.urls'.format(app_name=APP_NAME))),
    )
    urlpatterns += patterns(
        '',
        url(r'^{app_name}/section/'.format(app_name=APP_NAME),
            include('edc.dashboard.section.urls'), name='section'),
    )
    urlpatterns += patterns(
        '',
        url(r'^{app_name}/$'.format(app_name=APP_NAME),
            RedirectView.as_view(url='/{app_name}/section/'.format(app_name=APP_NAME))),
        url(r'', RedirectView.as_view(url='/{app_name}/section/'.format(app_name=APP_NAME))),
    )

    
## Pre-upgrade

### Features

#### Sections
    * divide the edc into sections such as maternal, infant. 
    * get to the correct subject in a section based on a search
    * search is applied to a model, such as consent
    * search term is usually just the subject_identifier
    Note: this is not really a "dashboard" feature but originally enabled a user to get to a dashboard
 
#### Subject Dashboard
    * marquee with demographics on the subject (identifier, dob, age, status, consent, etc)
    * shows all appointments
    * can drill in on appointments to see visit form and all required CRFs
    * listed CRFs include a link to get to the entry form (currently the admin form)
    * listed CRFs are based on meta data from edc-metadata
    * listed CRFs are flagged as required or not required based on logic managed by edc-rule-groups
    * CRFs are grouped by scheduled forms, unscheduled forms, lab requisitions, optional lab requisitions
      
       
