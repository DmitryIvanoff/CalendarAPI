#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

celery -A calendarapi.celery_app flower --broker_api=http://guest:guest@rabbit:15672/api/ --port=32201