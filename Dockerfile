FROM python:alpine3.7 
COPY . /app
WORKDIR /app
ENV FLASK_APP=manage.py
RUN pip install pipenv
RUN pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn
EXPOSE 80
ENTRYPOINT [ "python3" ]
CMD [ "manage.py" ] 