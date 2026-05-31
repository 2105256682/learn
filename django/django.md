# Django 教程

---

## 一、Django 介绍

Django，发音为 `[dʒæŋɡəʊ]`，诞生于 2003 年秋天，2005 年发布正式版本，由 Simon 和 Andrian 开发。当时两位作者的老板和记者要他们几天甚至几个小时之内增加新的功能。两人不得已开发了 Django 这套框架以实现快速开发目的，因此 Django 生来就是为了节省开发者时间的。

Django 发展至今，被许许多多国内外的开发者使用，已经成为 Web 开发者的首选框架。因此，如果你是用 Python 来做网站或 App 后端，没有理由不学好 Django。

### Django 的特点

| 特点 | 说明 |
|------|------|
| **快速开发** | 开箱即用的 Web 框架，集成了数据库处理、HTML 渲染、Admin 系统、发送邮件、登录鉴权等功能 |
| **安全性高** | 内置 SQL 注入防护、CSRF 攻击防护、点击劫持防护等常见 Web 安全问题处理 |
| **可伸缩性强** | 全球很多大型网站都使用 Django 开发，能快速灵活地调整硬件来满足不同的流量需求 |

### 相关网址

| 名称 | 地址 |
|------|------|
| GitHub 源代码 | https://github.com/django/django |
| Django 官网 | https://www.djangoproject.com/ |

### 使用 Django 开发的知名网站

#### 国外

| 网站 | 说明 |
|------|------|
| Instagram | 全球知名的图片社交平台，使用 Django 开发后端，通过 Django REST framework 提供 API |
| Pinterest | 图片分享社交平台，使用 Django 开发 |
| Mozilla | 非营利组织，推广开放式 Web 标准，使用 Django 管理网站后端 |
| The Washington Post | 美国知名媒体，使用 Django 开发网站后端，并在 GitHub 上开源了一些 Django 应用 |
| Bitbucket | 代码托管平台，由 Atlassian 公司提供支持，采用 Django 开发后端 |
| Disqus | 广泛使用的第三方评论系统，使用 Django 开发 |
| Spotify | 流行的音乐流媒体平台，使用 Django 开发后端 |

#### 国内

腾讯、阿里巴巴、百度、字节跳动等，在某些模块或功能上都在使用 Django。

> 更多使用 Django 开发的网站请参考：https://builtwithdjango.com/projects/

---

## 二、学前准备

### 1. 安装 Python 3.12+

确保已经安装 Python 3.12 以上的版本，本教程以 Python 3.12 版本进行讲解。

- 下载地址：https://www.python.org/downloads/release/python-3120/

### 2. 安装 Django

```bash
pip install django
```

本教程以 Django 5.0.3 版本为例进行讲解。

### 3. 安装编辑器

推荐使用 PyCharm Professional（专业版），如果由于电脑性能原因，可以退而求其次使用 VSCode。

> **注意**：如果使用 PyCharm，切记一定要下载 **Professional（专业版）**，Community（社区版）不能用于网页开发。

- PyCharm 下载链接：https://www.jetbrains.com/pycharm/download/?section=windows

---

## 三、URL 组成部分详解

URL 是 **Uniform Resource Locator** 的简写，统一资源定位符。

### URL 结构

```
scheme://host:port/path/?query-string=xxx#anchor
```

### 各部分说明

| 组成部分 | 说明 | 示例 |
|----------|------|------|
| `scheme` | 访问协议，一般为 `http`、`https` 或 `ftp` | `https://` |
| `host` | 主机名 / 域名 | `www.baidu.com` |
| `port` | 端口号，HTTP 默认 80，HTTPS 默认 443 | `:8080` |
| `path` | 查找路径 | `/trending/now` |
| `query-string` | 查询字符串 | `?wd=python` |
| `anchor` | 锚点，前端页面定位用（后台一般不用管） | `#section1` |

> **注意**：URL 中的所有字符都是 ASCII 字符集，如果出现非 ASCII 字符（如中文），浏览器会进行编码再进行传输。

---

## 四、第一个 Django 项目

### 1. 创建 Django 项目

#### 方式一：命令行

```bash
# 创建项目
django-admin startproject [项目名称]

# 示例
django-admin startproject first_project

# 创建应用（app）
# 在终端进入到项目所在的路径，然后执行：
python manage.py startapp [app名称]
```

#### 方式二：PyCharm

用 PyCharm 新建一个 Django 项目即可。

> 使用 PyCharm 创建完项目后，还是需要重新进入到命令行单独创建 app。

### 2. 运行 Django 项目

```bash
# 默认方式，端口号为 8000
python manage.py runserver
# 访问：http://127.0.0.1:8000/

# 指定端口号
python manage.py runserver 9000

# 允许其他电脑访问（指定 IP 为 0.0.0.0）
python manage.py runserver 0.0.0.0:8000
```

> PyCharm 中可以直接点击右上角的绿色箭头按钮运行。

### 3. 项目结构介绍

| 文件 | 说明 |
|------|------|
| `manage.py` | 与项目交互的核心文件，使用 `python manage.py [子命令]` 操作。一般不要编辑它 |
| `settings.py` | 本项目的设置项，所有项目相关的配置都放在这里 |
| `urls.py` | 配置 URL 路由，如 `http://127.0.0.1/news/` 访问什么页面 |
| `wsgi.py` | 项目与 WSGI 协议兼容的 Web 服务器入口，部署时使用，一般不需修改 |

### 4. Project 和 App 的关系

- **App** 是 Django 项目的组成部分，一个 App 代表项目中的一个模块
- 所有 URL 请求的响应都是由 App 来处理
- 例如：豆瓣有图书、电影、音乐、同城等模块 —— 在 Django 的角度来看，图书、电影这些模块就是 App
- **一个 Django 项目由许多 App 组成，一个 App 可以被用到其他项目**

```bash
python manage.py startapp book
```

---

## 五、URL 分发器

### 1. 视图（View）

视图一般都写在 App 的 `views.py` 中，第一个参数永远是 `request`（一个 `HttpRequest` 对象）。

视图函数的返回结果必须是 `HttpResponseBase` 对象或者子类的对象。

```python
from django.http import HttpResponse

def book_list(request):
    return HttpResponse("书籍列表！")
```

> 视图可以是函数，也可以是类。我们先学函数视图，后面再学类视图。

### 2. URL 映射

在用户输入某个 URL 请求到我们的网站时，Django 会从项目的 `urls.py` 文件中寻找对应的视图。

`urlpatterns` 变量中的匹配规则需要使用 `django.urls.path` 函数进行包裹：

```python
from django.contrib import admin
from django.urls import path
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', views.book_list)
]
```

#### URL 中添加参数

在 `path` 函数中使用尖括号的形式来定义动态参数：

```python
from django.contrib import admin
from django.urls import path
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', views.book_list),
    path('book/<book_id>', views.book_detail)
]
```

views.py 中的代码：

```python
def book_detail(request, book_id):
    text = "您输入的书籍的id是：%s" % book_id
    return HttpResponse(text)
```

#### 指定参数类型

```python
path("book/<int:book_id>", views.book_detail)
```

Django 的 `path` 支持的类型：

