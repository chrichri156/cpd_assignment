# syntax=docker/dockerfile:1
FROM python:3.8
RUN pip install flask
RUN pip install mysql-connector-python
WORKDIR /app
COPY form.py .
COPY index.html templates/index.html
COPY style.css static/css/style.css
COPY success.html /app/success.html
COPY style2.css /app/style2.css
CMD ["python", "form.py"]
