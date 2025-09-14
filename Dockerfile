FROM python:3.11-slim

# Install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Copy code and set entrypoint
COPY . /app
WORKDIR /app
ENTRYPOINT ["./entrypoint.sh"]

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
EXPOSE 5000
ENTRYPOINT ["/app/entrypoint.sh"]