| 类型 | 说明 |
|------|------|
| `str` | 非空的字符串类型（默认），不能包含斜杠 |
| `int` | 匹配任意零或正数的整型 |
| `slug` | 由英文的横杠 `-` 或下划线 `_` 连接英文字符或数字而成的字符串 |
| `uuid` | 匹配 UUID 字符串 |
| `path` | 匹配非空的英文字符串，可以包含斜杠 `/` |

#### 查询字符串方式传参

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', views.book_list),
    path('book/detail', views.book_detail)
]
```

views.py：

```python
def book_detail(request):
    book_id = request.GET.get("id")
    text = "您输入的书籍id是：%s" % book_id
    return HttpResponse(text)
```

访问方式：`/book/detail?id=1`

### 3. path 函数详解

```python
path(route, view, name=None, kwargs=None)
```

| 参数 | 说明 |
|------|------|
| `route` | URL 的匹配规则，通过 `<>` 尖括号指定动态参数，可指定数据类型如 `<int:id>` |
| `view` | 视图函数、类视图 `.as_view()` 或 `django.urls.include()` 函数的返回值 |
| `name` | 给这个 URL 取个名字，项目大、URL 多的时候用处很大 |
| `kwargs` | 额外的关键字参数 |

### 4. URL 中包含另外一个 urls 模块

使用 `include` 函数，在 App 内部包含自己的 URL 匹配规则：

```python
# startdjango/urls.py 文件：
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include("book.urls"))
]

# book/urls.py 文件：
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.book_list),
    path('detail/<book_id>/', views.book_detail)
]
```

访问书列表：`/book/list/`，访问书籍详情：`/book/detail/<id>/`

#### 应用命名空间

```python
# book/urls.py 文件：
app_name = 'book'

urlpatterns = [
    path('list/', views.book_list),
    path('detail/<book_id>/', views.book_detail)
]
```

### 5. URL 反转

通过 `reverse` 函数从视图函数反查 URL：

```python
reverse("list")
# > /book/list/

reverse('book:list')
# > /book/list/

reverse("book:detail", kwargs={"book_id": 1})
# > /book/detail/1

# 添加查询字符串参数需要手动拼接
login_url = reverse('login') + "?next=/"
```

---

## 六、模板

### 1. DTL 与普通 HTML 文件的区别

DTL（Django Template Language）模板是一种带有特殊语法的 HTML 文件，可以被 Django 编译，传递参数进去，实现数据动态化。编译完成后生成普通 HTML 文件发送给客户端。

### 2. 渲染模板

#### 方式一：render_to_string

```python
from django.template.loader import render_to_string
from django.http import HttpResponse

def book_detail(request, book_id):
    html = render_to_string("detail.html")
    return HttpResponse(html)
```

#### 方式二：render（推荐）

```python
from django.shortcuts import render

def book_list(request):
    return render(request, 'list.html')
```

### 3. 模板查找路径配置

在 `settings.py` 中的 `TEMPLATES` 配置：

| 配置项 | 说明 |
|--------|------|
| `DIRS` | 存放模板路径的列表，`render` 或 `render_to_string` 会在这些路径中查找模板 |
| `APP_DIRS` | 默认为 `True`，会在 `INSTALLED_APPS` 中已安装 App 下的 `templates` 文件夹中查找模板 |

**查找顺序**：先查 `DIRS` 列表 → 当前 App 的 `templates` → 其他已安装 App 的 `templates` → 都没找到则抛出 `TemplateDoesNotExist` 异常。

---

## 七、DTL 模板语法

### 1. 变量

变量通过视图函数传递 `context` 参数（字典类型）：

```python
# views.py 代码
def profile(request):
    return render(request, 'profile.html', context={'username': '知了课堂'})
```

```html
<!-- profile.html 模板代码 -->
<p>{{ username }}</p>
```

#### 点（`.`）语法解析规则

对于 `person.username` 的解析：

1. 如果 `person` 是字典 → 查找 `username` 这个 key 的值
2. 如果 `person` 是对象 → 查找 `username` 属性或方法
3. 如果 `person.1` → 判断是否为列表/元组，取其第 1 个值

> **注意**：
> - 不能通过中括号访问字典和列表（`dict['key']` 和 `list[1]` 不支持）
> - 给字典添加 key 时不能和字典的属性重复（如 `items`）

### 2. 常用模板标签

#### if 标签

```django
{% if "张三" in persons %}
    <p>张三</p>
{% else %}
    <p>李四</p>
{% endif %}
```

支持的运算符：`==`、`!=`、`<`、`<=`、`>`、`>=`、`in`、`not in`、`is`、`is not`

#### for...in... 标签

```django
{% for person in persons %}
    <p>{{ person.name }}</p>
{% endfor %}
```

反向遍历：

```django
{% for person in persons reversed %}
```

遍历字典：

```django
{% for key, value in person.items %}
    <p>key：{{ key }}</p>
    <p>value：{{ value }}</p>
{% endfor %}
```

##### for 循环内置变量

| 变量 | 说明 |
|------|------|
| `forloop.counter` | 当前循环的下标，以 1 为起始值 |
| `forloop.counter0` | 当前循环的下标，以 0 为起始值 |
| `forloop.revcounter` | 当前循环的反向下标值，最后一个元素的下标为 1 |
| `forloop.revcounter0` | 当前循环的反向下标值，最后一个元素的下标为 0 |
| `forloop.first` | 是否是第一次遍历 |
| `forloop.last` | 是否是最后一次遍历 |
| `forloop.parentloop` | 嵌套循环中，代表上一级的 for 循环 |

#### for...in...empty 标签

```django
{% for person in persons %}
    <li>{{ person }}</li>
{% empty %}
    暂时还没有任何人
{% endfor %}
```

#### with 标签

```django
{% with lisi=persons.1 %}
    <p>{{ lisi }}</p>
{% endwith %}
```

另一种写法：

```django
{% with persons.1 as lisi %}
    <p>{{ lisi }}</p>
{% endwith %}
```

> **注意**：`with` 中定义的变量只能在 `{%with%}{%endwith%}` 中使用；等号两边不能有空格。

#### url 标签

```django
<a href="{% url 'book:list' %}">图书列表页面</a>

<!-- 使用位置参数 -->
<a href="{% url 'book:detail' 1 %}">图书详情页面</a>

<!-- 使用关键字参数 -->
<a href="{% url 'book:detail' book_id=1 %}">图书详情页面</a>

<!-- 多个参数用空格分隔 -->
<a href="{% url 'book:detail' book_id=1 page=2 %}">图书详情页面</a>

<!-- 查询字符串参数需手动添加 -->
<a href="{% url 'book:detail' book_id=1 %}?page=1">图书详情页面</a>
```

#### spaceless 标签

移除 HTML 标签中的空白字符（空格、tab、换行等）：

```django
{% spaceless %}
    <p>
        <a href="foo/">Foo</a>
    </p>
{% endspaceless %}
<!-- 渲染结果：<p><a href="foo/">Foo</a></p> -->
```

> 只会移除 HTML 标签之间的空白字符，不会移除标签与文本之间的空白字符。

#### autoescape 标签

```django
context = {"info": "<a href='www.baidu.com'>百度</a>"}

