FROM python:3.14-alpine3.24

WORKDIR /app

#COPY . /app

CMD ["python","myapp.py"]


CMD python myapp.py
