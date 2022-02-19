#!/bin/bash

rm -f '/tmp/calendarapi.pid'
celery -A calendarapi.celery_app beat --pidfile=/tmp/calendarapi.pid -s /var/calendarapi/celerybeat-schedule