<!-- 关闭自动转义 -->
{% autoescape off %}
    {{ info }}
{% endautoescape %}

<!-- 开启自动转义 -->
{% autoescape on %}
    {{ info }}
{% endautoescape %}
```

#### verbatim 标签

在 `verbatim` 标签中的内容不会被 DTL 解析引擎处理：

```django
{% verbatim %}
    {{if dying}}Still alive.{{/if}}
{% endverbatim %}
```

> 更多标签请参考官方文档：https://docs.djangoproject.com/en/5.0/ref/templates/builtins/

---

## 八、模板常用过滤器

过滤器使用 `|` 来使用，格式：`{{ value|过滤器名称 }}`

### 常用过滤器列表

#### add

将传入的参数添加到原来的值上。优先尝试转换为整型相加，失败则拼接为字符串。

```django
{{ value|add:"2" }}
```

#### cut

移除值中所有指定的字符串，类似于 Python 中的 `replace(args, "")`。

```django
{{ value|cut:" " }}
```

#### date

将日期按指定格式格式化：

```django
{{ birthday|date:"Y/m/d" }}
```

##### 日期格式化字符

| 格式字符 | 描述 | 示例 |
|----------|------|------|
| `Y` | 四位数字的年份 | 2018 |
| `m` | 两位数字的月份 | 01-12 |
| `n` | 月份，1-9 前面没有 0 前缀 | 1-12 |
| `d` | 两位数字的天 | 01-31 |
| `j` | 天，1-9 前面没有 0 前缀 | 1-31 |
| `g` | 小时，12 小时格式，无 0 前缀 | 1-12 |
| `h` | 小时，12 小时格式，有 0 前缀 | 01-12 |
| `G` | 小时，24 小时格式，无 0 前缀 | 1-23 |
| `H` | 小时，24 小时格式，有 0 前缀 | 01-23 |
| `i` | 分钟，有 0 前缀 | 00-59 |
| `s` | 秒，有 0 前缀 | 00-59 |

#### default

```django
{{ value|default:"nothing" }}
```

当值被评估为 `False`（如 `[]`、`""`、`None`、`{}`）时，使用默认值。

#### default_if_none

```django
{{ value|default_if_none:"nothing" }}
```

只有值是 `None` 时才使用默认值（空字符串不会触发）。

#### first / last

```django
{{ value|first }}   <!-- 返回第一个元素 -->
{{ value|last }}    <!-- 返回最后一个元素 -->
```

#### floatformat

```django
{{ 34.23234|floatformat }}    <!-- 34.2 -->
{{ 34.000|floatformat }}      <!-- 34 -->
{{ 34.23234|floatformat:3 }}  <!-- 34.232 -->
```

#### join

```django
{{ value|join:"/" }}   <!-- 结果：a/b/c -->
```

#### length

```django
{{ value|length }}
```

#### lower / upper

```django
{{ value|lower }}   <!-- 全部小写 -->
{{ value|upper }}   <!-- 全部大写 -->
```

#### random

```django
{{ value|random }}   <!-- 从列表中随机选一个 -->
```

#### safe

标记字符串是安全的，关闭自动转义：

```django
{{ value|safe }}
```

#### slice

```django
{{ some_list|slice:"2:" }}
```

#### striptags

删除字符串中所有的 HTML 标签：

```django
{{ "<strong>hello</strong>"|striptags }}   <!-- hello -->
```

#### truncatechars

```django
{{ value|truncatechars:5 }}   <!-- "北京欢迎您~" → "北京..." -->
```

#### truncatechars_html

类似于 `truncatechars`，但不会切割 HTML 标签。

---

## 九、模板结构

### 1. include 模板

抽取重复使用的代码，类似于 Python 中的函数：

```django
<!-- header.html -->
<p>我是header</p>

<!-- footer.html -->
<p>我是footer</p>

<!-- main.html -->
{% include 'header.html' %}
<p>我是main内容</p>
{% include 'footer.html' %}
```

传递额外参数：

```django
{% include "header.html" with username='huangyong' %}
```

### 2. 模板继承

父模板 `base.html`：

```django
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="{% static 'style.css' %}" />
    <title>{% block title %}我的站点{% endblock %}</title>
</head>
<body>
    <div id="sidebar">
        {% block sidebar %}
        <ul>
            <li><a href="/">首页</a></li>
            <li><a href="/blog/">博客</a></li>
        </ul>
        {% endblock %}
    </div>
    <div id="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

子模板：

```django
{% extends "base.html" %}

{% block title %}博客列表{% endblock %}

{% block content %}
    {% for entry in blog_entries %}
        <h2>{{ entry.title }}</h2>
        <p>{{ entry.body }}</p>
    {% endfor %}
{% endblock %}
```

> **注意**：
> - `extends` 标签必须放在模版的第一行
> - 子模板中的代码必须放在 `block` 中，否则不会被渲染
> - 使用 `{{ block.super }}` 可以继承父模板的内容
> - 可在 block 结束处定义名字：`{% block title %}{% endblock title %}`

---

## 十、加载静态文件

### 配置步骤

**1.** 确保 `django.contrib.staticfiles` 已添加到 `settings.INSTALLED_APPS` 中。

**2.** 在 `settings.py` 中设置 `STATIC_URL`：

```python
STATIC_URL = 'static/'
```

**3.** 在已安装的 App 下创建 `static` 文件夹，再在其下创建与当前 App 同名的文件夹（避免多 App 间静态文件名冲突）：

```
book/static/book/zhiliao.jpg
```

**4.** 如果静态文件不跟任何 App 挂钩，在 `settings.py` 中添加：

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
```

**5.** 在模板中加载：

```django
{% load static %}
<link rel="stylesheet" href="{% static 'style.css' %}">
```

**6.** 不想每次都手动 `load`，可在 `settings.py` 的 `TEMPLATES/OPTIONS` 中添加：

```python
'builtins': ['django.templatetags.static']
```

### 媒体文件配置

```python
# settings.py
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
```

```python
# urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

> **注意**：静态文件和媒体文件，最好通过 Nginx 等专业的 Web 服务器来部署，以上方式仅在开发阶段使用。

---

## 十一、MySQL 数据库

### 1. 安装

- MySQL 官网：https://dev.mysql.com/downloads/mysql/
- 如提示缺少 .NET Framework 或 Microsoft Visual C++，请根据提示安装

### 2. Navicat 数据库操作软件

官网：https://www.navicat.com.cn/products

### 3. MySQL 驱动程序

```bash
pip install mysqlclient
```

#### 常见 MySQL 驱动对比

| 驱动 | 说明 |
|------|------|
| `MySQL-python`（MySQLdb） | C 语言操作 MySQL 的封装，只支持 Python2 |
| `mysqlclient` | MySQL-python 的分支，支持 Python3，修复了部分 bug |
| `pymysql` | 纯 Python 实现，执行效率不如 mysqlclient |
| `MySQL Connector/Python` | MySQL 官方纯 Python 驱动，效率不高 |

---

## 十二、操作数据库

