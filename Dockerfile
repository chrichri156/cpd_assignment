# syntax=docker/dockerfile:1
FROM python:3.8
RUN pip install flask
WORKDIR /app
COPY form.py .
COPY index.html templates/index.html
COPY style.css static/css/style.css
CMD ["python", "form.py"]
