FROM python:3.9
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN mkdir -p /var/calendarapi/\
 && mkdir -p /var/calendarapi/static/ \
 && mkdir -p /var/calendarapi/media/ \
 && mkdir -p /var/calendarapi/config/

# Установка пакетов Python
COPY config/local/requirements.txt /var/calendarapi/config/

RUN pip install --no-cache-dir -r /var/calendarapi/config/requirements.txt
# Копируем файлы настроек в отедльную директорию
COPY config/local/ /var/calendarapi/config/

# Переносим весь проект
COPY src /usr/src/app/

ENTRYPOINT ["/var/calendarapi/config/docker/wait-for-postgres-start.sh"]
