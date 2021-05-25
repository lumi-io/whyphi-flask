FROM python:3.7.9

WORKDIR /

RUN pip install pipenv && \
    pipenv install

ENV FLASK_APP "manage.py"

CMD pipenv run pytest