### 1. Django 配置连接数据库

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',    # 数据库引擎
        'NAME': 'dfz',                             # 数据库名称
        'USER': 'root',                            # 用户名
        'PASSWORD': 'root',                        # 密码
        'HOST': '127.0.0.1',                       # 主机地址
        'PORT': '3306',                            # 端口号
    }
}
```

支持的引擎：

| 引擎 | 数据库 |
|------|--------|
| `django.db.backends.postgresql` | PostgreSQL |
| `django.db.backends.mysql` | MySQL |
| `django.db.backends.sqlite3` | SQLite |
| `django.db.backends.oracle` | Oracle |

### 2. 使用原生 SQL 操作数据库

```python
from django.db import connection

# 获取游标对象
cursor = connection.cursor()

# 执行 SQL 语句
cursor.execute("select * from book")

# 获取所有数据
rows = cursor.fetchall()

for row in rows:
    print(row)
```

### 3. Python DB API cursor 常用接口

| 属性/方法 | 说明 |
|-----------|------|
| `description` | 返回列信息列表：`(name, type_code, display_size, ...)` |
| `rowcount` | SQL 语句执行后受影响的行数 |
| `close()` | 关闭游标 |
| `execute(sql, parameters)` | 执行 SQL 语句，参数化查询 |
| `fetchone()` | 获取第一条数据 |
| `fetchmany(size)` | 获取多条数据 |
| `fetchall()` | 获取所有数据 |

---

## 十三、ORM 模型

### 1. ORM 模型介绍

ORM（**O**bject **R**elational **M**apping，对象关系映射）通过类的方式操作数据库，无需写原生 SQL。

**为什么使用 ORM？**

| 传统 SQL 的问题 | ORM 的优势 |
|-----------------|------------|
| SQL 语句重复利用率不高 | 减少重复 SQL，代码直观清晰 |
| 业务逻辑中拼 SQL，修改困难 | 设计灵活，轻松写出复杂查询 |
| 容易忽略 Web 安全问题（SQL 注入） | 封装了底层安全处理 |
| 换数据库需大量修改 | 可移植性强，轻松切换数据库 |

### 2. 创建 ORM 模型

```python
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=20, null=False)
    author = models.CharField(max_length=20, null=False)
    pub_time = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)
```

> 如果没有定义主键，Django 会自动生成一个名为 `id` 的自增整型主键。

### 3. 映射模型到数据库

1. 在 `settings.py` 中配置好 `DATABASES`
2. 在 App 的 `models.py` 中定义模型（必须继承 `django.db.models.Model`）
3. 将 App 添加到 `settings.py` 的 `INSTALLED_APPS` 中
4. 在命令行执行：
   ```bash
   python manage.py makemigrations   # 生成迁移脚本文件
   python manage.py migrate           # 将迁移脚本映射到数据库中
   ```

---

## 十四、模型常用 Field 和参数

### 1. 常用字段

| 字段 | 数据库类型 | 说明 |
|------|-----------|------|
| `AutoField` | `int` | 自动增长，一般不手动使用 |
| `BigAutoField` | 64位整型 | 范围 1 ~ 9223372036854775807 |
| `BooleanField` | `tinyint` | 接收 `True`/`False` |
| `CharField` | `varchar` | 必须指定 `max_length` |
| `DateField` | `date` | 日期类型，支持 `auto_now` 和 `auto_now_add` |
| `DateTimeField` | `datetime` | 日期时间类型 |
| `TimeField` | `time` | 时间类型 |
| `EmailField` | `varchar(254)` | 邮箱字段 |
| `FileField` | - | 存储文件 |
| `ImageField` | - | 存储图片文件 |
| `FloatField` | `float` | 浮点类型 |
| `IntegerField` | `int` | 范围 -2147483648 ~ 2147483647 |
| `BigIntegerField` | `bigint` | 大整型 |
| `PositiveIntegerField` | `int` | 正整型，0 ~ 2147483647 |
| `SmallIntegerField` | `smallint` | 小整型，-32768 ~ 32767 |
| `PositiveSmallIntegerField` | `smallint` | 正小整型 |
| `TextField` | `longtext` | 大量文本 |
| `UUIDField` | - | UUID 格式字符串 |
| `URLField` | `varchar(200)` | URL 格式字符串 |

### 2. Field 常用参数

| 参数 | 说明 |
|------|------|
| `null` | 数据库级别是否允许为空（默认 `False`）。字符串字段保持默认即可 |
| `blank` | 表单验证级别是否允许为空（默认 `False`） |
| `db_column` | 在数据库中的字段名 |
| `default` | 默认值，可为一个值或函数（不支持 lambda） |
| `primary_key` | 是否为主键（默认 `False`） |
| `unique` | 字段值是否唯一 |

> 更多参数参考：https://docs.djangoproject.com/zh-hans/5.0/ref/models/fields/

### 3. 模型中 Meta 配置

```python
class Book(models.Model):
    name = models.CharField(max_length=20, null=False)
    desc = models.CharField(max_length=100, name='description', db_column="description1")

    class Meta:
        db_table = 'book_model'        # 指定表名
        ordering = ['pub_date']        # 默认排序方式
```

更多配置参考：https://docs.djangoproject.com/zh-hans/5.0/ref/models/options/

---

## 十五、外键和表关系

### 1. 外键（ForeignKey）

```python
class ForeignKey(to, on_delete, **options)
```

```python
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey("User", on_delete=models.CASCADE)
```

使用示例：

```python
article = Article(title='abc', content='123')
author = User(username='张三', password='111111')
article.author = author
article.save()

# 修改外键值
article.author.username = '李四'
article.save()
```

引用其他 App 的模型：

```python
author = models.ForeignKey("user.User", on_delete=models.CASCADE)
```

引用自身：

```python
origin_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
```

### 2. 外键删除操作（on_delete）

| 选项 | 说明 |
|------|------|
| `CASCADE` | 级联删除：外键数据被删除，本条数据也被删除 |
| `PROTECT` | 受保护：只要被引用就不能删除 |
| `SET_NULL` | 设置为空（需字段允许 `null=True`） |
| `SET_DEFAULT` | 设置默认值（需设置 `default`） |
| `SET()` | 设置为指定值，可传入可调用对象 |
| `DO_NOTHING` | 不采取任何行为，全看数据库级别的约束 |

### 3. 表关系

#### 一对多（多对一）

```python
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey("User", on_delete=models.CASCADE)
```

反向查询：

```python
user = User.objects.first()
articles = user.article_set.all()
```

#### 一对一

```python
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

class UserExtension(models.Model):
    birthday = models.DateTimeField(null=True)
    school = models.CharField(blank=True, max_length=50)
    user = models.OneToOneField("User", on_delete=models.CASCADE)
```

#### 多对多

```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField("Tag", related_name="articles")

class Tag(models.Model):
    name = models.CharField(max_length=50)
```

### 4. related_name 和 related_query_name

#### related_name

指定反向引用的名称：

```python
author = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, related_name='articles')

# 使用时
user.articles.all()
```

不想使用反向引用时：`related_name='+'`

#### related_query_name

指定反向过滤查询的名称：

```python
author = models.ForeignKey("User", on_delete=models.SET_NULL, null=True,
                           related_name='articles', related_query_name='article')

# 使用时
users = User.objects.filter(article__title='abc')
```

---

## 十六、CRUD 操作

### 1. 添加

```python
book = Book(name='三国演义', desc='三国英雄！')
book.save()
```

### 2. 查找

```python
# 查找所有
books = Book.objects.all()

