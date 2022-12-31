# syntax=docker/dockerfile:1
FROM python:3.8
RUN pip install flask
RUN pip install mysql-connector-python
WORKDIR /app
COPY form.py .
COPY index.html templates/index.html
COPY index_style.css static/css/index_style.css
COPY success.html /app/success.html
COPY success_style.css /app/success_style.css
CMD ["python", "form.py"]
