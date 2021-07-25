FROM python:3.8
COPY . /app
WORKDIR /app
ENV FLASK_APP=manage.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
RUN python3 --version
RUN pip install pipenv
RUN pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r requirements.txt
RUN pip install Authlib
EXPOSE 80
ENTRYPOINT [ "python3" ]
CMD [ "manage.py" ] 