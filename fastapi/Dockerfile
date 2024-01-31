FROM python:3.11
WORKDIR /usr/src/app
EXPOSE 8080
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
ENV OTEL_EXPORTER_OTLP_INSECURE=true
ENV OTEL_EXPORTER_OTLP_PROTOCOL=grpc
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://collector:4317"
ENV OTEL_LOGS_EXPORTER="otlp"
ENV OTEL_TRACES_EXPORTER="none"
ENV OTEL_METRICS_EXPORTER="none"
ENV OTEL_PYTHON_LOG_CORRELATION=true
ENV OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
ENV OTEL_PYTHON_LOG_LEVEL=info
COPY . .
CMD ["opentelemetry-instrument", "--service_name", "vapb", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
