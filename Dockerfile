# syntax=docker/dockerfile:1
FROM python:3.8
RUN pip install flask
RUN pip install mysql-connector-python
WORKDIR /cpd_assignment
COPY form.py .
COPY index.html .
COPY index_style.css .
COPY success.html .
COPY success_style.css .
CMD ["python", "form.py"]
