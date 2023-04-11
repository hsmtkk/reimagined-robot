#!/bin/sh
echo begin
echo "bind to port ${PORT}"
uvicorn main:app --reload --host 0.0.0.0 --port $PORT
echo end
