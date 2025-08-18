FROM apache/airflow:3.0.4
ADD requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt