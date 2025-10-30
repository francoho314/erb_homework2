#!/usr/bin/env python

import os
import sys
import django
import random
import json
from datetime import datetime, timedelta
from decimal import Decimal

# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# 设置Django环境 - 修复语言问题
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample_data.settings')

# 在django.setup()之前设置语言环境
os.environ['LANGUAGE_CODE'] = 'zh-hans'

try:
    django.setup()
except Exception as e:
    print(f"Django设置错误: {e}")
    sys.exit(1)

from django.contrib.auth.models import User
from sample_data.models import Category, Product, Customer

class DataManager:
    """数据管理类"""
    
    def __init__(self):
        self.generated_data = {
            'categories': [],
            'products': [],
            'customers': []
        }
    
    def clean_database(self):
        """清理数据库中的所有样本数据"""
        print("清理数据库中...")
        
        try:
            # 注意：删除顺序很重要，因为有外键约束
            Product.objects.all().delete()
            Customer.objects.all().delete()
            Category.objects.all().delete()
            
            # 删除非管理员用户
            User.objects.filter(is_staff=False).delete()
            
            print("数据库清理完成")
        except Exception as e:
            print(f"清理数据库时出错: {e}")
    
    def generate_categories(self):
        """生成商品分类数据"""
        print("生成商品分类...")
        
        categories_data = [
            {"name": "电子产品", "description": "手机、电脑、平板等电子设备"},
            {"name": "家用电器", "description": "冰箱、洗衣机、空调等家用电器"},
            {"name": "服装鞋帽", "description": "男女服装、鞋子、配饰"},
            {"name": "食品饮料", "description": "零食、饮料、生鲜食品"},
            {"name": "图书文具", "description": "书籍、文具、办公用品"},
        ]
        
        for data in categories_data:
            try:
                category = Category.objects.create(**data)
                self.generated_data['categories'].append(category)
                print(f"  创建分类: {category.name}")
            except Exception as e:
                print(f"创建分类 {data['name']} 时出错: {e}")
        
        return self.generated_data['categories']
    
    def generate_products(self):
        """生成产品数据"""
        print("生成产品数据...")
        
        products_data = [
            # 电子产品
            {"name": "iPhone 15 Pro", "price": 8999.00, "stock": 50, "desc": "最新款iPhone，搭载A17 Pro芯片"},
            {"name": "MacBook Air M2", "price": 9499.00, "stock": 30, "desc": "轻薄便携，性能强大的笔记本电脑"},
            {"name": "三星 Galaxy S24", "price": 5999.00, "stock": 25, "desc": "三星旗舰手机，拍照效果出色"},
            {"name": "iPad Pro", "price": 6799.00, "stock": 40, "desc": "专业级平板电脑，适合创作和工作"},
            
            # 家用电器
            {"name": "智能冰箱", "price": 4599.00, "stock": 15, "desc": "智能控制，节能环保"},
            {"name": "滚筒洗衣机", "price": 3299.00, "stock": 20, "desc": "静音设计，多种洗涤模式"},
            
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
        ]
        
        if not self.generated_data['categories']:
            print("错误：没有可用的分类，请先生成分类")
            return []
        
        for data in products_data:
            try:
                category = random.choice(self.generated_data['categories'])
                
                product = Product.objects.create(
                    name=data["name"],
                    description=data["desc"],
                    price=Decimal(str(data["price"])),
                    stock_quantity=data["stock"],
                    category=category,
                    status="available"
                )
                
                self.generated_data['products'].append(product)
                print(f"  创建产品: {product.name} - ¥{product.price}")
            except Exception as e:
                print(f"创建产品 {data['name']} 时出错: {e}")
        
        return self.generated_data['products']
    
    def generate_customers(self):
        """生成客户数据"""
        print("生成客户数据...")
        
        customers_data = [
            {"name": "张三", "email": "zhangsan@email.com", "phone": "13800138001", "address": "北京市朝阳区建国路123号"},
            {"name": "李四", "email": "lisi@email.com", "phone": "13800138002", "address": "上海市浦东新区陆家嘴路456号"},
            {"name": "王五", "email": "wangwu@email.com", "phone": "13800138003", "address": "广州市天河区体育西路789号"},
            {"name": "赵六", "email": "zhaoliu@email.com", "phone": "13800138004", "address": "深圳市南山区科技园101号"},
            {"name": "钱七", "email": "qianqi@email.com", "phone": "13800138005", "address": "杭州市西湖区文三路202号"},
        ]
        
        for data in customers_data:
            try:
                customer = Customer.objects.create(**data)
                self.generated_data['customers'].append(customer)
                print(f"  创建客户: {customer.name} - {customer.email}")
            except Exception as e:
                print(f"创建客户 {data['name']} 时出错: {e}")
        
        return self.generated_data['customers']
    
    def generate_sample_data(self):
        """生成完整的样本数据"""
        print("开始生成样本数据...")
        print("=" * 50)
        
        # 清理数据
        self.clean_database()
        
        # 生成数据
        categories = self.generate_categories()
        products = self.generate_products()
        customers = self.generate_customers()
        
        # 统计信息
        total_records = len(categories) + len(products) + len(customers)
        
        print("=" * 50)
        print("样本数据生成完成!")
        print(f"生成统计:")
        print(f"  商品分类: {len(categories)} 个")
        print(f"  产品数据: {len(products)} 个")
        print(f"  客户数据: {len(customers)} 个")
        print(f"  总计: {total_records} 条记录")
        print("\n下一步操作:")
        print("   1. 运行: python manage.py runserver")
        print("   2. 访问: http://localhost:8000/admin/")
        print("   3. 使用管理员账户登录查看数据")

def main():
    """主函数"""
    print("Django 样本数据管理系统")
    print("=" * 40)
    
    try:
        manager = DataManager()
        manager.generate_sample_data()
    except Exception as e:
        print(f"发生错误: {e}")
        print("请确保已执行数据库迁移: python manage.py migrate")

if __name__ == "__main__":
    main()