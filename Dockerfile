FROM python:3.13
WORKDIR /app
COPY script.py .
EXPOSE 8000
CMD ["python", "-u", "script.py"]