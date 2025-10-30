#!/usr/bin/env python

"""
Django样本数据生成脚本
直接在项目根目录运行: python generate_sample_data.py
"""

import os
import sys
import django
import random
from decimal import Decimal

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample_data.settings')

try:
    django.setup()
    print("✓ Django环境设置成功")
except Exception as e:
    print(f"✗ Django环境设置失败: {e}")
    sys.exit(1)

from sample_data.models import Category, Product, Customer

def setup_database():
    """设置数据库（迁移和创建表）"""
    print("设置数据库...")
    
    try:
        # 导入Django命令
        from django.core.management import execute_from_command_line
        
        # 创建迁移文件
        print("创建迁移文件...")
        execute_from_command_line(['manage.py', 'makemigrations', 'sample_data'])
        
        # 应用迁移
        print("应用数据库迁移...")
        execute_from_command_line(['manage.py', 'migrate'])
        
        print("✓ 数据库设置完成")
        return True
        
    except Exception as e:
        print(f"✗ 数据库设置失败: {e}")
        return False

def create_superuser():
    """创建管理员用户"""
    print("创建管理员用户...")
    
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            print("✓ 管理员用户创建成功")
            print("  用户名: admin")
            print("  密码: admin123")
        else:
            print("✓ 管理员用户已存在")
        
        return True
    except Exception as e:
        print(f"创建管理员用户失败: {e}")
        return False

def generate_categories():
    """生成分类数据"""
    print("生成商品分类...")
    
    categories_data = [
        {"name": "电子产品", "description": "手机、电脑、平板等电子设备"},
        {"name": "家用电器", "description": "冰箱、洗衣机、空调等家用电器"},
        {"name": "服装鞋帽", "description": "男女服装、鞋子、配饰"},
        {"name": "食品饮料", "description": "零食、饮料、生鲜食品"},
        {"name": "图书文具", "description": "书籍、文具、办公用品"},
        {"name": "运动户外", "description": "运动器材、户外装备"},
        {"name": "美妆个护", "description": "化妆品、护肤品、个人护理"},
    ]
    
    categories = []
    for data in categories_data:
        category, created = Category.objects.get_or_create(
            name=data["name"],
            defaults=data
        )
        categories.append(category)
        if created:
            print(f"  ✓ 创建分类: {category.name}")
        else:
            print(f"  ✓ 分类已存在: {category.name}")
    
    return categories

def generate_products(categories):
    """生成产品数据"""
    print("生成产品数据...")
    
    products_data = [
        # 电子产品
        ("iPhone 15 Pro", 8999.00, 50, "电子产品", "最新款iPhone，搭载A17 Pro芯片"),
        ("MacBook Air M2", 9499.00, 30, "电子产品", "轻薄便携，性能强大的笔记本电脑"),
        ("三星 Galaxy S24", 5999.00, 25, "电子产品", "三星旗舰手机，拍照效果出色"),
        ("iPad Pro", 6799.00, 40, "电子产品", "专业级平板电脑，适合创作和工作"),
        ("AirPods Pro", 1899.00, 60, "电子产品", "主动降噪无线耳机"),
        
        # 家用电器
        ("智能冰箱", 4599.00, 15, "家用电器", "智能控制，节能环保"),
        ("滚筒洗衣机", 3299.00, 20, "家用电器", "静音设计，多种洗涤模式"),
        ("空调", 2899.00, 10, "家用电器", "变频节能，快速制冷制热"),
        
        # 服装鞋帽
        ("男士牛仔裤", 299.00, 100, "服装鞋帽", "舒适耐穿，多种尺码可选"),
        ("女士连衣裙", 459.00, 80, "服装鞋帽", "时尚设计，适合多种场合"),
        ("运动鞋", 599.00, 60, "服装鞋帽", "轻便舒适，适合运动穿着"),
        
        # 食品饮料
        ("有机咖啡豆", 89.00, 200, "食品饮料", "100%有机种植，香气浓郁"),
        ("进口巧克力", 68.00, 150, "食品饮料", "比利时进口，口感丝滑"),
        
        # 图书文具
        ("Python编程指南", 89.00, 45, "图书文具", "从入门到精通，适合初学者"),
        ("笔记本电脑包", 199.00, 70, "图书文具", "防水设计，多隔层收纳"),
        
        # 运动户外
        ("瑜伽垫", 129.00, 90, "运动户外", "防滑材质，环保材料"),
        ("登山杖", 159.00, 40, "运动户外", "碳纤维材质，轻便耐用"),
        
        # 美妆个护
        ("保湿面霜", 199.00, 120, "美妆个护", "深层保湿，适合各种肤质"),
        ("洗发水", 89.00, 180, "美妆个护", "无硅油配方，呵护头皮健康"),
    ]
    
    category_map = {cat.name: cat for cat in categories}
    products = []
    
    for name, price, stock, cat_name, desc in products_data:
        category = category_map.get(cat_name)
        if category:
            product, created = Product.objects.get_or_create(
                name=name,
                defaults={
                    'description': desc,
                    'price': Decimal(str(price)),
                    'stock_quantity': stock,
                    'category': category,
                    'status': 'available'
                }
            )
            products.append(product)
            if created:
                print(f"  ✓ 创建产品: {product.name} - ¥{product.price}")
            else:
                print(f"  ✓ 产品已存在: {product.name}")
    
    return products

