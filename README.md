# Whyphi-Flask

PCT Application Tracking System

[![License](http://img.shields.io/badge/License-MIT-brightgreen.svg)](./LICENSE) [![build Actions Status](https://github.com/lumi-io/boards/workflows/build/badge.svg)](https://github.com/lumi-io/boards/actions) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-orange.svg)](https://www.python.org/)

## Notes:

### To activate a virtual environment

```bash
pipenv shell
```

### To deactivate a virtual environment

```bash
deactivate
exit
```

### To install all the dependencies from pipenv

```bash
pipenv install
```

### To install a specific dependency into the project (make sure you are within the virtual environment)

```bash
pipenv install dependency_name
```

### To run the Flask App using Docker (Windows, MacOS, Linux, etc)

```bash
make start-dev-container
```

### To run the Flask App on Debug Mode (through Bash)

```bash
export FLASK_APP=manage.py
export FLASK_ENV=development
flask run
```

### To test the Flask Application (TBA)

First, ensure you have Docker downloaded (https://www.docker.com/products/docker-desktop)

```bash
make test-container
```



### Documentation/Guides
- https://flask.palletsprojects.com/en/1.0.x/
- https://flask.palletsprojects.com/en/1.1.x/tutorial/views/
- https://flask.palletsprojects.com/en/1.1.x/patterns/mongoengine/
