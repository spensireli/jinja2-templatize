FROM python:3.8
COPY jinja2_templatize /app
COPY requirements.txt /app
RUN pip3 install -r /app/requirements.txt
ENTRYPOINT ["python3", "/app/main.py"]
