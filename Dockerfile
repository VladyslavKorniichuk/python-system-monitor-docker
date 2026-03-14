# Basic image with Python 3.13
FROM python:3.13-slim AS builder

WORKDIR /build

# Create a virtual environment and install dependencies
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Clean up build artifacts
FROM python:3.13-slim AS runner

# Security Best Practice: Create a non-root user to run the application
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

WORKDIR /app

# MULTI-STAGE: 
COPY --from=builder /opt/venv /opt/venv
# Set the PATH to use the virtual environment
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# Copy application code
COPY app.py .
COPY templates/ templates/
COPY static/ static/

# Change ownership of the files to the non-root user
RUN chown -R appuser:appgroup /app

# Switch to the non-root user
USER appuser

EXPOSE 8000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000')" || exit 1

CMD ["python", "app.py"]