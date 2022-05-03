FROM python:3.8
WORKDIR /server
COPY ./requirements/base.txt /server/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt
COPY ./app /server/app
WORKDIR /server/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
