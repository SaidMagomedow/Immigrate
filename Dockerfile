FROM python:3.9

ENV PYTHONUNBUFFERED=1


RUN pip install --upgrade pip\
    asgiref==3.3.4\
    atomicwrites==1.4.0\
    attrs==21.2.0\
    colorama==0.4.4\
    Django==3.2.4\
    django-currentuser==0.5.3\
    djangorestframework==3.12.4\
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