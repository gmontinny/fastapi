FROM python:3.9-slim

WORKDIR /app

#ADD requirements /app/requirements/
ADD requirements.txt /app/requirements.txt

RUN python -m venv /env \
&& /env/bin/pip install --upgrade pip \
&& /env/bin/pip install --no-cache-dir -r /app/requirements.txt

ADD . /app


ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH


EXPOSE 8001


CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8001"]