FROM python:3.11
WORKDIR /app
EXPOSE 5000
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
COPY . /app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--log-level=debug", "app:app"]