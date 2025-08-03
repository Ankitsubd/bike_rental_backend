# Backend Configuration Guide

## Environment Variables

Create a `.env` file in the backend directory with the following variables:

```env
# Django Configuration
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=bike-rental-backend-jmhr.onrender.com,localhost,127.0.0.1

# Email Configuration
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Frontend URL for email links
FRONTEND_URL=https://bike-rental-frontend-lifz.vercel.app

# CORS Configuration
CORS_ALLOW_ALL_ORIGINS=True
```

## Configuration Details

### Django Settings
- **SECRET_KEY:** Required for Django security
- **DEBUG:** Set to False in production
- **ALLOWED_HOSTS:** Comma-separated list of allowed domains

### Email Settings
- **EMAIL_HOST_USER:** Gmail address for sending emails
- **EMAIL_HOST_PASSWORD:** Gmail app password (not regular password)
- **FRONTEND_URL:** Frontend URL for email verification links

### CORS Settings
- **CORS_ALLOW_ALL_ORIGINS:** Set to True for development, False for production

## Deployment

### Render
1. Set environment variables in Render dashboard
2. Build command: `./build.sh`
3. Start command: `gunicorn backend.wsgi:application`

### Local Development
1. Copy `env.example` to `.env`
2. Update settings for local development
3. Run `python manage.py runserver`

## Database

### SQLite (Default)
- File: `db.sqlite3`
- No additional configuration needed
- Good for development and small deployments

### PostgreSQL (Recommended for Production)
```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432
```

## Security

### Production Checklist
- [ ] DEBUG = False
- [ ] SECRET_KEY is secure and unique
- [ ] ALLOWED_HOSTS is properly configured
- [ ] CORS settings are secure
- [ ] Email credentials are set
- [ ] Static files are collected

## Troubleshooting

### Common Issues
1. **CORS errors:** Check CORS_ALLOWED_ORIGINS
2. **Email not sending:** Verify EMAIL_HOST_USER and EMAIL_HOST_PASSWORD
3. **Static files not serving:** Run `python manage.py collectstatic`
4. **Database errors:** Check database configuration

### Debug Mode
For debugging, set `DEBUG=True` and check Django logs for detailed error messages. 