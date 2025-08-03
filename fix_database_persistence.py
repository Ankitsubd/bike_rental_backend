#!/usr/bin/env python3
"""
Comprehensive fix for database persistence issues
"""
import os
import sys
import shutil
from pathlib import Path

def fix_database_persistence():
    """Fix database persistence issues"""
    
    print("🔧 Fixing Database Persistence Issues")
    print("=" * 40)
    
    # Check current directory
    current_dir = Path.cwd()
    print(f"📁 Current directory: {current_dir}")
    
    # Check if we're in the right place
    if not (current_dir / "manage.py").exists():
        print("❌ Error: manage.py not found. Please run this from the backend directory.")
        return False
    
    # Check database file
    db_file = current_dir / "db.sqlite3"
    if db_file.exists():
        print(f"✅ Database file exists: {db_file}")
        print(f"📊 Size: {db_file.stat().st_size / 1024:.1f} KB")
    else:
        print("❌ Database file not found!")
        return False
    
    # Check build script
    build_script = current_dir / "build.sh"
    if build_script.exists():
        print(f"✅ Build script exists: {build_script}")
        
        # Read current build script
        with open(build_script, 'r') as f:
            content = f.read()
        
        # Check if persistence fix is already applied
        if "if [ ! -f \"db.sqlite3\" ]" in content:
            print("✅ Database persistence fix is already applied")
        else:
            print("❌ Database persistence fix is NOT applied")
            return False
    else:
        print("❌ Build script not found!")
        return False
    
    # Check production settings
    settings_file = current_dir / "backend" / "settings_production.py"
    if settings_file.exists():
        print(f"✅ Production settings exist: {settings_file}")
        
        with open(settings_file, 'r') as f:
            content = f.read()
        
        if "DATABASE_URL" in content:
            print("✅ Database URL configuration is applied")
        else:
            print("❌ Database URL configuration is NOT applied")
            return False
    else:
        print("❌ Production settings not found!")
        return False
    
    print("\n🎯 Database persistence should be working!")
    print("\n📋 To verify:")
    print("1. Deploy to Render")
    print("2. Add bikes through admin")
    print("3. Push to GitHub")
    print("4. Check if bikes persist")
    
    return True

def create_backup_script():
    """Create a backup script for production"""
    
    backup_script = """
#!/bin/bash
# Database backup script for production

echo "📦 Creating database backup..."

# Create backup directory
mkdir -p backups

# Create timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Backup database
if [ -f "db.sqlite3" ]; then
    cp db.sqlite3 "backups/db_backup_${TIMESTAMP}.sqlite3"
    echo "✅ Database backed up to: backups/db_backup_${TIMESTAMP}.sqlite3"
else
    echo "❌ Database file not found!"
fi
"""
    
    with open("backup_production.sh", "w") as f:
        f.write(backup_script)
    
    # Make executable
    os.chmod("backup_production.sh", 0o755)
    print("✅ Created backup script: backup_production.sh")

if __name__ == "__main__":
    print("🚀 Database Persistence Fix")
    print("=" * 30)
    
    # Check current setup
    if fix_database_persistence():
        print("\n✅ Database persistence is properly configured!")
        
        # Create backup script
        create_backup_script()
        
        print("\n📋 Next Steps:")
        print("1. Deploy to Render")
        print("2. Test by adding bikes")
        print("3. Push to GitHub")
        print("4. Verify bikes persist")
        
    else:
        print("\n❌ Database persistence needs to be fixed!")
        print("Please check the configuration files.") 