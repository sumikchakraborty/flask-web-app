#!/bin/bash
# entrypoint.sh

# Wait for Postgres to be ready
echo "Waiting for Postgres..."
while ! pg_isready -h "$POSTGRES_HOST" -p 5432 -U "$POSTGRES_USER"; do
  sleep 1
done
echo "Postgres is ready!"

# Initialize database
python init_db.py

# Start Flask
exec python -m flask run --host=0.0.0.0
