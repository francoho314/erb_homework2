# Django 样本数据生成系统

一个完整的Django应用程序，用于生成和管理样本数据。该系统提供了数据模型定义、样本数据生成、数据导入导出以及Django管理面板集成功能。

## 🌟 功能特点

- ✅ **数据模型设计** - 包含商品分类、产品和客户三个核心数据模型
- ✅ **样本数据生成** - 自动生成超过20条真实样本记录
- ✅ **数据清理** - 自动清理现有测试数据
- ✅ **导入/导出** - 支持JSON格式的数据交换
- ✅ **管理面板** - 完整的Django Admin界面
- ✅ **中文支持** - 完整的中文界面和提示信息

## 🛠 技术栈

- **后端框架**: Django 4.2+
- **数据库**: SQLite (默认，可配置为其他数据库)
- **编程语言**: Python 3.8+
- **数据格式**: JSON

## 📁 项目结构

```
erb_homework2/
├── manage.py                 # Django项目管理脚本
├── generate_sample_data.py   # 数据生成主脚本
├── requirements.txt          # 项目依赖
├── db.sqlite3               # SQLite数据库文件
└── sample_data/             # Django应用目录
    ├── __init__.py
    ├── settings.py          # 项目设置
    ├── urls.py              # URL路由配置
    ├── models.py            # 数据模型定义
    ├── admin.py             # 管理面板配置
    └── migrations/          # 数据库迁移文件
        └── __init__.py
```

## 🗃 数据模型

系统包含三个主要数据模型：

### 1. Category (商品分类)
- 名称、描述、创建时间
- 与产品建立一对多关系

### 2. Product (产品)
- 名称、描述、价格、库存数量
- 状态（可用/缺货/停产）
- 关联分类、创建时间、更新时间

### 3. Customer (客户)
- 姓名、邮箱、电话、地址
- 注册时间

## 🚀 快速开始

### 环境要求

- Python 3.8 或更高版本
- Django 4.2 或更高版本

### 安装步骤

1. **克隆项目**
```bash
git clone git@github.com:francoho314/erb_homework2.git
cd erb_homework2
```

2. **创建虚拟环境（推荐）**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows
```

3. **安装依赖**
```bash
pip install django
```

4. **运行数据生成脚本**
```bash
python generate_sample_data.py
```

这个脚本会自动执行以下操作：
- 创建数据库迁移文件
- 应用数据库迁移
- 创建管理员账户 (admin/admin123)
- 生成样本数据（7个分类，20个产品，8个客户）

5. **启动开发服务器**
```bash
python manage.py runserver
```

6. **访问管理面板**
- 打开 http://localhost:8000/admin/
- 使用以下凭据登录：
  - 用户名: `admin`
  - 密码: `admin123`

## 📊 样本数据详情

### 生成的分类 (7个)
- 电子产品、家用电器、服装鞋帽、食品饮料、图书文具、运动户外、美妆个护

### 生成的产品 (20个)
| 产品名称 | 价格 | 分类 | 库存 |
|---------|------|------|------|
| iPhone 15 Pro | ¥8999.00 | 电子产品 | 50 |
| MacBook Air M2 | ¥9499.00 | 电子产品 | 30 |
| 智能冰箱 | ¥4599.00 | 家用电器 | 15 |
| 男士牛仔裤 | ¥299.00 | 服装鞋帽 | 100 |
| Python编程指南 | ¥89.00 | 图书文具 | 45 |
| ... 等等 | ... | ... | ... |

### 生成的客户 (8个)
- 张三、李四、王五、赵六、钱七、孙八、周九、吴十
- 包含完整的联系信息和地址

## 🔧 详细使用说明

### 数据生成脚本功能

`generate_sample_data.py` 脚本提供完整的数据管理功能：

#### 1. 自动数据库设置
- 创建和应用迁移文件
- 初始化数据库表结构

#### 2. 样本数据生成
- **商品分类**: 电子产品、家用电器、服装鞋帽等7个分类
- **产品数据**: iPhone、MacBook、冰箱、洗衣机等20个产品
- **客户数据**: 张三、李四、王五等8个客户信息

#### 3. 管理员账户创建
自动创建默认管理员账户，无需手动操作。

### 手动操作（可选）

如果自动脚本遇到问题，可以手动执行以下步骤：

```bash
# 1. 创建迁移文件
python manage.py makemigrations sample_data