# 过滤
books = Book.objects.filter(name='三国演义')
books = Book.objects.filter(name='三国演义', desc='test')   # 多个条件

# 获取单个对象
book = Book.objects.get(name='三国演义')    # 没找到抛出异常，返回多条也抛异常
```

### 3. 排序

```python
books = Book.objects.order_by("pub_date")      # 正序
books = Book.objects.order_by("-pub_date")     # 倒序
```

### 4. 修改

```python
book = Book.objects.get(name='三国演义')
book.pub_date = datetime.now()
book.save()
```

### 5. 删除

```python
book = Book.objects.get(name='三国演义')
book.delete()
```

---

## 十七、查询操作

### 1. 查询条件

查询条件使用 `field + __ + condition` 的方式指定。

| 条件 | 说明 | 示例 |
|------|------|------|
| `exact` | 精确匹配 `=` | `id__exact=14` |
| `iexact` | 不区分大小写的 `=` | `title__iexact='hello'` |
| `contains` | 大小写敏感的模糊查询 | `title__contains='hello'` |
| `icontains` | 大小写不敏感的模糊查询 | `title__icontains='hello'` |
| `in` | 在给定容器中 | `id__in=[1,2,3]` |
| `gt` | 大于 | `id__gt=4` |
| `gte` | 大于等于 | `id__gte=4` |
| `lt` | 小于 | `id__lt=10` |
| `lte` | 小于等于 | `id__lte=10` |
| `startswith` | 以某值开头（大小写敏感） | `title__startswith='hello'` |
| `istartswith` | 以某值开头（不区分大小写） | 同上 |
| `endswith` | 以某值结尾（大小写敏感） | `title__endswith='world'` |
| `iendswith` | 以某值结尾（不区分大小写） | 同上 |
| `range` | 在给定区间内 | `pub_date__range=(start, end)` |
| `date` | 按日期过滤 | `pub_date__date=date(2018,3,29)` |
| `year` | 按年份过滤 | `pub_date__year=2018` |
| `month` | 按月份过滤 | `pub_date__month=6` |
| `day` | 按日期过滤 | `pub_date__day=15` |
| `week_day` | 按星期几过滤（1=周日，7=周六） | `pub_date__week_day=2` |
| `time` | 按时间过滤 | `pub_date__time=time(12,12,12)` |
| `isnull` | 是否为空 | `pub_date__isnull=False` |
| `regex` | 正则表达式（大小写敏感） | `title__regex=r'^hello'` |
| `iregex` | 正则表达式（不区分大小写） | 同上 |

#### 跨表关联查询

```python
class Category(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=100, null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

# 查询标题包含 "hello" 的文章对应的所有分类
categories = Category.objects.filter(article__title__contains="hello")
```

### 2. 聚合函数

```python
from django.db.models import Avg, Count, Max, Min, Sum

# 平均值
result = Book.objects.aggregate(Avg('price'))
result = Book.objects.aggregate(my_avg=Avg('price'))

# 计数
result = Book.objects.aggregate(book_num=Count('id'))
result = Author.objects.aggregate(count=Count('email', distinct=True))

# 最大值 / 最小值
result = Author.objects.aggregate(Max('age'), Min('age'))

# 求和
result = Book.objects.annotate(total=Sum("bookstore__price")).values("name", "total")
```

### 3. aggregate 和 annotate 的区别

| 方法 | 说明 |
|------|------|
| `aggregate` | 返回使用聚合函数后的字段和值（全表聚合） |
| `annotate` | 在原来模型字段基础上添加聚合函数字段，使用当前模型主键进行 `GROUP BY` |

### 4. F 表达式和 Q 表达式

#### F 表达式

直接在数据库层面完成运算，无需将数据取出到 Python 内存中：

```python
from django.db.models import F

# 将所有员工工资增加 1000 元
Employee.objects.update(salary=F("salary") + 1000)

# 获取 name 和 email 相同的作者
authors = Author.objects.filter(name=F("email"))
```

#### Q 表达式

实现复杂的逻辑查询（`|` 或、`&` 且、`~` 非）：

```python
from django.db.models import Q

# 价格低于 10 元 或 评分低于 9 的图书
books = Book.objects.filter(Q(price__lte=10) | Q(rating__lte=9))

# id 等于 3
books = Book.objects.filter(Q(id=3))

# id 等于 3，或名字中包含 "记"
books = Book.objects.filter(Q(id=3) | Q(name__contains="记"))

# 价格大于 100，且书名中包含 "记"
books = Book.objects.filter(Q(price__gte=100) & Q(name__contains="记"))

# 书名包含 "记"，但 id 不等于 3
books = Book.objects.filter(Q(name__contains='记') & ~Q(id=3))
```

---

## 十八、QuerySet API

`模型名字.objects` 是一个 `django.db.models.manager.Manager` 对象，方法从 `QuerySet` 类中拷贝而来。

### 返回新的 QuerySet 的方法

| 方法 | 说明 |
|------|------|
| `filter()` | 将满足条件的数据提取出来 |
| `exclude()` | 排除满足条件的数据 |
| `annotate()` | 添加使用聚合函数的字段 |
| `order_by()` | 指定排序（倒序加负号 `-`） |
| `values()` | 指定提取哪些字段，返回字典 |
| `values_list()` | 指定提取哪些字段，返回元组。`flat=True` 扁平化 |
| `all()` | 获取 QuerySet 对象 |
| `select_related()` | 提前将关联数据提取出来（一对多/一对一） |
| `prefetch_related()` | 解决多对多和多对一关系的查询优化 |
| `defer()` | 延迟加载指定字段（过滤掉不查） |
| `only()` | 只加载指定字段 |

### 不返回 QuerySet 的方法

| 方法 | 说明 |
|------|------|
| `get()` | 获取单条数据（多条或多条不存在均报错） |
| `create()` | 创建并保存数据 |
| `get_or_create()` | 查找或创建，返回元组 `(对象, 是否创建)` |
| `bulk_create()` | 批量创建 |
| `count()` | 获取数量（比 `len()` 高效） |
| `first()` / `last()` | 获取第一条/最后一条 |
| `aggregate()` | 聚合函数 |
| `exists()` | 判断是否存在（比 `count()` 和直接判断更高效） |
| `distinct()` | 去重 |
| `update()` | 更新操作，不执行 `save()` 方法 |
| `delete()` | 删除操作 |

### QuerySet 触发 SQL 执行的时机

- **迭代遍历**时
- 使用**步长做切片**时
- 调用 **`len()`** 函数时
- 调用 **`list()`** 函数时
- 进行**布尔判断**时

---

## 十九、ORM 模型与表的同步

### 1. 迁移命令

```bash
# 生成迁移脚本
python manage.py makemigrations [app_label]
# 选项：--name（指定名字）、--empty（生成空迁移脚本）

# 映射迁移脚本到数据库
python manage.py migrate [app_label] [migrationname]
# 选项：--fake（标记为已应用但不执行）、--fake-initial（标记首次迁移为已应用）

# 查看迁移文件
python manage.py showmigrations

# 查看迁移文件的 SQL 语句
python manage.py sqlmigrate [app_label] [migrationname]
```

### 2. 迁移版本不一致的处理

**方法一**：用 `python manage.py migrate --fake [版本名字]` 标记为已映射。

**方法二**：删除 migrations 和 `django_migrations` 表中的相关记录 → 保持模型和数据库一致 → 重新生成迁移脚本 → `python manage.py migrate --fake-initial` 标记初始迁移为已应用。

### 3. 根据已有表自动生成模型

```bash
# 查看生成的模型代码
python manage.py inspectdb

# 保存到文件
python manage.py inspectdb > models.py

# 只转换指定表
python manage.py inspectdb article_article > models.py
```

**修正步骤**：

1. 修正模型名、所属 App
2. 外键引用改为字符串格式
3. 删除 `Meta` 下的 `managed=False`
4. 手动处理多对多关系，用 `ManyToManyField` 配合 `db_table` 替换中间表
5. 不要修改表名
6. 执行 `python manage.py makemigrations` → `python manage.py migrate --fake-initial`
7. 将 Django 核心表映射到数据库中

---

## 二十、ORM 查询作业

假设有以下 ORM 模型（Student / Course / Score / Teacher），实现以下查询：

### 题目与答案

**1. 查询平均成绩大于 60 分的同学的 id 和平均成绩：**

```python
rows = Student.objects.annotate(avg=Avg("score__number")).filter(avg__gte=60).values("id", "avg")
```

**2. 查询所有同学的 id、姓名、选课的数量、总成绩：**

```python
rows = Student.objects.annotate(
    course_nums=Count("score__course"),
    total_score=Sum("score__number")
).values("id", "name", "course_nums", "total_score")
```

**3. 查询姓"李"的老师的个数：**

```python
teacher_nums = Teacher.objects.filter(name__startswith="李").count()
```

**4. 查询没学过"黄老师"课的同学的 id、姓名：**

```python
rows = Student.objects.exclude(score__course__teacher__name="黄老师").values('id', 'name')
```

**5. 查询学过课程 id 为 1 和 2 的所有同学的 id、姓名：**

```python
rows = Student.objects.filter(score__course__in=[1, 2]).distinct().values('id', 'name')
```

**6. 查询学过"黄老师"所教的"所有课"的同学的学号、姓名：**

```python
rows = Student.objects.annotate(
    nums=Count("score__course", filter=Q(score__course__teacher__name='黄老师'))
).filter(nums=Course.objects.filter(teacher__name='黄老师').count()).values('id', 'name')
```

**7. 查询所有课程成绩小于 60 分的同学的 id 和姓名：**

```python
students = Student.objects.exclude(score__number__gt=60)
```

**8. 查询没有学全所有课的同学的 id、姓名：**

```python
students = Student.objects.annotate(
    num=Count(F("score__course"))
).filter(num__lt=Course.objects.count()).values('id', 'name')
```

**9. 查询所有学生的姓名、平均分，按照平均分从高到低排序：**

```python
students = Student.objects.annotate(avg=Avg("score__number")).order_by("-avg").values('name', 'avg')
```

**10. 查询各科成绩的最高和最低分：**

```python
courses = Course.objects.annotate(
    min=Min("score__number"), max=Max("score__number")
).values("id", 'name', 'min', 'max')
```

**11. 查询每门课程的平均成绩，按照平均成绩排序：**

```python
courses = Course.objects.annotate(avg=Avg("score__number")).order_by('avg').values('id', 'name', 'avg')
```

**12. 统计总共有多少女生，多少男生：**

```python
rows = Student.objects.aggregate(
    male_num=Count("gender", filter=Q(gender=1)),
    female_num=Count("gender", filter=Q(gender=2))
)
```

**13. 将"黄老师"的每一门课程都在原来的基础之上加 5 分：**

```python
rows = Score.objects.filter(course__teacher__name='黄老师').update(number=F("number") + 5)
```

**14. 查询两门以上不及格的同学的 id、姓名以及不及格课程数：**

```python
students = Student.objects.annotate(
    bad_count=Count("score__number", filter=Q(score__number__lt=60))
).filter(bad_count__gte=2).values('id', 'name', 'bad_count')
```

**15. 查询每门课的选课人数：**

```python
courses = Course.objects.annotate(student_nums=Count("score__student")).values('id', 'name', 'student_nums')
```

---

## 二十一、Django 限制请求 Method

### 常用请求 Method

| Method | 说明 |
|--------|------|
| `GET` | 向服务器索取数据，不更改服务器状态 |
| `POST` | 向服务器提交数据，会更改服务器状态 |

### 限制请求装饰器

```python
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe

@require_http_methods(["GET"])       # 只允许 GET
@require_GET                          # 只允许 GET（简写）
@require_POST                         # 只允许 POST（简写）
@require_safe                         # 只允许 GET 和 HEAD
```

---

## 二十二、页面重定向

| 类型 | HTTP 状态码 | 说明 |
|------|-------------|------|
| 永久性重定向 | 301 | 旧网址被废弃，如 `jingdong.com` → `jd.com` |
| 暂时性重定向 | 302 | 临时跳转，如未登录时跳转到登录页面 |

```python
from django.shortcuts import reverse, redirect

def profile(request):
    if request.GET.get("username"):
        return HttpResponse("%s，欢迎来到个人中心页面！")
    else:
        return redirect(reverse("user:login"))
```

---

## 二十三、WSGIRequest 对象

Django 接收到 HTTP 请求后，会根据携带的参数创建 `WSGIRequest` 对象，作为视图函数的第一个参数 `request`。

### 常用属性

| 属性 | 说明 |
|------|------|
| `path` | 请求的完整路径（不含域名和参数） |
| `method` | 请求方法（GET / POST） |
| `GET` | `QueryDict` 对象，包含 `?xxx=xxx` 参数 |
| `POST` | `QueryDict` 对象，包含 POST 参数 |
| `FILES` | `QueryDict` 对象，包含上传的文件 |
| `COOKIES` | 标准 Python 字典，包含所有 cookie |
| `session` | 用于操作服务器 session |
| `META` | 存储客户端发送的所有 header 信息 |

### META 常用 Key

| Key | 说明 |
|-----|------|
| `CONTENT_LENGTH` | 请求正文长度 |
| `CONTENT_TYPE` | 请求正文 MIME 类型 |
| `HTTP_ACCEPT` | 可接收的 Content-Type |
| `HTTP_ACCEPT_ENCODING` | 可接收的编码 |
| `HTTP_ACCEPT_LANGUAGE` | 可接收的语言 |
| `HTTP_HOST` | 客户端发送的 HOST 值 |
| `HTTP_REFERER` | 上一个页面的 URL |
| `QUERY_STRING` | 未解析的查询字符串 |
| `REMOTE_ADDR` | 客户端的 IP 地址 |
| `REMOTE_HOST` | 客户端主机名 |
| `REQUEST_METHOD` | 请求方法 |
| `SERVER_NAME` | 服务器域名 |
| `SERVER_PORT` | 服务器端口号 |

获取真实 IP 地址：

```python
if request.META.has_key('HTTP_X_FORWARDED_FOR'):
    ip = request.META['HTTP_X_FORWARDED_FOR']
else:
    ip = request.META['REMOTE_ADDR']
```

### 常用方法

| 方法 | 说明 |
|------|------|
| `is_secure()` | 是否采用 HTTPS 协议 |
| `get_host()` | 服务器域名（含端口号） |
| `get_full_path()` | 完整 path（含查询字符串） |
| `get_raw_uri()` | 请求的完整 URL |

### QueryDict 对象

```python
request.GET.get('key')           # 获取指定 key 的值
request.GET.getlist('key')       # 如果 key 对应多个值
```

---

## 二十四、HttpResponse 对象

### 常用属性

| 属性 | 说明 |
|------|------|
| `content` | 返回的内容 |
| `status_code` | HTTP 响应状态码 |
| `content_type` | MIME 类型，默认 `text/html` |

### 常用 Content-Type

| MIME 类型 | 说明 |
|-----------|------|
| `text/html` | HTML 文件（默认） |
| `text/plain` | 纯文本 |
| `text/css` | CSS 文件 |
| `text/javascript` | JS 文件 |
| `multipart/form-data` | 文件提交 |
| `application/json` | JSON 传输 |
| `application/xml` | XML 文件 |

### 设置请求头

```python
response['X-Access-Token'] = 'xxxx'
```

### 常用方法

| 方法 | 说明 |
|------|------|
| `set_cookie()` | 设置 cookie 信息 |
| `delete_cookie()` | 删除 cookie 信息 |
| `write()` | 写入数据到数据体 |

### JsonResponse 类

```python
from django.http import JsonResponse

# 字典
return JsonResponse({"username": "zhiliao", "age": 18})

# 非字典数据需设置 safe=False
persons = ['张三', '李四', '王五']
return JsonResponse(persons, safe=False)
```

---

## 二十五、生成 CSV 文件

### 生成小 CSV 文件

```python
import csv
from django.http import HttpResponse

def csv_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['username', 'age', 'height', 'weight'])
    writer.writerow(['zhiliao', '18', '180', '110'])
    return response
