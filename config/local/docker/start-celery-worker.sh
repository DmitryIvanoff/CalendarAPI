#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

celery -A calendarapi.celery_app worker -E