# 2. 应用迁移
python manage.py migrate

# 3. 创建超级用户
python manage.py createsuperuser

# 4. 运行数据生成（仅数据）
python generate_sample_data.py
```

### 管理面板功能

登录管理面板后，您可以：

1. **查看数据**
   - 浏览所有分类、产品和客户
   - 使用搜索和过滤功能

2. **管理数据**
   - 添加新的记录
   - 编辑现有记录
   - 删除不需要的记录

3. **数据统计**
   - 查看各模型的记录数量
   - 监控数据变化

## ⚙️ 自定义配置

### 修改数据库设置

编辑 `sample_data/settings.py` 中的 `DATABASES` 部分，可以配置其他数据库：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 添加新的数据模型

1. 在 `sample_data/models.py` 中定义新模型
2. 在 `sample_data/admin.py` 中注册到管理面板
3. 运行 `python manage.py makemigrations` 和 `python manage.py migrate`
4. 更新数据生成脚本以包含新模型的样本数据

### 扩展数据生成

修改 `generate_sample_data.py` 中的相应函数来：
- 添加更多样本数据
- 修改现有数据格式
- 添加数据验证逻辑

## 🐛 故障排除

### 常见问题

1. **"no such table" 错误**
   - 解决方案：运行 `python manage.py migrate`

2. **语言设置错误**
   - 解决方案：确保 `settings.py` 中的 `LANGUAGE_CODE` 设置为 `zh-hans` 或 `en-us`

3. **端口被占用**
   - 解决方案：使用其他端口 `python manage.py runserver 8000`

4. **管理员账户已存在**
   - 解决方案：脚本会自动检测并跳过创建已存在的账户

### 重新开始

如果需要完全重新开始：

```bash
# 删除数据库文件
rm db.sqlite3

# 重新运行数据生成脚本
python generate_sample_data.py
```

## 💻 开发说明

### 代码结构

- **models.py**: 数据模型定义，使用Django ORM
- **admin.py**: 管理面板配置，自定义显示字段和过滤选项
- **generate_sample_data.py**: 主要的数据生成逻辑
- **settings.py**: 项目配置，包含数据库、语言、时区等设置

### 数据完整性

系统确保：
- 外键关系的正确性
- 唯一约束的遵守（如客户邮箱）
- 数据格式的正确性（如价格使用Decimal类型）

### 扩展建议

- 添加订单和订单项模型
- 实现数据导入/导出到CSV格式
- 添加数据验证和清洗功能
- 实现数据备份和恢复功能

## 📝 作业要求完成情况

- ✅ 为至少3个Django资料模型建立样本资料记录
- ✅ 清理原始资料功能
- ✅ 格式化资料集
- ✅ 资料汇入和汇出到Django资料库
- ✅ 可在Django管理面板下检查结果

## 📄 许可证

本项目仅供学习和教育用途。

## ❓ 支持

如果您在使用过程中遇到任何问题，请检查：
1. Python和Django版本是否符合要求
2. 数据库迁移是否成功执行
3. 所有必要文件是否存在于正确的位置

---

**开始使用**: 运行 `python generate_sample_data.py` 即可体验完整的样本数据生成系统！

## 👥 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目。

## 📞 联系信息

- 开发者: Franco Ho
- GitHub: [francoho314](https://github.com/francoho314)
- 项目地址: [erb_homework2](https://github.com/francoho314/erb_homework2)
