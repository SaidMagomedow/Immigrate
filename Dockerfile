FROM python:3.9

ENV PYTHONUNBUFFERED=1


RUN pip install --upgrade pip\
    asgiref\
    atomicwrites==1.4.0\
    attrs==21.2.0\
    colorama==0.4.4\
    django==3.1.2\
    django-currentuser==0.5.3\
    djangorestframework==3.12.4\
    django-activeurl==0.2.0\
    django-crispy-forms==1.9.2\
    django-filter==2.4.0\
    django-js-reverse==0.9.1\
    django-mjml==0.10.2\
    django-mptt==0.11.0\
    django-formtools==2.2\
    django-notifications-hq==1.6.0\
    django-login-required-middleware==0.5.0\
    django-phonenumber-field[phonenumbers]==5.0.0\
    django-session-timeout==0.1.0\
    django-tables2==2.3.2\
    django-debug-toolbar==3.1.1\
    django-debug-toolbar-line-profiling==0.7.1\
    django-debug-toolbar-template-profiler==2.0.1\
    git+git://github.com/wearespindle/django-debug-toolbar-template-timings.git@d49ba04acd71c1902997fa9d2b64e47019981fd6 \
    django-silk==4.1.0 \
    django-test-plus==1.4.0 \
    iniconfig==1.1.1\
    packaging==20.9\
    pluggy==0.13.1\
    psycopg2-binary\
    py==1.10.0\
    pyparsing==2.4.7\
    pytest==6.2.4\
    pytz==2021.1\
    sqlparse==0.4.1\
    toml==0.10.2


WORKDIR code
COPY . /code