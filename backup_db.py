#!/usr/bin/env python3
"""
Database backup and restore utility for SQLite
"""
import os
import shutil
import sqlite3
from datetime import datetime
from pathlib import Path

def backup_database():
    """Backup the current database"""
    db_path = Path("db.sqlite3")
    if not db_path.exists():
        print("❌ No database file found")
        return False
    
    # Create backup directory
    backup_dir = Path("backups")
    backup_dir.mkdir(exist_ok=True)
    
    # Create backup filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup_dir / f"db_backup_{timestamp}.sqlite3"
    
    try:
        # Copy database file
        shutil.copy2(db_path, backup_path)
        print(f"✅ Database backed up to: {backup_path}")
        return True
    except Exception as e:
        print(f"❌ Backup failed: {e}")
        return False

def restore_database(backup_file):
    """Restore database from backup"""
    backup_path = Path("backups") / backup_file
    if not backup_path.exists():
        print(f"❌ Backup file not found: {backup_path}")
        return False
    
    try:
        # Copy backup to main database
        shutil.copy2(backup_path, "db.sqlite3")
        print(f"✅ Database restored from: {backup_path}")
        return True
    except Exception as e:
        print(f"❌ Restore failed: {e}")
        return False

def list_backups():
    """List all available backups"""
    backup_dir = Path("backups")
    if not backup_dir.exists():
        print("❌ No backups directory found")
        return
    
    backups = list(backup_dir.glob("db_backup_*.sqlite3"))
    if not backups:
        print("❌ No backup files found")
        return
    
    print("📁 Available backups:")
    for backup in sorted(backups, reverse=True):
        size = backup.stat().st_size / 1024  # KB
        print(f"  - {backup.name} ({size:.1f} KB)")

def check_database():
    """Check database status"""
    db_path = Path("db.sqlite3")
    if not db_path.exists():
        print("❌ Database file not found")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        # Check bike count
        cursor.execute("SELECT COUNT(*) FROM rental_api_bike;")
        bike_count = cursor.fetchone()[0]
        
        print(f"✅ Database is healthy")
        print(f"📊 Tables: {len(tables)}")
        print(f"🚴 Bikes: {bike_count}")
        
        conn.close()
    except Exception as e:
        print(f"❌ Database check failed: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python backup_db.py backup    # Create backup")
        print("  python backup_db.py restore <file>  # Restore from backup")
        print("  python backup_db.py list      # List backups")
        print("  python backup_db.py check     # Check database")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "backup":
        backup_database()
    elif command == "restore":
        if len(sys.argv) < 3:
            print("❌ Please specify backup file")
            sys.exit(1)
        restore_database(sys.argv[2])
    elif command == "list":
        list_backups()
    elif command == "check":
        check_database()
    else:
        print(f"❌ Unknown command: {command}")
        sys.exit(1) 