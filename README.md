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
