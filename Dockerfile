FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .
EXPOSE 8000

# Add Healthcheck
HEALTHCHECK --interval=20s --timeout=7s --start-period=2s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000')" || exit 1

# Start the application
CMD ["python", "app.py"]