#!/usr/bin/env python
"""
项目初始化脚本
"""

import os
import sys
import django
import subprocess

def setup_project():
    """设置Django项目"""
    print("设置Django项目...")
    
    # 设置环境变量
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    os.environ['LANGUAGE_CODE'] = 'zh-hans'
    
    try:
        django.setup()
        print("Django设置成功!")
        return True
    except Exception as e:
        print(f"Django设置失败: {e}")
        return False

def run_migrations():
    """运行数据库迁移"""
    print("运行数据库迁移...")
    try:
        subprocess.run([sys.executable, 'manage.py', 'makemigrations'], check=True)
        subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)
        print("数据库迁移成功!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"数据库迁移失败: {e}")
        return False

def create_superuser():
    """创建管理员用户"""
    print("创建管理员用户...")
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            print("管理员用户创建成功!")
            print("用户名: admin")
            print("密码: admin123")
        else:
            print("管理员用户已存在")
        return True
    except Exception as e:
        print(f"创建管理员用户失败: {e}")
        return False

if __name__ == "__main__":
    print("项目初始化...")
    
    if setup_project():
        if run_migrations():
            create_superuser()
            print("\n初始化完成! 现在可以运行数据生成脚本。")
        else:
            print("初始化失败: 数据库迁移错误")
    else:
        print("初始化失败: Django设置错误")