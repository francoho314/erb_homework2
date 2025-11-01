#!/usr/bin/env python
import os
import sys
import django
import random
from decimal import Decimal

# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

# 设置Django环境 - 使用正确的设置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

try:
    django.setup()
    print("✓ Django环境设置成功")
except Exception as e:
    print(f"✗ Django环境设置失败: {e}")
    sys.exit(1)

from django.core.management import execute_from_command_line
from sample_data.models import Category, Product, Customer

def setup_database():
    """设置数据库（迁移和创建表）"""
    print("设置数据库...")
    
    try:
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

def clean_database():
    """清理数据库中的所有样本数据"""
    print("清理数据库中...")
    
    try:
        # 注意：删除顺序很重要，因为有外键约束
        Product.objects.all().delete()
        Customer.objects.all().delete()
        Category.objects.all().delete()
        print("数据库清理完成")
    except Exception as e:
        print(f"清理数据库时出错: {e}")

def generate_categories():
    """生成商品分类数据"""
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
        try:
            category = Category.objects.create(**data)
            categories.append(category)
            print(f"  ✓ 创建分类: {category.name}")
        except Exception as e:
            print(f"创建分类 {data['name']} 时出错: {e}")
    
    return categories

def generate_products(categories):
    """生成产品数据"""
    print("生成产品数据...")
    
    products_data = [
        # 电子产品
        {"name": "iPhone 15 Pro", "price": 8999.00, "stock": 50, "desc": "最新款iPhone，搭载A17 Pro芯片"},
        {"name": "MacBook Air M2", "price": 9499.00, "stock": 30, "desc": "轻薄便携，性能强大的笔记本电脑"},
        {"name": "三星 Galaxy S24", "price": 5999.00, "stock": 25, "desc": "三星旗舰手机，拍照效果出色"},
        {"name": "iPad Pro", "price": 6799.00, "stock": 40, "desc": "专业级平板电脑，适合创作和工作"},
        {"name": "AirPods Pro", "price": 1899.00, "stock": 60, "desc": "主动降噪无线耳机"},
        
        # 家用电器
        {"name": "智能冰箱", "price": 4599.00, "stock": 15, "desc": "智能控制，节能环保"},
        {"name": "滚筒洗衣机", "price": 3299.00, "stock": 20, "desc": "静音设计，多种洗涤模式"},
        {"name": "空调", "price": 2899.00, "stock": 10, "desc": "变频节能，快速制冷制热"},
        
        # 服装鞋帽
        {"name": "男士牛仔裤", "price": 299.00, "stock": 100, "desc": "舒适耐穿，多种尺码可选"},
        {"name": "女士连衣裙", "price": 459.00, "stock": 80, "desc": "时尚设计，适合多种场合"},
        {"name": "运动鞋", "price": 599.00, "stock": 60, "desc": "轻便舒适，适合运动穿着"},
        
        # 食品饮料
        {"name": "有机咖啡豆", "price": 89.00, "stock": 200, "desc": "100%有机种植，香气浓郁"},
        {"name": "进口巧克力", "price": 68.00, "stock": 150, "desc": "比利时进口，口感丝滑"},
        
        # 图书文具
        {"name": "Python编程指南", "price": 89.00, "stock": 45, "desc": "从入门到精通，适合初学者"},
        {"name": "笔记本电脑包", "price": 199.00, "stock": 70, "desc": "防水设计，多隔层收纳"},
        
        # 运动户外
        {"name": "瑜伽垫", "price": 129.00, "stock": 90, "desc": "防滑材质，环保材料"},
        {"name": "登山杖", "price": 159.00, "stock": 40, "desc": "碳纤维材质，轻便耐用"},
        
        # 美妆个护
        {"name": "保湿面霜", "price": 199.00, "stock": 120, "desc": "深层保湿，适合各种肤质"},
        {"name": "洗发水", "price": 89.00, "stock": 180, "desc": "无硅油配方，呵护头皮健康"},
    ]
    
    products = []
    for data in products_data:
        try:
            category = random.choice(categories)
            
            product = Product.objects.create(
                name=data["name"],
                description=data["desc"],
                price=Decimal(str(data["price"])),
                stock_quantity=data["stock"],
                category=category,
                status="available"
            )
            
            products.append(product)
            print(f"  ✓ 创建产品: {product.name} - ¥{product.price}")
        except Exception as e:
            print(f"创建产品 {data['name']} 时出错: {e}")
    
    return products

def generate_customers():
    """生成客户数据"""
    print("生成客户数据...")
    
    customers_data = [
        {"name": "张三", "email": "zhangsan@email.com", "phone": "13800138001", "address": "北京市朝阳区建国路123号"},
        {"name": "李四", "email": "lisi@email.com", "phone": "13800138002", "address": "上海市浦东新区陆家嘴路456号"},
        {"name": "王五", "email": "wangwu@email.com", "phone": "13800138003", "address": "广州市天河区体育西路789号"},
        {"name": "赵六", "email": "zhaoliu@email.com", "phone": "13800138004", "address": "深圳市南山区科技园101号"},
        {"name": "钱七", "email": "qianqi@email.com", "phone": "13800138005", "address": "杭州市西湖区文三路202号"},
        {"name": "孙八", "email": "sunba@email.com", "phone": "13800138006", "address": "成都市武侯区人民南路303号"},
        {"name": "周九", "email": "zhoujiu@email.com", "phone": "13800138007", "address": "武汉市武昌区中南路404号"},
        {"name": "吴十", "email": "wushi@email.com", "phone": "13800138008", "address": "南京市鼓楼区中山路505号"},
    ]
    
    customers = []
    for data in customers_data:
        try:
            customer = Customer.objects.create(**data)
            customers.append(customer)
            print(f"  ✓ 创建客户: {customer.name} - {customer.email}")
        except Exception as e:
            print(f"创建客户 {data['name']} 时出错: {e}")
    
    return customers

def main():
    """主函数"""
    print("=" * 50)
    print("Django 样本数据生成系统 (修复版)")
    print("=" * 50)
    
    # 1. 设置数据库
    if not setup_database():
        print("数据库设置失败，退出...")
        return
    
    # 2. 创建管理员用户
    create_superuser()
    
    # 3. 清理现有数据
    clean_database()
    
    # 4. 生成样本数据
    print("\n开始生成样本数据...")
    print("-" * 40)
    
    categories = generate_categories()
    products = generate_products(categories)
    customers = generate_customers()
    
    # 统计信息
    total_categories = len(categories)
    total_products = len(products)
    total_customers = len(customers)
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