```

### 生成大 CSV 文件（StreamingHttpResponse）

```python
from django.http import StreamingHttpResponse

class Echo:
    def write(self, value):
        return value

def large_csv(request):
    rows = (["Row {}".format(idx), str(idx)] for idx in range(655360))
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse(
        (writer.writerow(row) for row in rows),
        content_type="text/csv"
    )
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    return response
```

> `StreamingHttpResponse` 会启动一个进程和客户端保持长连接，很消耗资源，非特殊要求尽量少用。

---

## 二十六、类视图

### 1. View

所有类视图的基类，根据请求 method 分发到对应方法：

```python
from django.views import View

class BookDetailView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'detail.html')
```

URL 映射：

```python
path("detail/<book_id>/", views.BookDetailView.as_view(), name='detail')
```

支持的 HTTP 方法：`get`、`post`、`put`、`patch`、`delete`、`head`、`options`、`trace`

未定义的方法会转发到 `http_method_not_allowed()`：

```python
def http_method_not_allowed(self, request, *args, **kwargs):
    return HttpResponse("您当前采用的method是：%s，本视图只支持使用post请求！" % request.method)
```

### 2. TemplateView

专门用来返回模板的类视图：

```python
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = "知了黄勇"
        return context
```

直接在 URLs 中渲染：

```python
path('about/', TemplateView.as_view(template_name="about.html"))
```

### 3. ListView

```python
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    paginate_by = 10
    context_object_name = 'articles'
    ordering = 'create_time'
    page_kwarg = 'page'

    def get_queryset(self):
        return Article.objects.filter(id__lte=89)
