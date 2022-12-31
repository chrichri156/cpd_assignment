FROM python:3.8
RUN python -m pip install pip==22.3.1
RUN pip install flask==2.2.2
RUN pip install mysql-connector-python==8.0.31
WORKDIR /cpd_assignment
COPY form.py /cpd_assignment/form.py
COPY index.html /cpd_assignment/index.html
COPY index_style.css /cpd_assignment/index_style.css
COPY success.html /cpd_assignment/success.html
COPY success_style.css /cpd_assignment/success_style.css
CMD ["python", "form.py"]
