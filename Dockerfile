FROM python:3.8

RUN mkdir /LightSwitcher
ENV APP_ROOT /LightSwitcher
WORKDIR $APP_ROOT

COPY ./requirements.txt $APP_ROOT/requirements.txt

RUN pip install -r requirements.txt

COPY . $APP_ROOT

CMD ["python", "light_switcher.py"]

