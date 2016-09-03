# edc-dashboard

in development ...

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
      
       
