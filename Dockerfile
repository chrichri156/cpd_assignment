FROM python:3.8-slim
RUN python -m pip install pip==22.3.1 && \
  pip install flask && \
  pip install mysql-connector-python
WORKDIR /cpd_assignment
COPY . /cpd_assignment
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=3000"]
EXPOSE 3000
ENTRYPOINT ["python", "form.py"]
HEALTHCHECK --interval=30s --timeout=5s CMD ["curl", "-f", "http://cpd3.westeurope.cloudapp.azure.com:80"]
