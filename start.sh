#!/bin/bash

if [[ "$VIRTUAL_ENV" == "" ]]; then
    source venv/bin/activate
fi
python app.py https://ua.igotoworld.com/
find . -name "__pycache__" -exec rm -rv {} + >/dev/null
