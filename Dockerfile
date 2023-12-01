FROM python:3.11
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
RUN chmod +x ./entry.sh
ENTRYPOINT ["./entry.sh"]
