FROM python:3.10-slim-bullseye

ARG APP_PATH=/app

WORKDIR ${APP_PATH}

COPY ./requirements.txt /${APP_PATH}/requirements.txt

# RUN pip install --no-cache-dir --upgrade -r /${APP_PATH}/requirements.txt
RUN pip install --upgrade -r /${APP_PATH}/requirements.txt

COPY . /${APP_PATH}

EXPOSE 80

ENTRYPOINT ["uvicorn", "app.main:app"]
CMD ["--host","0.0.0.0", "--port", "80"]