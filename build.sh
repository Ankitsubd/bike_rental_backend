#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🚀 Starting build process..."

pip install -r requirements.txt

echo "📦 Installing dependencies completed"

python manage.py collectstatic --no-input

echo "📁 Static files collected"

# Database management with persistence
echo "🗄️ Checking database..."

if [ ! -f "db.sqlite3" ]; then
    echo "📊 Creating new database..."
    python manage.py migrate
    echo "✅ Database initialized"
else
    echo "📊 Database exists, checking migrations..."
    python manage.py migrate --run-syncdb
    echo "✅ Database migrations applied"
fi

echo "🎉 Build completed successfully!" 