from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="分类名称")
    description = models.TextField(blank=True, verbose_name="描述")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    
    class Meta:
        verbose_name = "商品分类"
        verbose_name_plural = "商品分类"
    
    def __str__(self):
        return self.name

class Product(models.Model):
    STATUS_CHOICES = [
        ('available', '可用'),
        ('out_of_stock', '缺货'),
        ('discontinued', '停产'),
    ]
    
    name = models.CharField(max_length=200, verbose_name="产品名称")
    description = models.TextField(verbose_name="产品描述")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格")
    stock_quantity = models.IntegerField(default=0, verbose_name="库存数量")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name="状态")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    class Meta:
        verbose_name = "产品"
        verbose_name_plural = "产品"
    
    def __str__(self):
        return f"{self.name} - ¥{self.price}"

class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="客户姓名")
    email = models.EmailField(unique=True, verbose_name="邮箱")
    phone = models.CharField(max_length=20, blank=True, verbose_name="电话")
    address = models.TextField(verbose_name="地址")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="注册时间")
    
    class Meta:
        verbose_name = "客户"
        verbose_name_plural = "客户"
    
    def __str__(self):
        return self.name