```

### 4. Paginator 和 Page 类

```python
from django.core.paginator import Paginator

paginator = Paginator(object_list, per_page)
page = paginator.page(number)
```

**Paginator 常用属性和方法：**

| 属性/方法 | 说明 |
|-----------|------|
| `count` | 总数据条数 |
| `num_pages` | 总页数 |
| `page_range` | 页面区间，如 `range(1, 4)` |

**Page 常用属性和方法：**

| 属性/方法 | 说明 |
|-----------|------|
| `has_next()` | 是否有下一页 |
| `has_previous()` | 是否有上一页 |
| `next_page_number()` | 下一页的页码 |
| `previous_page_number()` | 上一页的页码 |
| `number` | 当前页 |
| `start_index()` | 当前页第一条数据的索引 |
| `end_index()` | 当前页最后一条数据的索引 |

### 5. 给类视图添加装饰器

```python
from django.utils.decorators import method_decorator

# 方式一：装饰 dispatch 方法
@method_decorator(login_required)
def dispatch(self, request, *args, **kwargs):
    return super(IndexView, self).dispatch(request, *args, **kwargs)

# 方式二：装饰在整个类上
@method_decorator(login_required, name='dispatch')
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("index")
```

---

## 二十七、错误处理

### 常见 HTTP 错误码

| 状态码 | 说明 |
|--------|------|
| 400 | Bad Request，请求参数错误 |
| 403 | Forbidden，没有权限 |
| 404 | Not Found，服务器没有指定的 URL |
| 405 | Method Not Allowed，请求 method 错误 |
| 500 | Internal Server Error，服务器内部错误 |
| 502 | Bad Gateway，部署时的网关错误 |

### 自定义错误模板

在 `templates` 文件夹下创建相应错误代码的 HTML 模板文件即可（如 `404.html`、`500.html`）。

### 错误处理方案

- 对于 404 和 500 等自动抛出的错误：直接在 `templates` 文件夹下创建对应模板
- 对于其他错误：可以专门定义一个 App 来处理错误

---

## 二十八、表单

### 1. HTML 中的表单

```html
<form action="" method="post" enctype="multipart/form-data">
    <input type="file" name="myfile">
</form>
```

### 2. Django 中的表单

Django 表单主要做两件事：
- **渲染表单模板**
- **表单验证数据是否合法**

### 3. 表单使用流程

```python
# forms.py
from django import forms

class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=3, label='标题', min_length=2,
        error_messages={"min_length": '标题字符段不符合要求！'})
    content = forms.CharField(widget=forms.Textarea, label='内容')
    email = forms.EmailField(label='邮箱')
    reply = forms.BooleanField(required=False, label='回复')
```

```python
# views.py
class IndexView(View):
    def get(self, request):
        form = MessageBoardForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = MessageBoardForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            reply = form.cleaned_data.get('reply')
            return HttpResponse('success')
        else:
            print(form.errors)
            return HttpResponse('fail')
```

模板中渲染：

```django
<form action="" method="post">
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input type="submit" value="提交"></td>
        </tr>
    </table>
</form>
```

---

## 二十九、表单验证

### 1. 常用 Field

| Field | 说明 | 常用参数 |
|-------|------|----------|
| `CharField` | 文本 | `max_length`, `min_length`, `required`, `error_messages` |
| `EmailField` | 邮件 | 自动验证邮件格式 |
| `FloatField` | 浮点 | `max_value`, `min_value` |
| `IntegerField` | 整型 | `max_value`, `min_value` |
| `URLField` | URL 格式字符串 | - |

### 2. 常用验证器（validators）

```python
from django.core import validators

