FROM python:3.8-slim
RUN python -m pip install pip==22.3.1
COPY requirements.txt /cpd_assignment/requirements.txt
RUN pip install --upgrade -r requirements.txt
WORKDIR /cpd_assignment
COPY form.py /cpd_assignment/form.py
COPY index.html /cpd_assignment/index.html
COPY index_style.css /cpd_assignment/index_style.css
COPY success.html /cpd_assignment/success.html
COPY success_style.css /cpd_assignment/success_style.css
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]
EXPOSE 80
ENTRYPOINT ["python", "form.py"]
HEALTHCHECK --interval=30s --timeout=5s CMD ["curl", "-f", "http://cpd3.westeurope.cloudapp.azure.com:80"]