def generate_customers():
    """生成客户数据"""
    print("生成客户数据...")
    
    customers_data = [
        ("张三", "zhangsan@email.com", "13800138001", "北京市朝阳区建国路123号"),
        ("李四", "lisi@email.com", "13800138002", "上海市浦东新区陆家嘴路456号"),
        ("王五", "wangwu@email.com", "13800138003", "广州市天河区体育西路789号"),
        ("赵六", "zhaoliu@email.com", "13800138004", "深圳市南山区科技园101号"),
        ("钱七", "qianqi@email.com", "13800138005", "杭州市西湖区文三路202号"),
        ("孙八", "sunba@email.com", "13800138006", "成都市武侯区人民南路303号"),
        ("周九", "zhoujiu@email.com", "13800138007", "武汉市武昌区中南路404号"),
        ("吴十", "wushi@email.com", "13800138008", "南京市鼓楼区中山路505号"),
    ]
    
    customers = []
    for name, email, phone, address in customers_data:
        customer, created = Customer.objects.get_or_create(
            email=email,
            defaults={
                'name': name,
                'phone': phone,
                'address': address
            }
        )
        customers.append(customer)
        if created:
            print(f"  ✓ 创建客户: {customer.name} - {customer.email}")
        else:
            print(f"  ✓ 客户已存在: {customer.name}")
    
    return customers

def main():
    """主函数"""
    print("=" * 50)
    print("Django 样本数据生成系统")
    print("=" * 50)
    
    # 1. 设置数据库
    if not setup_database():
        print("数据库设置失败，退出...")
        return
    
    # 2. 创建管理员用户
    create_superuser()
    
    # 3. 生成样本数据
    print("\n开始生成样本数据...")
    print("-" * 40)
    
    categories = generate_categories()
    products = generate_products(categories)
    customers = generate_customers()
    
    # 统计信息
    total_categories = Category.objects.count()
    total_products = Product.objects.count()
    total_customers = Customer.objects.count()
    total_records = total_categories + total_products + total_customers
    
    print("\n" + "=" * 50)
    print("🎉 样本数据生成完成!")
    print(f"📊 生成统计:")
    print(f"   商品分类: {total_categories} 个")
    print(f"   产品数据: {total_products} 个")
    print(f"   客户数据: {total_customers} 个")
    print(f"   总计: {total_records} 条记录")
    
    print("\n🎯 下一步操作:")
    print("  1. 启动服务器: python manage.py runserver")
    print("  2. 访问管理后台: http://localhost:8000/admin/")
    print("  3. 使用以下账户登录:")
    print("     - 用户名: admin")
    print("     - 密码: admin123")
    print("=" * 50)

if __name__ == "__main__":
    main()