class MyForm(forms.Form):
    telephone = forms.CharField(
        validators=[validators.RegexValidator("1[345678]\d{9}", message='请输入正确格式的手机号码！')]
    )
```

| 验证器 | 说明 |
|--------|------|
| `MaxValueValidator` | 最大值 |
| `MinValueValidator` | 最小值 |
| `MinLengthValidator` | 最小长度 |
| `MaxLengthValidator` | 最大长度 |
| `EmailValidator` | 邮箱格式 |
| `URLValidator` | URL 格式 |
| `RegexValidator` | 正则表达式 |

### 3. 自定义验证

对单个字段验证：

```python
def clean_telephone(self):
    telephone = self.cleaned_data.get('telephone')
    exists = User.objects.filter(telephone=telephone).exists()
    if exists:
        raise forms.ValidationError("手机号码已经存在！")
    return telephone
```

多字段联合验证：

```python
def clean(self):
    cleaned_data = super().clean()
    pwd1 = cleaned_data.get('pwd1')
    pwd2 = cleaned_data.get('pwd2')
    if pwd1 != pwd2:
        raise forms.ValidationError('两个密码不一致！')
    return cleaned_data
```

### 4. 提取错误信息

```python
form.errors                                    # 含 HTML 标签
form.errors.get_json_data()                    # 字典类型
form.as_json()                                 # JSON 字符串

# 自定义整理错误信息
def get_errors(self):
    errors = self.errors.get_json_data()
    new_errors = {}
    for key, message_dicts in errors.items():
        messages = [message['message'] for message in message_dicts]
        new_errors[key] = messages
    return new_errors
```

---

## 三十、ModelForm

### 1. 基本使用

将模型中的字段直接转换为表单验证：

```python
from django import forms
from .models import Article

class MyForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"                    # 所有字段
        # fields = ['title', 'content']       # 指定字段
        # exclude = ['category']              # 排除字段
```

### 2. 自定义错误消息

```python
class MyForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['category']
        error_messages = {
            'title': {
                'max_length': '最多不能超过10个字符！',
                'min_length': '最少不能少于3个字符！'
            },
            'content': {
                'required': '必须输入content！',
            }
        }
```

### 3. save 方法

```python
form = MyForm(request.POST)
if form.is_valid():
    form.save()                               # 直接保存
    return HttpResponse('success')

# 不完全保存
form = MyForm(request.POST)
if form.is_valid():
    article = form.save(commit=False)         # 只创建对象，不保存
    article.category = 'Python'               # 补充其他字段
    article.save()                            # 再保存
```

---

## 三十一、文件上传

### 1. 前端 HTML

```html
<form action="" method="post" enctype="multipart/form-data">
    <input type="file" name="myfile">
    <input type="submit" value="上传">
</form>
```

### 2. 后端处理

```python
def save_file(file):
    with open('somefile.txt', 'wb') as fp:
        for chunk in file.chunks():
            fp.write(chunk)

def index(request):
    if request.method == 'GET':
        form = MyForm()
        return render(request, 'index.html', {'form': form})
    else:
        myfile = request.FILES.get('myfile')
        save_file(myfile)
        return HttpResponse('success')
```

### 3. 使用模型处理文件上传

```python
# models.py
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.FileField(upload_to="files")
```

`upload_to` 支持日期格式：

```python
thumbnail = models.FileField(upload_to="%Y/%m/%d/")
```

### 4. MEDIA_ROOT 和 MEDIA_URL

```python
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

### 5. 限制上传文件扩展名

```python
from django.core import validators

thumbnail = models.FileField(
    upload_to='%Y/%m/%d/',
    validators=[validators.FileExtensionValidator(['txt', 'pdf'])]
)
```

### 6. 上传图片

```python
# models.py
class Article(models.Model):
    thumbnail = models.ImageField(upload_to="%Y/%m/%d/")

# forms.py
class MyForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
```

> **注意**：使用 `ImageField` 必须先安装 Pillow：`pip install pillow`

---

## 三十二、Cookie 和 Session

### 1. Cookie 介绍

- HTTP 请求是无状态的
- Cookie 的出现解决了"服务器识别当前用户"的问题
- 第一次登录后服务器返回 Cookie 给浏览器，浏览器保存；之后每次请求自动携带
- Cookie 存储数据量有限，一般不超过 4KB

### 2. Session 介绍

- Session 和 Cookie 目的类似，都用于存储用户相关信息
- Cookie 存储在本地浏览器，Session 是服务器存储授权信息的解决方案
- Session 的出现是为了解决 Cookie 存储数据不安全的问题

### 3. 两种常见存储方案

| 方案 | 说明 |
|------|------|
| **服务端 Session**（Server Side） | Cookie 存储 sessionid，数据存储在服务器（Django 默认存数据库） |
| **客户端 Session**（Client Side） | Session 数据加密后存储在 Cookie 中（Flask 默认方式） |

### 4. Django 中操作 Cookie

```python
# 设置 cookie
response.set_cookie(key, value, max_age=None, expires=None, path='/',
                     domain=None, secure=False, httponly=False)

# 删除 cookie
response.delete_cookie('key')

# 获取 cookie
cookies = request.COOKIES
for key, value in cookies.items():
    print(key, value)
```

**set_cookie 参数说明：**

| 参数 | 说明 |
|------|------|
| `key` | Cookie 的 key |
| `value` | Cookie 的 value |
| `max_age` | 最长生命周期（秒），超时后自动删除 |
| `expires` | 过期时间（具体日期），与 `max_age` 同时设置时优先使用 |
| `path` | 对哪个路径有效（默认所有路径） |
| `domain` | 对哪个域名有效（默认主域名） |
| `secure` | `True` 则仅 HTTPS 协议可用 |
| `httponly` | `True` 则客户端不能通过 JavaScript 操作 |

### 5. Django 中操作 Session

```python
# 获取
request.session.get('username')

# 删除
request.session.pop('key')

# 获取所有键/值
request.session.keys()
request.session.items()

# 清除当前用户 session 数据
request.session.clear()

# 删除 session 并删除浏览器中的 session_id（注销时使用）
request.session.flush()

# 设置过期时间
request.session.set_expiry(value)
```

**`set_expiry` 参数说明：**

| 值 | 说明 |
|----|------|
| 整型 | 多少秒后过期 |
| `0` | 浏览器关闭即过期 |
| `None` | 使用全局配置 `SESSION_COOKIE_AGE`（默认 1209600 秒 = 2 周） |

清除过期 Session：

```bash
python manage.py clearsessions
```

### 6. 修改 Session 存储机制

通过 `SESSION_ENGINE` 配置：

| 引擎 | 说明 |
|------|------|
| `django.contrib.sessions.backends.db` | 存储在数据库（默认） |
| `django.contrib.sessions.backends.file` | 存储在文件 |
| `django.contrib.sessions.backends.cache` | 存储在缓存（需配置 CACHES，推荐 Memcached） |
| `django.contrib.sessions.backends.cached_db` | 先缓存再数据库（容灾方案） |
| `django.contrib.sessions.backends.signed_cookies` | 加密存储在浏览器 Cookie（不超过 4KB） |

---

> **文档参考**：以上内容整理自 Django 入门教程，涵盖从项目创建到表单处理、数据库操作、部署配置等核心知识点。
