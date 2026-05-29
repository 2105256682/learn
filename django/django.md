Django介绍
Django，发音为[`dʒæŋɡəʊ]，Django诞生于2003 年秋天，2005 年发布正式版本，由Simon和Andrian
开发。当时两位作者的老板和记者要他们 天甚至 个小时之内增 新的功能。两人不得已开发了
Django这套框架以实现快速开发目的， 此Django生来就是为了节省开发者时间的。Django发展至今，
被许许多多国内外的开发者使用，已经成为web开发者的首选框架。 此，如果 是用python 来做网站
或app后端，没有理由不学好Django。Django具有以下特点：
1.快速开发。
Django是一个开箱即用的Web框架，包括了数据库处理、HTML渲染、Admin 系统、发
送邮件、登录鉴权等平时开发中 能想到的功能，他都已经集成好了，只要 学会了，以后开发的
速度是非常快的。
2.安全性高。
Django在安全方面做得非常完善，节省开发者处理安全的时间。比如SQL注入、CSRF攻
击，点击劫持等常见的Web安全问题，Django都已经处理好了。
3.可伸缩性强。世界上很多大型网站都是用
Django开发的，能快速和灵活的调整硬件来满足不同的流
量需求。
一、Django 相关的网址
1.
Github源代 ： https://github.com/django/django
2.
Django官网： https://www.djangoproject.com/
二、使用Django 开发的网站
1.
Instagram：全球知名的图片社交平台，使用Django开发后端，并通过Django REST framework提
供API。
2.
Pinterest：一个图片分享社交平台，也是使用Django开发的。
3.
Mozilla：一个非营利组织，旨在推广开放式Web 准，使用Django管理其网站的后端。
4.
The Washington Post ：美国知名媒体，利用Django开发网站的后端，同时也在GitHub 上开源了其
一些Django应用。
5.
Bitbucket：代 托管平台，由Atlassian公司提供支持，采用Django开发后端。
6.
Disqus：一个广泛使用的第三方评论系统，也是用Django开发的。
7.
Spotify：一个流行的音乐流媒体平台，使用Django开发后端。
国内包括有腾讯、阿里巴巴、百度、字节跳动等，在某些模块或功能上，都在使用Django。
更多使用Django开发的网站请参考： https://builtwithdjango.com/projects/
学前准备
在学 Django之前，需要做好以下准备工作。
一、安装Python3.12
确保已经安装 Python 3.12 以上的版本，教学以 Python 3.12 版本进行讲解。Python3.12 的下载路径
为：https://www.python.org/downloads/release/python-3120/
二、安装Django
通过pip install django 安装django，教学以 Django 5.0.3 版本为例进行讲解。
三、安装Pycharm专业版
安装pycharm profession 或者VSCode等任意一款 喜欢的编辑器。（推荐使用 pycharm ，如果由于
电脑性能原 ，可以退而求其次使用 VSCode）。如果使用 pycharm ，切记一定要下载profession （专
业版），community （社区版）不能用于网页开发。至于 解和正版，大家到网上搜下就知道啦。
Pycharm下载链接： https://www.jetbrains.com/pycharm/download/?section=windows
URL组成部分详解：
URL是Uniform Resource Locator 的简写，统一资源定位符。
一个URL由以下 部分组成：
scheme ：代表的是访问的协议，一般为 http或者https以及ftp等。
host：主机名，域名，比如 www.baidu.com 。
port：端口号。HTTP协议是80端口，HTTPS协议是443 端口。
path：查找路径。比如： www.jianshu.com/trending/now ，后面的 trending/now 就是path。
query-string：查询字符串，比如： www.baidu.com/s?wd=python ，后面的 wd=python 就是查询
字符串。
anchor：锚点，后台一般不用管，前端用来做页面定位的。
注意：URL中的所有字符都是 ASCII字符集，如果出现非 ASCII字符，比如中文，浏览器会进行编 再
进行 输。  scheme://host:port/path/?query-string=xxx#anchor
第一个Django 项目

一、创建Django 项目：
1. 用命令行的方式：
1. 创建项目：打开终端，使用命令： django-admin startproject [项目名称] 即可创建。比如：
django-admin startproject first_project 。
2. 创建应用（app）：一个项目类似于是一个架子，但是真正起作用的还是 app。在终端进入到项目
所在的路径，然后执行 python manage.py startapp [app名称] 创建一个app。

2. 用pycharm 的方式：
用pycharm 新建一个 Django项目，新建项目的截图如下：
使用pycharm 创建完项目后，还是需要重新进入到命令行单独创建 app的。

二、运行Django 项目：
1. 通过命令行的方式： python manage.py runserver 。这 可以在本地访问 的网站，默认端口号
是8000，这 就可以在浏览器中通过 http://127.0.0.1:8000/ 来访问 的网站啦。如果想要修
改端口号，那么在运行的时候可以指定端口号， python manage.py runserver 9000 这 就可以
通过9000端口来访问啦。另外，这 运行的项目只能在本机上能访问，如果想要在其他电脑上也
能访问本网站，那么需要指定 ip地址为0.0.0.0 。示例为： python manage.py runserver
0.0.0.0:8000 。
2. 通过pycharm 运行。直接点击右上角的绿色箭头按钮即可运行。

三、项目结构介绍：
1. manage.py ：以后和项目交互基本上都是基于这个文件。一般都是在终端输入 python manage.py
[子命令] 。可以输入 python manage.py help 看下能做什么事情。除非 知道 自己在做什么，
一般情况下不应该编辑这个文件。
2. settings.py ：本项目的设置项，以后所有和项目相关的配置都是放在这个里面。
3. urls.py ：这个文件是用来配置URL路由的。比如访问 http://127.0.0.1/news/ 是访问新闻列表
页，这些东西就需要在这个文件中完成。
4. wsgi.py ：项目与 WSGI协议兼容的 web服务器入口，部署的时候需要用到的，一般情况下也是不
需要修改的。

四、project和app的关系：
app是django项目的组成部分。一个 app代表项目中的一个模块，所有 URL请求的响应都是由 app来
处理。比如豆瓣，里面有图书，电影，音乐，同城等许许多多的模块，如果站在 django的角度来看，图
书，电影这些模块就是 app，图书，电影这些 app共同组成豆瓣这个项目。 此这里要有一个概念，
django项目由许多 app组成，一个 app可以被用到其他项目， django也能拥有不同的 app。通过命
令：
 python manage.py startapp book
URL分发器

一、视图：
视图一般都写在 app的views.py 中。并且视图的第一个参数永远都是 request （一个
HttpRequest）对象。这个对象存储了请求过来的所有信息，包括携带的参数以及一些头部信息等。在视
图中，一般是完成逻辑相关的操作。比如这个请求是添 一篇博客，那么可以通过request来接收到这些
数据，然后存储到数据库中，最后再把执行的结果返回给浏览器。视图函数的返回结果必须是
HttpResponseBase 对象或者子类的对象。示例代 如下：
视图可以是函数，也可以是类，我们先学 函数视图，后面再学 类视图。

二、URL 射：
视图写完后，要与URL进行 射，也即用户在浏览器中输入什么 url的时候可以请求到这个视图函
数。在用户输入了某个 url，请求到我们的网站的时候， django会从项目的 urls.py 文件中寻找对应
的视图。在 urls.py 文件中有一个 urlpatterns 变量，以后 django就会从这个变量中读取所有的匹配
规则。匹配规则需要使用 django.urls.path 函数进行包裹，这个函数会 据 入的参数返回
URLPattern 或者是URLResolver 的对象。示例代 如下：
1. URL中添 参数：
有时候， url中包含了一些参数需要动态调整。比如简书某篇文 的详情页的url，是
https://www.jianshu.com/p/a5aab9c4978e 后面的a5aab9c4978e 就是这篇文 的 id，那么简书的
文 详情页面的url就可以写成 https://www.jianshu.com/p/<id> ，其中id就是文 的id。那么如何在
django中实现这种需求呢。这时候我们可以在 path函数中，使用尖括号的形式来定义一个参数。比如
我现在想要获取一本书籍的详细信息，那么应该在 url中指定这个参数。示例代 如下：from django.http import HttpResponse
def book_list( request):
  return  HttpResponse ("书籍列表！")
from django.contrib import admin
from django.urls import path
from book import views
urlpatterns = [
  path( 'admin/', admin. site.urls),
  path( 'book/',views.book_list)
]
而views.py 中的代 如下：
在指定参数时，也可以指定参数的类型，比如以上 book_id 为整形，那么在定义 URL的时候，就可以使
用以下语法实现：
除了int类型，django的path部分还支持 str、slug、uuid、path类型。

当然，也可以通过查询字符串的方式 递一个参数过去。示例代 如下：
在views.py 中的代 如下：
以后在访问的时候就是通过 /book/detail?id=1 即可将参数 递过去。

2. path函数：
path函数的定义为： path(route,view,name=None,kwargs=None) 。以下对这 个参数进行讲解。from django.contrib import admin
from django.urls import path
from book import views
urlpatterns = [
  path( 'admin/', admin. site.urls),
  path( 'book/',views.book_list),
  path( 'book/<book_id>', views.book_detail)
]
def book_detail( request,book_id):
  text = "您输入的书籍的id是：%s" % book_id
  return  HttpResponse (text)
...
path("book/<int:book_id>", views.book_detail)
...
urlpatterns = [
  path( 'admin/', admin. site.urls),
  path( 'book/',views.book_list),
  path( 'book/detail', views.book_detail)
]
def book_detail( request):
  book_id  = request.GET.get("id")
  text = "您输入的书籍id是：%s" % book_id
  return  HttpResponse (text)
1. route参数：url的匹配规则。这个参数中可以指定 url中需要 递的参数，比如在访问文 详情
页的时候，可以 递一个 id。 递参数是通过 <>尖括号来进行指定的。并且在 递参数的时候，
可以指定这个参数的数据类型，比如文 的 id都是int类型，那么可以这 写 <int:id> ，以后匹
配的时候，就只会匹配到 id为int类型的url，而不会匹配其他的 url，并且在视图函数中获取
这个参数的时候，就已经被转换成一个 int类型了。其中还有 种常用的类型：
str：非空的字符串类型。默认的转换器。但是不能包含斜 。
int：匹配任意的零或者正数的整形。到视图函数中就是一个int类型。
slug：由英文中的横  -，或者下划线 _连接英文字符或者数字而成的字符串。
uuid：匹配uuid字符串。
path：匹配非空的英文字符串，可以包含斜  /。
2. view参数：可以为一个视图函数或者是 类视图.as_view() 或者是django.urls.include() 函数
的返回值。
3. name参数：这个参数是给这个 url取个名字的，这在项目比较大， url比较多的时候用处很大。

3. URL中包含另外一个urls模块：
在我们的项目中，不可能只有一个 app，如果把所有的 app的views中的视图都放在 urls.py 中进行
射，肯定会让代 显得非常乱。 此 django给我们提供了一个方法，可以在 app内部包含自己的 url匹
配规则，而在项目的 urls.py 中再统一包含这个 app的urls。使用这个技术需要借助 include 函数。
示例代 如下：
在urls.py 文件中把所有的和 book这个app相关的url都移动到 app/urls.py 中了，然后在
startdjango/urls.py 中，通过 include 函数包含 book.urls ，以后在请求 book相关的url的时候都
需要 一个 book的前缀。# startdjango/urls.py文件：
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
  path( 'admin/', admin. site.urls),
  path( 'book/',include("book.urls"))
]
# book/urls.py文件：
from django.urls import path
from . import  views
urlpatterns = [
  path( 'list/',views.book_list),
  path( 'detail/<book_id>/', views.book_detail)
]
以后访问书的列表的 url的时候，就通过 /book/list/ 来访问，访问书籍详情页面的 url的时候就通过
book/detail/<id> 来访问。为了避免多个模块的 urls.py 中包含同名的 url，可以指定一个应用命名
空间：

4. url反转：
之前我们都是通过url来访问视图函数。有时候我们知道这个视图函数，但是想反转回他的url。这时候就
可以通过 reverse 来实现。示例代 如下：
如果有应用命名空间或者有实例命名空间，那么应该在反转的时候 上命名空间。示例代 如下：
如果这个url中需要 递参数，那么可以通过 kwargs来 递参数。示例代 如下：
 为django中的reverse 反转url的时候不区分 GET请求和POST请求， 此不能在反转的时候添 查
询字符串的参数。如果想要添 查询字符串的参数，只能手动的添 。示例代 如下：# book/urls.py文件：
from django.urls import path
from . import  views
# 指定应用命名空间
app_name= 'book'
urlpatterns = [
  path( 'list/',views.book_list),
  path( 'detail/<book_id>/', views.book_detail)
]
reverse("list")
> /book/list/
reverse('book:list')
> /book/list/
reverse("book:detail", kwargs={"book_id": 1})
> /book/detail/1
login_url = reverse('login') + "?next=/"
模板
在之前的 节中，视图函数只是直接返回文本，而在实际生产环境中其实很少这 用， 为实际的
页面大多是带有 式的HTML代 ，这可以让浏览器渲染出非常漂亮的页面。目前市面上有非常多的模板
系统，其中最知名最好用的就是DTL和Jinja2。 DTL是Django Template Language 三个单词的缩写，也
就是Django自带的模板语言。当然也可以配置Django支持Jinja2等其他模板引擎，但是作为Django内置
的模板语言，和Django可以达到 缝衔接而不会产生一些不兼容的情况。 此建议大家学 好DTL。

一、DTL与普通的HTML文件的区别：
DTL模板是一种带有特殊语法的HTML文件，这个HTML文件可以被Django编译，可以 递参数进去，实
现数据动态化。在编译完成后，生成一个普通的HTML文件，然后发送给客户端。

二、渲染模板：
渲染模板有多种方式。这里讲下两种常用的方式。
1. render_to_string ：找到模板，然后将模板编译后渲染成Python的字符串 式。最后再通过
HttpResponse 类包装成一个 HttpResponse 对象返回回去。示例代 如下：
2. 以上方式虽然已经很方便了。但是django 还提供了一个更 简便的方式，直接将模板渲染成字符串
和包装成 HttpResponse 对象一步到位完成。示例代 如下：

三、模板查找路径配置：
在项目的 settings.py 文件中。有一个 TEMPLATES 配置，这个配置包含了模板引擎的配置，模板查找路
径的配置，模板上下文的配置等。模板路径可以在两个地方配置。
1. DIRS：这是一个列表，在这个列表中可以存放所有的模板路径，以后在视图中使用 render或者
render_to_string 渲染模板的时候，会在这个列表的路径中查找模板。
2. APP_DIRS ：默认为 True，这个设置为 True后，会在 INSTALLED_APPS 的安装了的 APP下的
templates 文件夹中查找模板。 from django.template. loader import render_to_string
 from django.http import HttpResponse
 def book_detail( request,book_id):
  html = render_to_string( "detail.html")
  return  HttpResponse (html)
 from django.shortcuts import render
 def book_list( request):
  return  render(request,'list.html')
3. 查找顺序：比如代  render('list.html') 。先会在 DIRS这个列表中依次查找路径下有没有这个
模板，如果有，就返回。如果 DIRS列表中所有的路径都没有找到，那么会先检查当前这个视图所
处的app是否已经安装，如果已经安装了，那么就先在当前这个 app下的templates 文件夹中查找
模板，如果没有找到，那么会在其他已经安装了的 app中查找。如果所有路径下都没有找到，那么
会抛出一个 TemplateDoesNotExist 的异常。
DTL模板语法

变量：
模板中可以包含变量， Django在渲染模板的时候，可以 递变量对应的值过去进行替换。变量的命名规
范和Python非常类似，只能是阿拉伯数字和英文字符以及下划线的组合，不能出现 点符号等特殊字
符。变量需要通过视图函数渲染，视图函数在使用 render或者render_to_string 的时候可以 递一个
context 的参数，这个参数是一个字典类型。以后在模板中的变量就从这个字典中读取值的。示例代
如下：
模板中的变量同 也支持 点(.)的形式。在出现了点的情况，比如 person.username ，模板是按照以下
方式进行解析的：
1. 如果person是一个字典，那么就会查找这个字典的 username 这个key对应的值。
2. 如果person是一个对象，那么就会查找这个对象的 username 属性，或者是 username 这个方法。
3. 如果出现的是 person.1 ，会判断 persons 是否是一个列表或者元组或者任意的可以通过下 访问
的对象，如果是的话就取这个列表的第1个值。如果不是就获取到的是一个空的字符串。

有以下 点需要注意：
不能通过中括号的形式访问字典和列表中的值，比如dict['key']和list[1]是不支持的！
 为使用点（.）语法获取对象值的时候，可以获取这个对象的属性，如果这个对象是一个字典，也
可以获取这个字典的值。所以在给这个字典添 key的时候，千万不能和字典中的一些属性重复。比
如items， 为items是字典的方法，那么如果给这个字典添 一个items作为key，那么以后就不能
再通过item来访问这个字典的键值对了。# profile.html模板代
<p>{{ username }}</p >
# views.py代
def profile (request):
  return  render(request,'profile.html', context={'username': '知了课 '})
常用的模板 签

1. if 签：if 签相当于 Python中的if语句，有 elif和else相对应，但是所有的 签都需要
用 签符号（ {%%}）进行包裹。 if 签中可以使用 ==、!=、<、<=、>、>=、in、not in、is、is
not等判断运算符。示例代 如下：
2. for...in...  签：for...in... 类似于Python中的for...in... 。可以遍历列表、元组、字
符串、字典等一切可以遍历的对象。示例代 如下：
如果想要反向遍历，那么在遍历的时候就 上一个 reversed 。示例代 如下：
遍历字典的时候，需要使用 items、keys和values等方法。在 DTL中，执行一个方法不能使用圆
括号的形式。遍历字典示例代 如下：
在for循环中， DTL提供了一些变量可供使用。这些变量如下：
forloop.counter ：当前循环的下 。以1作为起始值。
forloop.counter0 ：当前循环的下 。以0作为起始值。
forloop.revcounter ：当前循环的反向下 值。比如列表有5个元 ，那么第一次遍历这个
属性是等于5，第二次是4，以此类推。并且是以1作为最后一个元 的下 。
forloop.revcounter0 ：类似于 forloop.revcounter 。不同的是最后一个元 的下 是从
0开始。
forloop.first ：是否是第一次遍历。
forloop.last ：是否是最后一次遍历。
forloop.parentloop ：如果有多个循环嵌套，那么这个属性代表的是上一级的for循环。
3. for...in...empty  签：这个 签使用跟 for...in... 是一 的，只不过是在遍历的对象如果没
有元 的情况下，会执行 empty中的内容。示例代 如下： {% if " 三" in persons %}
  <p> 三</p>
 {% else %}
  <p>李四</p>
 {% endif %}
 {% for person  in persons %}
  <p>{{ person .name }}</p >
 {% endfor %}
 {% for person  in persons reversed %}
  <p>{{ person .name }}</p >
 {% endfor %}
 {% for key,value in person.items %}
  <p>key：{{ key }}</p >
  <p>value：{{ value }}</p >
 {% endfor %}
4. with 签：在模版中定义变量。有时候一个变量访问的时候比较复杂，那么可以先把这个复杂的
变量缓存到一个变量上，以后就可以直接使用这个变量就可以了。示例代 如下：
有 点需要强烈的注意：
在with语句中定义的变量，只能在 {%with%}{%endwith%} 中使用，不能在这个 签外面使
用。
定义变量的时候，不能在等号左右两边留有空 。比如 {% with lisi = persons.1%} 是错
误的。
还有另外一种写法同 也是支持的：
5. url 签：在模版中，我们经常要写一些 url，比如某个 a 签中需要定义 href属性。当然如果
通过硬编 的方式直接将这个 url写死在里面也是可以的。但是这 对于以后项目维护可能不是一
件好事。 此建议使用这种反转的方式来实现，类似于 django中的reverse 一 。示例代 如
下：
如果url反转的时候需要 递参数，那么可以在后面 递。但是参数分位置参数和关键字参数。位
置参数和关键字参数不能同时使用。示例代 如下：
如果想要在使用 url 签反转的时候要 递查询字符串的参数，那么必须要手动在在后面添 。示
例代 如下： {% for person  in persons %}
  <li>{{ person  }}</li>
 {% empty %}
  暂时还没有任何人
 {% endfor %}
 context = {
  "persons": [" 三", "李四"]
 }
 {% with lisi=persons.1 %}
  <p>{{ lisi }}</p >
 {% endwith %}
  {% with persons.1 as lisi %}
  <p>{{ lisi }}</p >
  {% endwith %}
 <a href="{% url 'book:list' %}" >图书列表页面</a >
  # path部分
  path( 'detail/<book_id>/', views.book_detail, name='detail')
  # url反转，使用位置参数
  <a href="{% url 'book:detail' 1 %}"> 图书详情页面</a >
  # url反转，使用关键字参数
  <a href="{% url 'book:detail' book_id=1 %}"> 图书详情页面</a >
如果需要 递多个参数，那么通过空 的方式进行分隔。示例代 如下：
6. spaceless  签：移除html 签中的空白字符。包括空 、tab键、换行等。示例代 如下：
那么在渲染完成后，会变成以下的代 ：
spaceless 只会移除html 签之间的空白字符。而不会移除 签与文本之间的空白字符。看以下代
 ：
这个将不会移除 strong中的空白字符。
7. autoescape  签：开启和关闭这个 签内元 的自动转义功能。自动转义是可以将一些特殊的字
符。比如 <转义成html语法能识别的字符，会被转义成 <，而>会被自动转义成 >。模板中默认
是已经开启了自动转义的。 autoescape 的示例代 如下：
那么就会显示百度的一个超链接。如果把 off改成on，那么就会显示成一个普通的字符串。示例
代 如下：  <a href="{% url 'book:detail' book_id=1 %}?page=1"> 图书详情页面</a >
  <a href="{% url 'book:detail' book_id=1 page=2 %}"> 图书详情页面</a >
 {% spaceless %}
  <p>
  < a href="foo/">Foo</a>
  </p>
 {% endspaceless  %}
 <p><a href="foo/">Foo</a></p>
 {% spaceless %}
  <strong>
  Hello
  </strong>
 {% endspaceless  %}
 #  递的上下文信息
 context = {
  "info" :"<a href='www.baidu.com'>百度</a>"
 }
 # 模板中关闭自动转义
 {% autoescape off %}
  {{ info }}
 {% endautoescape %}
 {% autoescape on %}
  {{ info }}
 {% endautoescape %}
8. verbatim  签：默认在 DTL模板中是会去解析那些特殊字符的。比如 {%和%}以及{{等。如果
在某个代 片段中不想使用 DTL的解析引擎。那么 可以把这个代 片段放在 verbatim  签中。
示例代 下：
9. 更多 签请参考官方文档： https://docs.djangoproject.com/en/5.0/ref/templates/builtins/ {% verbatim %}
  {{if dying}}Still alive.{{/ if}}
 {% endverbatim %}
模版常用过滤器
在模版中，有时候需要对一些数据进行处理以后才能使用。一般在 Python中我们是通过函数的形式来完
成的。而在模版中，则是通过过滤器来实现的。过滤器使用的是 |来使用。比如使用 add过滤器，那么
示例代 如下：
那么以下就讲下在开发中常用的过滤器。
1. add
将 进来的参数添 到原来的值上面。这个过滤器会尝试将 值和参数转换成整形然后进行相 。如果转
换成整形过程中失败了，那么会将 值和参数进行拼接。如果是字符串，那么会拼接成字符串，如果是列
表，那么会拼接成一个列表。示例代 如下：
如果value是等于4，那么结果将是6。如果 value是等于一个普通的字符串，比如 abc，那么结果将是
abc2。add过滤器的源代 如下：
2. cut
移除值中所有指定的字符串。类似于 python中的replace(args,"") 。示例代 如下：
以上示例将会移除 value中所有的空 字符。 cut过滤器的源代 如下：  {{ value|add:"2" }}
{{ value| add:"2" }}
def add(value, arg):
  """Add the arg to the value."""
  try:
  return int(value) +  int(arg)
  except  (ValueError, TypeError):
  try:
  return  value + arg
  except Exception:
  return  ''
{{ value| cut:" " }}
def cut(value, arg):
  """Remove all values of arg from the given string."""
  safe = isinstance( value, SafeData)
  value = value.replace(arg, '')
  if safe and arg != ';':
  return mark_safe( value)
  return  value
 式字符 描述 示例
Y 四位数字的年份 2018
m 两位数字的月份 01-12
n 月份，1-9 前面没有0前缀 1-12
d 两位数字的天 01-31
j 天，但是1-9 前面没有0前缀 1-31
g 小时，12小时 式的，1-9 前面没有0前缀 1-12
h 小时，12小时 式的，1-9 前面有0前缀 01-12
G 小时，24小时 式的，1-9 前面没有0前缀 1-23
H 小时，24小时 式的，1-9 前面有0前缀 01-23
i 分钟，1-9 前面有0前缀 00-59
s 秒，1-9前面有0前缀 00-593. date
将一个日期按照指定的 式， 式化成字符串。示例代 如下：
那么将会输出 2058/02/01 。其中Y代表的是四位数字的年份， m代表的是两位数字的月份， d代表的是
两位数字的日。
还有更多时间 式化的方式。见下表。
4. default
如果值被评估为 False。比如[]，""，None，{}等这些在 if判断中为 False的值，都会使用
default 过滤器提供的默认值。示例代 如下：
如果value是等于一个空的字符串。比如 ""，那么以上代 将会输出 nothing 。# 数据
context = {
  "birthday": datetime. now()
}
# 模版
{{ birthday| date:"Y/m/d" }}
{{ value| default:"nothing" }}
5. default_if_none
如果值是 None，那么将会使用 default_if_none 提供的默认值。这个和 default 有区别， default 是
所有被评估为 False的都会使用默认值。而 default_if_none 则只有这个值是等于 None的时候才会使
用默认值。示例代 如下：
如果value是等于""也即空字符串，那么以上会输出空字符串。如果 value是一个None值，以上代
才会输出 nothing 。
6. first
返回列表/元组/字符串中的第一个元 。示例代 如下：
如果value是等于['a','b','c'] ，那么输出将会是 a。
7. last
返回列表/元组/字符串中的最后一个元 。示例代 如下：
如果value是等于['a','b','c'] ，那么输出将会是 c。
8. floatformat
使用四舍五入的方式 式化一个浮点类型。如果这个过滤器没有 递任何参数。那么只会在小数点后保
留一个小数，如果小数后面全是0，那么只会保留整数。当然也可以 递一个参数， 识具体要保留 个
小数。
1.
value 模版代  输出
34.23234 {{ value|floatformat }} 34.2
34.000 {{ value|floatformat }} 34
34.260 {{ value|floatformat }} 34.3如果没有 递参数：
2.
value 模版代  输出
34.23234 {{value|floatformat:3}} 34.232
34.0000 {{value|floatformat:3}} 34.000
34.26000 {{value\|floatformat:3}} 34.260如果 递参数：{{ value| default_if_none: "nothing" }}
{{ value| first }}
{{ value| last }}

9. join
类似与Python中的join，将列表/元组/字符串用指定的字符进行拼接。示例代 如下：
如果value是等于['a','b','c'] ，那么以上代 将输出 a/b/c。
10. length
获取一个列表/元组/字符串/字典的长度。示例代 如下：
如果value是等于['a','b','c'] ，那么以上代 将输出 3。如果value为None，那么以上将返回
0。
11. lower
将值中所有的字符全部转换成小写。示例代 如下：
如果value是等于Hello World 。那么以上代 将输出 hello world 。
12. upper
类似于lower，只不过是将指定的字符串全部转换成大写。
13. random
在被给的列表/字符串/元组中随机的选择一个值。示例代 如下：
如果value是等于['a','b','c'] ，那么以上代 会在列表中随机选择一个。
14. safe
 记一个字符串是安全的。也即会关掉这个字符串的自动转义。示例代 如下：
如果value是一个不包含任何特殊字符的字符串，比如 <a>这种，那么以上代 就会把字符串正常的输
入。如果 value是一串html代 ，那么以上代 将会把这个 html代 渲染到浏览器中。{{ value| join:"/" }}
{{ value| length }}
{{ value| lower }}
{{ value| random }}
{{value| safe}}
15. slice
类似于Python中的切片操作。示例代 如下：
以上代 将会给 some_list 从2开始做切片操作。
16. stringtags
 除字符串中所有的 html 签。示例代 如下：
如果value是<strong>hello world</strong> ，那么以上代 将会输出 hello world 。
17. truncatechars
如果给定的字符串长度超过了过滤器指定的长度。那么就会进行切割，并且会拼接三个点来作为省略
号。示例代 如下：
如果value是等于北京欢迎您~ ，那么输出的结果是 北京...。可能 会想，为什么不会 北京欢迎您...
呢。 为三个点也 了三个字符，所以 北京 +三个点的字符长度就是5。
18. truncatechars_html
类似于truncatechars ，只不过是不会切割 html 签。示例代 如下：
如果value是等于<p>北京欢迎您~</p> ，那么输出将是 <p>北京...</p> 。{{ some_list| slice:"2:" }}
{{ value| striptags }}
{{ value| truncatechars: 5 }}
{{ value| truncatechars: 5 }}
模版结构

一、include 模版
有时候一些代 是在许多模版中都用到的。如果我们每次都重复的去拷贝代 那肯定不符合项目的规
范。一般我们可以把这些重复性的代 抽取出来，就类似于Python中的函数一 ，以后想要使用这些代
 的时候，就通过 include 包含进来。这个 签就是 include 。示例代 如下：
include  签寻找路径的方式。也是跟 render渲染模板的函数是一 的。
默认include  签包含模版，会自动的使用主模版中的上下文，也即可以自动的使用主模版中的变量。
如果想 入一些其他的参数，那么可以使用 with语句。示例代 如下：

二、模板继承：
在前端页面开发中。有些代 是需要重复使用的。这种情况可以使用 include  签来实现。也可以使用
另外一个比较强大的方式来实现，那就是模版继承。模版继承类似于 Python中的类，在父类中可以先定
义好一些变量和方法，然后在子类中实现。模版继承也可以在父模版中先定义好一些子模版需要用到的
代 ，然后子模版直接继承就可以了。并且 为子模版肯定有自己的不同代 ， 此可以在父模版中定
义一个block接口，然后子模版再去实现。以下是父模版的代 ：# header.html
<p>我是header</p>
# footer.html
<p>我是footer</p>
# main.html
{% include 'header.html' %}
<p>我是main内容</p>
{% include 'footer.html' %}
# header.html
<p>用户名：{{ username }}</p>
# main.html
{% include "header.html" with username='huangyong' %}
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet"  href="{% static 'style.css' %}" />
  <title> {% block title %}我的站点{% endblock %}</title>
</head>
<body>
  <div id="sidebar">
这个模版，我们取名叫做 base.html ，定义好一个简单的 html骨架，然后定义好两个 block接口，让
子模版来 据具体需求来实现。子模板然后通过 extends  签来实现，示例代 如下：
需要注意的是：extends 签必须放在模版的第一行。子模板中的代 必须放在block中，否则将不会被
渲染。
如果在某个block中需要使用父模版的内容，那么可以使用 {{block.super}} 来继承。比如上例，
{%block title%} ，如果想要使用父模版的 title，那么可以在子模版的 title block 中使用{{
block.super }} 来实现。
在定义block的时候，除了在 block开始的地方定义这个 block的名字，还可以在 block结束的时候定
义名字。比如 {% block title %}{% endblock title %} 。这在大型模版中显得尤其有用，能让 快
速的看到 block包含在哪里。  {% block sidebar %}
  <ul>
  <li><a  href="/">首页</a></li>
  <li><a  href="/blog/"> 博客</a></li>
  </ul>
  {% endblock %}
  </div>
  <div id="content">
  {% block content %}{% endblock %}
  </div>
</body>
</html>
{% extends "base.html" %}
{% block title %}博客列表{% endblock %}
{% block content %}
  {% for entry in blog_entries %}
  <h2>{{ entry.title }} </h2>
  <p>{{ entry.body }}</p>
  {% endfor %}
{% endblock %}
 载静态文件

在一个网页中，不仅仅只有一个 html骨架，还需要 css 式文件， js执行文件以及一些图片等。
 此在DTL中 载静态文件是一个必须要解决的问题。在 DTL中，使用 static 签来 载静态文件。要
使用static 签，首先需要 {% load static %} 。 载静态文件的步骤如下：
1. 首先确保 django.contrib.staticfiles 已经添 到 settings.INSTALLED_APPS 中。
2. 确保在settings.py 中设置了 STATIC_URL 。比如：
3. 在已经安装了的 app下创建一个文件夹叫做 static，然后再在这个 static文件夹下创建一个当前
app的名字的文件夹，再把静态文件放到这个文件夹下。例如 的 app叫做book，有一个静态文
件叫做zhiliao.jpg ，那么路径为 book/static/book/zhiliao.jpg 。（为什么在 app下创建一
个static文件夹，还需要在这个 static下创建一个同 app名字的文件夹呢？原 是如果直接把静
态文件放在 static文件夹下，那么在模版 载静态文件的时候就是使用 zhiliao.jpg ，如果在多
个app之间有同名的静态文件，这时候可能就会产生混淆。而在 static文件夹下 了一个同名
app文件夹，在模版中 载的时候就是使用 app/zhiliao.jpg ，这 就可以避免产生混淆。）
4. 如果有一些静态文件是不和任何 app挂钩的。那么可以在 settings.py 中添
STATICFILES_DIRS ，以后DTL就会在这个列表的路径中查找静态文件。比如可以设置为:
5. 在模版中使用 load 签 载 static 签。比如要 载在项目的 static文件夹下的 style.css 的
文件。那么示例代 如下：
6. 如果不想每次在模版中 载静态文件都使用 load 载static 签，那么可以在 settings.py 中
的TEMPLATES/OPTIONS 添 'builtins':['django.templatetags.static'] ，这 以后在模版
中就可以直接使用 static 签，而不用手动的 load了。STATIC_URL = 'static/'
 STATICFILES_DIRS = [
  os. path.join(BASE_DIR, "static")
 ]
 {% load static %}
 <link rel="stylesheet"  href="{% static 'style.css' %}">
TEMPLATES = [
  {
  'BACKEND': 'django.template.backends.django.DjangoTemplates',
  'DIRS': [BASE_DIR / 'templates']
  ,
  'APP_DIRS': True,
  'OPTIONS': {
  'context_processors': [
  'django.template.context_processors.debug',
  'django.template.context_processors.request',
  'django.contrib.auth.context_processors.auth' ,
  'django.contrib.messages.context_processors.messages',
  ],
7. 如果没有在 settings.INSTALLED_APPS 中添 django.contrib.staticfiles 。那么我们就需要
手动的将请求静态文件的 url与静态文件的路径进行 射了，这个操作通常用来 载媒体文件（上
 的文件）。示例代 如下：
在settings.py 中的对MEDIA_URL 和MEDIA_ROOT 的配置如下：

注意：静态文件和媒体文件，最好都是通过Nginx等专业的web服务器来部署，以上方式仅在开发阶段
使用。
  # 这里 载
  'builtins':['django.templatetags.static' ]
  },
  },
]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  path( 'admin/', admin. site.urls),
  ...
] + static(settings. MEDIA_URL, document_root= settings. MEDIA_ROOT)
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL=  '/media/'
MySQL数据库
在网站开发中，数据库是网站的重要组成部分。只有提供数据库，数据才能够动态的展示，而不是在网
页中显示一个静态的页面。数据库有很多，比如有关系型数据库 SQL Server 、Oracle、PostgreSQL
以及MySQL等等，还有非关系型数据库： MongoDB 、Redis等。二MySQL由于价 实 、简单易用、不
受平台限制、灵活度高等特性，目前已经取得了绝大多数的市场份额。 此我们在 Django中，也是使用
MySQL来作为数据存储。
一、MySQL 数据库安装：
1. 在MySQL的官网下载 MySQL数据库安装文件： https://dev.mysql.com/downloads/mysql/ 。
2. 如果提示没有 .NET Framework 框架。那么就在提示框中找到下载链接，下载一个就可以了。
3. 如果提示没有 Microsoft Virtual C++ x64(x86) ，那么百度或者谷歌这个软件安装即可。
4. 接下来就是做好用户名和密 的配置即可。
二、navicat 数据库操作软件：
安装完MySQL数据库以后，就可以使用 MySQL提供的终端客户端软件来操作数据库。如下：
这个软件所有的操作都是基于 sql语言，对于想要熟练 sql语言的同学来讲是非常合适的。但是对于在
企业中可能不是一款好用的工具。在企业中我们推荐使用 mysql workbench 以及navicat 这种图形化操
作的软件。而 mysql workbench 是mysql官方提供的一个免费的软件，正 为是免费，所以在一些功能
上不及navicat 。navicat 是一款收费的软件。官网地址如下：
https://www.navicat.com.cn/products 。使用的截图如下：

三、MySQL 驱动程序安装：
我们使用 Django来操作MySQL，实际上底层还是通过 Python来操作的。 此我们想要用 Django来操
作MySQL，首先还是需要安装一个驱动程序。在 Python3 中，驱动程序有多种选择。比如有 pymysql 以
及mysqlclient 等。这里我们就使用 mysqlclient 来操作。 mysqlclient 安装非常简单。只需要通过
pip install mysqlclient 即可安装。
常见MySQL驱动介绍：
1. MySQL-python ：也就是 MySQLdb 。是对C语言操作 MySQL数据库的一个简单封装。遵循了
Python DB API v2 。但是只支持 Python2 ，目前还不支持 Python3 。
2. mysqlclient ：是MySQL-python 的另外一个分支。支持 Python3 并且修复了一些 bug。
3. pymysql ：纯Python实现的一个驱动。 为是纯 Python编写的， 此执行效率不如 MySQL-
python。并且也 为是纯 Python编写的， 此可以和 Python代  缝衔接。
4. MySQL Connector/Python ：MySQL官方推出的使用纯 Python连接MySQL的驱动。 为是纯
Python开发的。效率不高。
操作数据库

一、Django 配置连接数据库：
在操作数据库之前，首先先要连接数据库。这里我们以配置 MySQL为例来讲解。 Django连接数据库，不
需要单独的创建一个连接对象。只需要在 settings.py 文件中做好数据库相关的配置就可以了。示例代
 如下：
其中engine的选择还有以下：
'django.db.backends.postgresql'
'django.db.backends.mysql'
'django.db.backends.sqlite3'
'django.db.backends.oracle'

二、在Django 中操作数据库：
在Django中操作数据库有两种方式。第一种方式就是使用原生 sql语句操作，第二种就是使用 ORM模型
来操作。这节课首先来讲下第一种。
在Django中使用原生 sql语句操作其实就是使用 python db api 的接口来操作。如果 的 mysql驱动
使用的是 pymysql ，那么 就是使用 pymysql 来操作的，只不过 Django将数据库连接的这一部分封装
好了，我们只要在 settings.py 中配置好了数据库连接信息后直接使用 Django封装好的接口就可以操
作了。示例代 如下：DATABASES = {
  'default': {
  # 数据库引擎（是mysql还是oracle等）
  'ENGINE': 'django.db.backends.mysql',
  # 数据库的名字
  'NAME': 'dfz',
  # 连接mysql数据库的用户名
  'USER': 'root' ,
  # 连接mysql数据库的密
  'PASSWORD': 'root' ,
  # mysql数据库的主机地址
  'HOST': '127.0.0.1',
  # mysql数据库的端口号
  'PORT': '3306' ,
  }
}
以上的execute 以及fetchall 方法都是 Python DB API 规范中定义好的。任何使用 Python来操作
MySQL的驱动程序都应该遵循这个规范。所以不管是使用 pymysql 或者是mysqlclient 或者是
mysqldb ，他们的接口都是一 的。更多规范请参考： https://www.python.org/dev/peps/pep-024
9/。

三、Python DB API下规范下cursor 对象常用接口：
1. description ：如果cursor执行了查询的 sql代 。那么读取 cursor.description 属性的时
候，将返回一个列表，这个列表中装的是元组，元组中装的分别是
(name,type_code,display_size,internal_size,precision,scale,null_ok) ，其中name代
表的是查找出来的数据的字段名称，其他参数暂时用处不大。
2. rowcount ：代表的是在执行了 sql语句后受影响的行数。
3. close：关闭游 。关闭游 以后就再也不能使用了，否则会抛出异常。
4. execute(sql[,parameters]) ：执行某个 sql语句。如果在执行 sql语句的时候还需要 递参
数，那么可以 给 parameters 参数。示例代 如下：
5. fetchone ：在执行了查询操作以后，获取第一条数据。
6. fetchmany(size) ：在执行查询操作以后，获取多条数据。具体是多少条要看 的 size参数。如
果不 size参数，那么默认是获取第一条数据。
7. fetchall ：获取所有满足 sql语句的数据。# 使用django封装好的connection对象，会自动读取settings.py中数据库的配置信息
from django.db import connection
# 获取游 对象
cursor = connection. cursor()
# 拿到游 对象后执行sql语句
cursor.execute("select * from book")
# 获取所有的数据
rows = cursor.fetchall()
# 遍历查询到的数据
for row in rows:
  print( row)
 cursor.execute("select * from article where id=%s",(1 ,))
ORM模型介绍

一、ORM模型介绍
随着项目越来越大，采用写原生SQL的方式在代 中会出现大量的SQL语句，那么问题就出现了：
1. SQL语句重复利用率不高，越复杂的SQL语句条件越多，代 越长。会出现很多相近的SQL语句。
2. 很多SQL语句是在业务逻辑中拼出来的，如果有数据库需要更改，就要去修改这些逻辑，这会很容
易漏掉对某些SQL语句的修改。
3. 写SQL时容易忽略web安全问题，给未来 成隐患。SQL注入。
ORM，全称Object Relational Mapping ，中文叫做对象关系 射，通过 ORM我们可以通过类的方式
去操作数据库，而不用再写原生的SQL语句。通过把表 射成类，把行作实例，把字段作为属性， ORM
在执行对象操作的时候最终还是会把对应的操作转换为数据库原生语句。使用 ORM有许多优点：
1. 易用性：使用 ORM做数据库的开发可以有效的减少重复SQL语句的概率，写出来的模型也更 直
观、清晰。
2. 性能损耗小： ORM转换成底层数据库操作指令确实会有一些开销。但从实际的情况来看，这种性能
损耗很少（不足5%），只要不是对性能有严苛的要求，综合考虑开发效率、代 的阅读性，带来的
好处要远远大于性能损耗，而且项目越大作用越明显。
3. 设计灵活：可以轻松的写出复杂的查询。
4. 可移植性：Django封装了底层的数据库实现，支持多个关系数据库引擎，包括流行的 MySQL、
PostgreSQL 和SQLite。可以非常轻松的切换数据库。

二、创建ORM模型：
ORM模型一般都是放在 app的models.py 文件中。每个 app都可以拥有自己的模型。并且如果这个模型
想要 射到数据库中，那么这个 app必须要放在 settings.py 的INSTALLED_APP 中进行安装。以下是
写一个简单的书籍 ORM模型。示例代 如下：
以上便定义了一个模型。这个模型继承自 django.db.models.Model ，如果这个模型想要 射到数据库
中，就必须继承自这个类。这个模型以后 射到数据库中，表名是模型名称的小写形式，为 book。在这
个表中，有四个字段，一个为 name，这个字段是保存的是书的名称，是 varchar 类型，最长不能超过
20个字符，并且不能为空。第二个字段是作者名字类型，同 也是 varchar 类型，长度不能超过20个。
第三个是出版时间，数据类型是 datetime 类型，默认是保存这本书籍的时间。第五个是这本书的价 ，
是浮点类型。
还有一个字段我们没有写，就是主键 id，在django中，如果一个模型没有定义主键，那么将会自动生
成一个自动增长的 int类型的主键，并且这个主键的名字就叫做 id。

三、 射模型到数据库中：
将ORM模型 射到数据库中，总结起来就是以下 步：
1. 在settings.py 中，配置好 DATABASES ，做好数据库相关的配置。
2. 在app中的models.py 中定义好模型，这个模型必须继承自 django.db.models 。
3. 将这个app添 到settings.py 的INSTALLED_APP 中。
4. 在命令行终端，进入到项目所在的路径，然后执行命令 python manage.py makemigrations 来生
成迁移脚本文件。
5. 同 在命令行中，执行命令 python manage.py migrate 来将迁移脚本文件 射到数据库中。from django.db import models
class Book(models.Model):
  name = models.CharField( max_length= 20,null=False)
  author  = models.CharField( max_length= 20,null=False)
  pub_time = models.DateTimeField( auto_add_now =True)
  price = models.FloatField( default=0)
模型常用Field和参数

一、常用字段：
在Django中，定义了一些 Field来与数据库表中的字段类型来进行 射。以下将介绍那些常用的字段类
型。
1. AutoField：
 射到数据库中是 int类型，可以有自动增长的特性。一般不需要使用这个类型，如果不指定主键，那
么模型会自动的生成一个叫做 id的自动增长的主键。如果 想指定一个其他名字的并且具有自动增长的
主键，使用 AutoField 也是可以的。
2. BigAutoField：
64位的整形，类似于 AutoField ，只不过是产生的数据的范围是从 1-9223372036854775807 。
3. BooleanField：
在模型层面接收的是 True/False 。在数据库层面是 tinyint 类型。如果没有指定默认值，默认值是
None。
4. CharField：
在数据库层面是 varchar 类型。在 Python层面就是普通的字符串。这个类型在使用的时候必须要指定
最大的长度，也即必须要 递 max_length 这个关键字参数进去。
5. DateField：
日期类型。在 Python中是datetime.date 类型，可以记录年月日。在 射到数据库中也是 date类型。
使用这个 Field可以 递以下 个参数：
1. auto_now ：在每次这个数据保存的时候，都使用当前的时间。比如作为一个记录修改日期的字
段，可以将这个属性设置为 True。
2. auto_now_add ：在每次数据第一次被添 进去的时候，都使用当前的时间。比如作为一个记录第
一次入库的字段，可以将这个属性设置为 True。
6. DateTimeField：
日期时间类型，类似于 DateField 。不仅仅可以存储日期，还可以存储时间。 射到数据库中是
datetime 类型。这个 Field也可以使用 auto_now 和auto_now_add 两个属性。
7. TimeField：
时间类型。在数据库中是 time类型。在 Python中是datetime.time 类型。
8. EmailField：
类似于CharField 。在数据库底层也是一个 varchar 类型。最大长度是254 个字符。
9. FileField：
用来存储文件的。这个请参考后面的文件上  节部分。
10. ImageField ：
用来存储图片文件的。这个请参考后面的图片上  节部分。
11. FloatField：
浮点类型。 射到数据库中是float类型。
12. IntegerField ：
整形。值的区间是 -2147483648——2147483647 。
13. BigIntegerField ：
大整形。值的区间是 -9223372036854775808——9223372036854775807 。
14. PositiveIntegerField：
正整形。值的区间是 0——2147483647 。
15. SmallIntegerField ：
小整形。值的区间是 -32768——32767 。
16. PositiveSmallIntegerField：
正小整形。值的区间是 0——32767 。
17. TextField ：
大量的文本类型。 射到数据库中是longtext类型。
18. UUIDField ：
只能存储uuid 式的字符串。 uuid是一个32位的全球唯一的字符串，一般用来作为主键。
19. URLField ：
类似于CharField ，只不过只能用来存储 url 式的字符串。并且默认的 max_length 是200。


二、Field的常用参数：
null：
如果设置为 True，Django将会在 射表的时候指定是否为空。默认是为 False。在使用字符串相关的
Field（CharField/TextField）的时候，官方推荐尽量不要使用这个参数，也就是保持默认值 False。
 为Django在处理字符串相关的 Field的时候，即使这个 Field的null=False ，如果 没有给这个
Field 递任何值，那么 Django也会使用一个空的字符串 ""来作为默认值存储进去。 此如果再使用
null=True ，Django会产生两种空值的情形（NULL或者空字符串）。如果想要在表单验证的时候允许
这个字符串为空，那么建议使用 blank=True 。如果 的 Field是BooleanField ，那么对应的可空的
字段则为 NullBooleanField 。
blank：
 识这个字段在表单验证的时候是否可以为空。默认是 False。
这个和null是有区别的， null是一个纯数据库级别的。而 blank是表单验证级别的。
db_column ：
这个字段在数据库中的名字。如果没有设置这个参数，那么将会使用模型中属性的名字。
default：
默认值。可以为一个值，或者是一个函数，但是不支持 lambda表达式。并且不支持列表/字典/集合等可
变的数据结构。
primary_key：
是否为主键。默认是False。
unique：
在表中这个字段的值是否唯一。一般是设置手机号 /邮箱等。
更多Field参数请参考官方文档： https://docs.djangoproject.com/zh-hans/5.0/ref/models/fields/

三、模型中 Meta配置：
对于一些模型级别的配置。我们可以在模型中定义一个类，叫做 Meta。然后在这个类中添 一些类属性
来控制模型的作用。比如我们想要在数据库 射的时候使用自己指定的表名，而不是使用模型的名称。
那么我们可以在 Meta类中添 一个 db_table 的属性。示例代 如下：
以下将对 Meta类中的一些常用配置进行解释。class Book(models.Model):
  name = models.CharField( max_length= 20,null=False)
  desc =
models.CharField( max_length= 100,name= 'description', db_column= "description1")
  class Meta:
  db_table = 'book_model'
db_table：
这个模型 射到数据库中的表名。如果没有指定这个参数，那么在 射的时候将会使用模型名来作为默
认的表名。
ordering：
设置在提取数据的排序方式。后面 节会讲到如何查找数据。比如我想在查找数据的时候 据添 的时
间排序，那么示例代 如下：
更多的配置后面会慢慢介绍到。 官方文档： https://docs.djangoproject.com/zh-hans/5.0/ref/models/
options/class Book(models.Model):
  name = models.CharField( max_length= 20,null=False)
  desc =
models.CharField( max_length= 100,name= 'description', db_column= "description1")
  pub_date = models.DateTimeField( auto_now_add =True)
  class Meta:
  db_table = 'book_model'
  ordering = ['pub_date']
外键和表关系

一、外键：
在MySQL中，表有两种引擎，一种是 InnoDB，另外一种是 myisam。如果使用的是 InnoDB引擎，是支
持外键约束的。外键的存在使得 ORM框架在处理表关系的时候异常的强大。 此这里我们首先来介绍下
外键在Django中的使用。
类定义为 class ForeignKey(to,on_delete,**options) 。第一个参数是引用的是哪个模型，第二个
参数是在使用外键引用的模型数据被 除了，这个字段该如何处理，比如有 CASCADE 、SET_NULL 等。
这里以一个实际案例来说明。比如有一个 User和一个Article 两个模型。一个 User可以发表多篇文
 ，一个 Article 只能有一个 Author，并且通过外键进行引用。那么相关的示例代 如下：
以上使用 ForeignKey 来定义模型之间的关系。即在 article 的实例中可以通过 author属性来操作对应
的User模型。这 使用起来非常的方便。示例代 如下：
为什么使用了 ForeignKey 后，就能通过 author访问到对应的 user对象呢。 此在底层， Django为
Article 表添 了一个 属性名_id 的字段（比如author的字段名称是author_id），这个字段是一个外
键，记录着对应的作者的主键。以后通过 article.author 访问的时候，实际上是先通过 author_id 找
到对应的数据，然后再提取 User表中的这条数据，形成一个模型。
如果想要引用另外一个 app的模型，那么应该在 递 to参数的时候，使用 app.model_name 进行指定。
以上例为例，如果 User和Article 不是在同一个 app中，那么在引用的时候的示例代 如下：class User(models.Model):
  username = models.CharField( max_length= 20)
  password = models.CharField( max_length= 100)
class Article(models.Model):
  title = models.CharField( max_length= 100)
  content  = models.TextField()
  author  = models.ForeignKey( "User",on_delete= models.CASCADE)
article = Article(title='abc',content='123')
author = User(username= ' 三',password= '111111')
article.author = author
article.save()
# 修改article.author上的值
article.author.username = '李四'
article.save()
如果模型的外键引用的是本身自己这个模型，那么 to参数可以为 'self'，或者是这个模型的名字。在
论坛开发中，一般评论都可以进行二级评论，即可以针对另外一个评论进行评论，那么在定义模型的时
候就需要使用外键来引用自身。示例代 如下：

二、外键 除操作：
如果一个模型使用了外键。那么在对方那个模型被 掉后，该进行什么 的操作。可以通过 on_delete
来指定。可以指定的类型如下：
1. CASCADE ：级联操作。如果外键对应的那条数据被 除了，那么这条数据也会被 除。
2. PROTECT ：受保护。即只要这条数据引用了外键的那条数据，那么就不能 除外键的那条数据。
3. SET_NULL ：设置为空。如果外键的那条数据被 除了，那么在本条数据上就将这个字段设置为
空。如果设置这个选项，前提是要指定这个字段可以为空。
4. SET_DEFAULT ：设置默认值。如果外键的那条数据被 除了，那么本条数据上就将这个字段设置为
默认值。如果设置这个选项，前提是要指定这个字段一个默认值。
5. SET()：如果外键的那条数据被 除了。那么将会获取 SET函数中的值来作为这个外键的值。 SET
函数可以接收一个可以调用的对象（比如函数或者方法），如果是可以调用的对象，那么会将这个
对象调用后的结果作为值返回回去。
6. DO_NOTHING ：不采取任何行为。一切全看数据库级别的约束。
以上这些选项只是Django 级别的，数据级别依旧是RESTRICT ！

三、表关系：
表之间的关系都是通过外键来进行关联的。而表之间的关系， 非就是三种关系：一对一、一对多（多
对一）、多对多等。以下将讨论一下三种关系的应用场景及其实现方式。# User模型在user这个app中
class User(models.Model):
  username = models.CharField( max_length= 20)
  password = models.CharField( max_length= 100)
# Article模型在article这个app中
class Article(models.Model):
  title = models.CharField( max_length= 100)
  content  = models.TextField()
  author  = models.ForeignKey( "user.User", on_delete= models.CASCADE)
class Comment(models.Model):
  content  = models.TextField()
  origin_comment = models.ForeignKey( 'self',on_delete= models.CASCADE,null=True)
  # 或者
  # origin_comment =
models.ForeignKey('Comment',on_delete=models.CASCADE,null=True)
1. 一对多：
1. 应用场景：比如文 和作者之间的关系。一个文 只能由一个作者编写，但是一个作者可以写多篇
文 。文 和作者之间的关系就是典型的多对一的关系。
2. 实现方式：一对多或者多对一，都是通过 ForeignKey 来实现的。还是以文 和作者的案例进行讲
解。
那么以后在给 Article 对象指定 author，就可以使用以下代 来完成：
并且以后如果想要获取某个用户下所有的文 ，可以通过 article_set 来实现。示例代 如下：
2. 一对一：
1. 应用场景：比如一个用户表和一个用户信息表。在实际网站中，可能需要保存用户的许多信息，但
是有些信息是不经常用的。如果把所有信息都存放到一 表中可能会影响查询效率， 此可以把用
户的一些不常用的信息存放到另外一 表中我们叫做UserExtension 。但是用户表 User和用户信
息表UserExtension 就是典型的一对一了。
2. 实现方式： Django为一对一提供了一个专门的 Field叫做OneToOneField 来实现一对一操作。示
例代 如下： class User(models.Model):
  username = models.CharField( max_length= 20)
  password = models.CharField( max_length= 100)
 class Article(models.Model):
  title = models.CharField( max_length= 100)
  content  = models.TextField()
  author  = models.ForeignKey( "User",on_delete= models.CASCADE)
article = Article(title='abc',content='123')
author = User(username= 'zhiliao', password= '111111')
# 要先保存到数据库中
author.save()
article.author = author
article.save()
user = User.objects.first()
# 获取第一个用户写的所有文
articles = user.article_set. all()
for article  in articles:
  print( article)
 class User(models.Model):
  username = models.CharField( max_length= 20)
  password = models.CharField( max_length= 100)
 class UserExtension( models.Model):
  birthday = models.DateTimeField( null=True)
  school  = models.CharField( blank=True,max_length= 50)
  user = models.OneToOneField( "User", on_delete= models.CASCADE)
在UserExtension 模型上增 了一个一对一的关系 射。其实底层是在 UserExtension 这个表上
增 了一个 user_id ，来和user表进行关联，并且这个外键数据在表中必须是唯一的，来保证一
对一。
3. 多对多：
1. 应用场景：比如文 和 签的关系。一篇文 可以有多个 签，一个 签可以被多个文 所引用。
 此 签和文 的关系是典型的多对多的关系。
2. 实现方式： Django为这种多对多的实现提供了专门的 Field。叫做ManyToManyField 。还是拿文
 和 签为例进行讲解。示例代 如下：
在数据库层面，实际上 Django是为这种多对多的关系建立了一个中间表。这个中间表分别定义了
两个外键，引用到 article 和tag两 表的主键。


四、related_name和related_query_name：

1. related_name：
还是以User和Article 为例来进行说明。如果一个 article 想要访问对应的作者，那么可以通过
author来进行访问。但是如果有一个 user对象，想要通过这个 user对象获取所有的文 ，该如何做
呢？这时候可以通过 user.article_set 来访问，这个名字的规律是 模型名字小写_set 。示例代 如
下：
如果不想使用 模型名字小写_set 的方式，想要使用其他的名字，那么可以在定义模型的时候指定
related_name 。示例代 如下：
以后在反向引用的时候。使用 articles 可以访问到这个作者的文 模型。示例代 如下： class Article(models.Model):
  title = models.CharField( max_length= 100)
  content  = models.TextField()
  tags = models.ManyToManyField( "Tag",related_name ="articles")
 class Tag(models .Model):
  name = models.CharField( max_length= 50)
user = User.objects.get(name= ' 三')
user.article_set. all()
class Article(models.Model):
  title = models.CharField( max_length= 100)
  content  = models.TextField()
  #  递related_name参数，以后在方向引用的时候使用articles进行访问
  author  =
models.ForeignKey( "User",on_delete= models.SET_NULL, null=True,related_name ='articl
es')
如果不想使用反向引用，那么可以指定 related_name='+' 。示例代 如下：
以后将不能通过 user.article_set 来访问文 模型了。

2. related_query_name：
在查找数据的时候，可以使用 filter进行过滤。使用 filter过滤的时候，不仅仅可以指定本模型上的
某个属性要满足什么条件，还可以指定相关联的模型满足什么属性。比如现在想要获取写过 题为 abc
的所有用户，那么可以这 写：
如果 设置了 related_name 为articles ， 为反转的过滤器的名字将使用 related_name 的名字，那
么上例代 将改成如下：
可以通过 related_query_name 将查询的反转名字修改成其他的名字。比如 article 。示例代 如下：
那么在做反向过滤查找的时候就可以使用以下代 ：user = User.objects.get(name= ' 三')
user.articles. all()
class Article(models.Model):
  title = models.CharField( max_length= 100)
  content  = models.TextField()
  #  递related_name参数，以后在方向引用的时候使用articles进行访问
  author  =
models.ForeignKey( "User",on_delete= models.SET_NULL, null=True,related_name ='+')
users = User.objects.filter(article__title= 'abc')
users = User.objects.filter(articles__title= 'abc')
class Article(models.Model):
  title = models.CharField( max_length= 100)
  content  = models.TextField()
  #  递related_name参数，以后在方向引用的时候使用articles进行访问
  author  =
models.ForeignKey( "User",on_delete= models.SET_NULL, null=True,related_name ='articl
es',related_query_name ='article')
users = User.objects.filter(article__title= 'abc')
CRUD操作

在ORM框架中，所有模型相关的操作，比如添 / 除等。其实都是 射到数据库中一条数据的操作。
此模型操作也就是数据库表中数据的操作。
一、添 一个模型到数据库中：
添 模型到数据库中。首先需要创建一个模型。创建模型的方式很简单，就跟创建普通的 Python对象是
一摸一 的。在创建完模型之后，需要调用模型的 save方法，这  Django会自动的将这个模型转换成
sql语句，然后存储到数据库中。示例代 如下：

二、查找数据：
查找数据都是通过模型下的 objects 对象来实现的。
1. 查找所有数据：
要查找Book这个模型对应的表下的所有数据。那么示例代 如下：
以上将返回 Book模型下的所有数据。
2. 数据过滤：
在查找数据的时候，有时候需要对一些数据进行过滤。那么这时候需要调用 objects 的filter方法。
实例代 如下：
调用filter，会将所有满足条件的模型对象都返回。class Book(models.Model):
  name = models.CharField( max_length= 20,null=False)
  desc =
models.CharField( max_length= 100,name= 'description', db_column= "description1")
  pub_date = models.DateTimeField( auto_now_add =True)
book = Book(name='三国演义',desc= '三国英雄！')
book.save()
books = Book.objects.all()
books = Book.objects.filter(name='三国演义')
> [<Book:三国演义>]
# 多个条件
books = Book.objects.filter(name='三国演义',desc= 'test')
3. 获取单个对象：
使用filter返回的是所有满足条件的结果集。有时候如果只需要返回第一个满足条件的对象。那么可以
使用get方法。示例代 如下：
当然，如果没有找到满足条件的对象，那么就会抛出一个异常。而 filter在没有找到满足条件的数据的
时候，是返回一个空的列表。
4. 数据排序：
在之前的例子中，数据都是 序的。如果 想在查找数据的时候使用某个字段来进行排序，那么可以使
用order_by 方法来实现。示例代 如下：
以上代 在提取所有书籍的数据的时候，将会使用 pub_date 从小到大进行排序。如果想要进行倒序排
序，那么可以在 pub_date 前面 一个负号。实例代 如下：

二、修改数据：
在查找到数据后，便可以进行修改了。修改的方式非常简单，只需要将查找出来的对象的某个属性进行
修改，然后再调用这个对象的save方法便可以进行修改。示例代 如下：

三、 除数据：
在查找到数据后，便可以进行 除了。 除数据非常简单，只需要调用这个对象的 delete方法即可。实
例代 如下：book = Book.objects.get(name= '三国演义')
> <Book:三国演义>
books = Book.objects.order_by( "pub_date")
books = Book.objects.order_by( "-pub_date")
from datetime import datetime
book = Book.objects.get(name= '三国演义')
book.pub_date = datetime. now()
book.save()
book = Book.objects.get(name= '三国演义')
book.delete()
查询操作
查找是数据库操作中一个非常重要的技术。查询一般就是使用 filter、exclude 以及get三个方法来
实现。我们可以在调用这些方法的时候 递不同的参数来实现查询需求。在 ORM层面，这些查询条件都
是使用field +__+condition 的方式来使用的。以下将那些常用的查询条件来一一解释。

一、查询条件
1. exact：
使用精确的 =进行查找。如果提供的是一个 None，那么在 SQL层面就是被解释为 NULL。示例代 如
下：
以上的两个查找在翻译为 SQL语句为如下：
2. iexact：
使用like进行查找。示例代 如下：
那么以上的查询就等价于以下的 SQL语句：
注意上面这个 sql语句， 为在 MySQL中，没有一个叫做 ilike的。所以 exact和iexact的区别实际
上就是LIKE和=的区别，在大部分 collation=utf8_general_ci 情况下都是一 的（ collation 是
用来对字符串比较的）。
3. contains ：
大小写敏感，判断某个字段是否包含了某个数据。示例代 如下：
在翻译成 SQL语句为如下：
要注意的是，在使用 contains 的时候，翻译成的 sql语句左右两边是有百分号的，意味着使用的是模糊
查询。而 exact翻译成sql语句左右两边是没有百分号的，意味着使用的是精确的查询。article = Article.objects.get(id__exact= 14)
article = Article.objects.get(id__exact= None)
select ... from article where id= 14;
select ... from article where id IS NULL;
article = Article.objects.filter(title__iexact='hello world')
select ... from article where title like 'hello world';
articles = Article.objects.filter(title__contains= 'hello')
select ... where title like binary '%hello%';
4. icontains ：
大小写不敏感的匹配查询。示例代 如下：
在翻译成 SQL语句为如下：
5. in：
提取那些给定的 field的值是否在给定的容器中。容器可以为 list、tuple或者任何一个可以迭代的
对象，包括 QuerySet 对象。示例代 如下：
以上代 在翻译成 SQL语句为如下：
当然也可以 递一个 QuerySet 对象进去。示例代 如下：
以上代 的意思是获取那些文  题包含 hello的所有分类。
将翻译成以下 SQL语句，示例代 如下：
6. gt：
某个field的值要大于给定的值。示例代 如下：
以上代 的意思是将所有 id大于4的文 全部都找出来。
将翻译成以下 SQL语句：
7. gte：
类似于gt，是大于等于。articles = Article.objects.filter(title__icontains= 'hello')
select ... where title like '%hello%';
articles = Article.objects.filter(id__in=[1,2,3])
select ... where id in (1,3,4)
inner_qs = Article.objects.filter(title__contains= 'hello')
categories = Category. objects.filter(article__in= inner_qs)
select ...from category where article.id in (select id from article where title
like '%hello%') ;
articles = Article.objects.filter(id__gt=4)
select ... where id >  4;
8. lt：
类似于gt是小于。
9. lte：
类似于lt，是小于等于。
10. startswith：
判断某个字段的值是否是以某个值开始的。大小写敏感。示例代 如下：
以上代 的意思是提取所有 题以 hello字符串开头的文 。
将翻译成以下 SQL语句：
11. istartswith ：
类似于startswith ，但是大小写是不敏感的。
12. endswith：
判断某个字段的值是否以某个值结束。大小写敏感。示例代 如下：
以上代 的意思是提取所有 题以 world结尾的文 。
将翻译成以下 SQL语句：
13. iendswith：
类似于endswith ，只不过大小写不敏感。
14. range：
判断某个 field的值是否在给定的区间中。示例代 如下：
以上代 的意思是提取所有发布时间在 2018/1/1 到2018/12/12 之间的文 。
将翻译成以下的 SQL语句：articles = Article.objects.filter(title__startswith ='hello')
select ... where title like 'hello%'
articles = Article.objects.filter(title__endswith= 'world')
select ... where title like '%world';
from django.utils.timezone import make_aware
from datetime import datetime
start_date = make_aware( datetime( year=2018,month=1,day=1))
end_date = make_aware( datetime( year=2018,month=3,day=29,hour=16))
articles = Article.objects.filter(pub_date__range= (start_date, end_date))
需要注意的是，以上提取数据，不会包含最后一个值。也就是不会包含 2018/12/12 的文 。
15. date ：
针对某些 date或者datetime 类型的字段。可以指定 date的范围。并且这个时间过滤，还可以使用链
式调用。示例代 如下：
以上代 的意思是查找时间为 2018/3/29 这一天发表的所有文 。
将翻译成以下的 sql语句：

16. year ：
 据年份进行查找。示例代 如下：
以上的代 在翻译成 SQL语句为如下：
17. month：
同year， 据月份进行查找。
18. day：
同year， 据日期进行查找。
19. week_day ：
Django 1.11 新增的查找方式。同 year， 据星期 进行查找。1表示星期天，7表示星期六， 2-6代
表的是星期一到星期五。
20. time：
 据时间进行查找。示例代 如下：select ... from article where pub_time between  '2018-01-01'  and '2018-12-12' 。
articles = Article.objects.filter(pub_date__date= date(2018,3,29))
select ... WHERE DATE( CONVERT_TZ( `front_article`. `pub_date`, 'UTC',
'Asia/Shanghai')) = 2018-03-29
articles = Article.objects.filter(pub_date__year= 2018)
articles = Article.objects.filter(pub_date__year__gte= 2017)
select ... where pub_date between  '2018-01-01'  and '2018-12-31' ;
select ... where pub_date >= '2017-01-01' ;
articles = Article.objects.filter(pub_date__time= datetime. time(12,12,12));
以上的代 是获取每一天中12点12分12秒发表的所有文 。
更多的关于时间的过滤，请参考 Django官方文档： https://docs.djangoproject.com/en/5.0/ref/model
s/querysets/#range 。
21. isnull ：
 据值是否为空进行查找。示例代 如下：
以上的代 的意思是获取所有发布日期不为空的文 。
将来翻译成 SQL语句如下：
22. regex 和iregex：
大小写敏感和大小写不敏感的正则表达式。示例代 如下：
以上代 的意思是提取所有 题以 hello字符串开头的文 。
将翻译成以下的 SQL语句：
iregex是大小写不敏感的。
23.  据关联的表进行查询：
假如现在有两个 ORM模型，一个是 Article ，一个是 Category 。代 如下：
比如想要获取文  题中包含"hello" 的所有的分类。那么可以通过以下代 来实现：
 articles = Article.objects.filter(pub_date__isnull= False)
select ... where pub_date is not null;
articles = Article.objects.filter(title__regex =r'^hello')
select ... where title regexp binary '^hello';
class Category( models.Model):
  """文 分类表"""
  name = models.CharField( max_length= 100)
class Article(models.Model):
  """文 表"""
  title = models.CharField( max_length= 100,null= True)
  category = models.ForeignKey( "Category", on_delete= models.CASCADE)
categories = Category. object.filter(article__title__contains( "hello"))
二、聚合函数：
如果 用原生 SQL，则可以使用聚合函数来提取数据。比如提取某个商品销售的数量，那么可以使用
Count，如果想要知道商品销售的平均价 ，那么可以使用 Avg。
聚合函数是通过 aggregate 方法来实现的。在讲解这些聚合函数的用法的时候，都是基于以下的模型对
象来实现的。
  from django.db import models
 class Author(models.Model):
  """作者模型"""
  name = models.CharField( max_length= 100)
  age = models.IntegerField ()
  email = models.EmailField()
  class Meta:
  db_table = 'author'
 class Publisher( models.Model):
  """出版社模型"""
  name = models.CharField( max_length= 300)
  class Meta:
  db_table = 'publisher'
 class Book(models.Model):
  """图书模型"""
  name = models.CharField( max_length= 300)
  pages = models.IntegerField ()
  price = models.FloatField()
  rating  = models.FloatField()
  author  = models.ForeignKey( Author,on_delete= models.CASCADE)
  publisher = models.ForeignKey( Publisher, on_delete= models.CASCADE)
  class Meta:
  db_table = 'book'
 class BookOrder( models.Model):
  """图书订单模型"""
  book = models.ForeignKey( "Book",on_delete= models.CASCADE)
  price = models.FloatField()
  class Meta:
  db_table = 'book_order'
1. Avg：求平均值
比如想要获取所有图书的价 平均值。那么可以使用以下代 实现。
以上的打印结果是：
其中price__avg 的结构是 据 field__avg 规则构成的。如果想要修改默认的名字，那么可以将 Avg赋
值给一个关键字参数。示例代 如下：
那么以上的结果打印为：

2. Count：获取指定的对象的个数。
示例代 如下：
以上的result将返回Book表中总共有多少本图书。
Count类中，还有另外一个参数叫做 distinct ，默认是等于 False，如果是等于 True，那么将去掉那
些重复的值。比如要获取作者表中所有的不重复的邮箱总共有多少个，那么可以通过以下代 来实现：

3. Max和Min：获取指定对象的最大值和最小值。
比如想要获取 Author表中，最大的年龄和最小的年龄分别是多少。那么可以通过以下代 来实现：
如果最大的年龄是88,最小的年龄是18。那么以上的result将为： from django.db.models import Avg
 result = Book.objects.aggregate( Avg('price' ))
 print(result)
 {"price__avg" :23.0}
 from django.db.models import Avg
 result = Book.objects.aggregate( my_avg=Avg('price' ))
 print(result)
 {"my_avg":23}
 from django.db.models import Count
 result = Book.objects.aggregate( book_num= Count('id'))
  from djang.db.models import Count
  result  = Author.objects.aggregate( count=Count('email',distinct= True))
 from django.db.models import Max,Min
 result = Author.objects.aggregate( Max('age'),Min( 'age'))

4. Sum：求指定对象的总和。
比如要求图书的销售总额。那么可以使用以下代 实现：
以上的代  annotate 的意思是给 Book表在查询的时候添 一个字段叫做 total，这个字段的数据来源
是从BookStore 模型的price的总和而来。 values方法是只提取 name和total两个字段的值。
更多的聚合函数请参考官方文档： https://docs.djangoproject.com/en/2.0/ref/models/querysets/#ag
gregation-functions

三、aggregate和annotate的区别：
1. aggregate ：返回使用聚合函数后的字段和值。
2. annotate ：在原来模型字段的基础之上添 一个使用了聚合函数的字段，并且在使用聚合函数的
时候，会使用当前这个模型的主键进行分组（group by ）。
比如以上 Sum的例子，如果使用的是 annotate ，那么将在每条图书的数据上都添 一个字段叫做
total，计算这本书的销售总额。
而如果使用的是 aggregate ，那么将求所有图书的销售总额。

四、F表达式和Q表达式：
1. F表达式：
F表达式是用来优化 ORM操作数据库的。比如我们要将公司所有员工的薪水都增 1000 元，如果按照正
常的流程，应该是先从数据库中提取所有的员工工资到Python内存中，然后使用Python代 在员工工资
的基础之上增 1000 元，最后再保存到数据库中。这里面涉及的流程就是，首先从数据库中提取数据到
Python内存中，然后在Python内存中做完运算，之后再保存到数据库中。示例代 如下：
而我们的 F表达式就可以优化这个流程，他可以不需要先把数据从数据库中提取出来，计算完成后再保存
回去，他可以直接执行 SQL语句，就将员工的工资增 1000 元。示例代 如下：
F表达式并不会马上从数据库中获取数据，而是在生成 SQL语句的时候，动态的获取 给 F表达式的值。 {"age__max":88,"age__min":18}
 from djang.db.models import Sum
 result =
Book.objects.annotate( total=Sum("bookstore__price" )).values ("name","total")
employees = Employee. objects.all()
for employee in employees:
  employee. salary += 1000
  employee. save()
from djang.db.models import F
Employee. object.update(salary=F("salary") +1000)
比如如果想要获取作者中， name和email相同的作者数据。如果不使用 F表达式，那么需要使用以下代
 来完成：
如果使用 F表达式，那么一行代 就可以搞定。示例代 如下：
2. Q表达式：
如果想要实现所有价 高于100 元，并且评分达到9.0以上评分的图书。那么可以通过以下代 来实现：
以上这个案例是一个并集查询，可以简单的通过 递多个条件进去来实现。
但是如果想要实现一些复杂的查询语句，比如要查询所有价 低于10元，或者是评分低于9分的图书。那
就没有办法通过 递多个条件进去实现了。这时候就需要使用Q表达式来实现了。示例代 如下：
以上是进行或运算，当然还可以进行其他的运算，比如有 &和~（非）等。一些用 Q表达式的例子如下：  authors  = Author.objects.all()
  for author in authors:
  if author.name == author.email:
  print( author)
  from django.db.models import F
  authors  = Author.objects.filter(name=F("email"))
books = Book.objects.filter(price__gte= 100,rating__gte= 9)
from django.db.models import Q
books = Book.objects.filter(Q(price__lte= 10) | Q(rating__lte= 9))
from django.db.models import Q
# 获取id等于3的图书
books = Book.objects.filter(Q(id=3))
# 获取id等于3，或者名字中包含文字"记"的图书
books = Book.objects.filter(Q(id=3)|Q(name__contains( "记")))
# 获取价 大于100，并且书名中包含"记"的图书
books = Book.objects.filter(Q(price__gte= 100)&Q(name__contains( "记")))
# 获取书名包含“记”，但是id不等于3的图书
books = Book.objects.filter(Q(name__contains= '记') & ~Q(id=3))
QuerySet API ：
我们通常做查询操作的时候，都是通过 模型名字.objects 的方式进行操作。其实 模型名字.objects 是一
个django.db.models.manager.Manager 对象，而 Manager 这个类是一个“空壳”的类，他本身是没有任
何的属性和方法的。他的方法全部都是通过 Python动态添 的方式，从 QuerySet 类中拷贝过来的。示
例图如下：
所以我们如果想要学  ORM模型的查找操作，必须首先要学会 QuerySet 上的一些 API的使用。

一、返回新的QuerySet的方法：
在使用QuerySet 进行查找操作的时候，可以提供多种操作。比如过滤完后还要 据某个字段进行排序，
那么这一系列的操作我们可以通过一个非常流畅的 链式调用 的方式进行。比如要从文 表中获取 题为
123，并且提取后要将结果 据发布的时间进行排序，那么可以使用以下方式来完成：
可以看到 order_by 方法是直接在 filter执行后调用的。这说明 filter返回的对象是一个拥有
order_by 方法的对象。而这个对象正是一个新的 QuerySet 对象。 此可以使用 order_by 方法。

二、常用的QuerySet方法
那么以下将介绍在那些会返回新的 QuerySet 对象的方法。
1. filter：将满足条件的数据提取出来，返回一个新的 QuerySet 。具体的 filter可以提供什么条
件查询。请见查询操作 节。
2. exclude ：排除满足条件的数据，返回一个新的 QuerySet 。示例代 如下：articles = Article.objects.filter(title='123').order_by( 'create_time')
以上代 的意思是提取那些 题不包含 hello的图书。
3. annotate ：给QuerySet 中的每个对象都添 一个使用查询表达式（聚合函数、F表达式、Q表达
式、Func表达式等）的新字段。示例代 如下：
以上代 将在每个对象中都添 一个 author__name 的字段，用来显示这个文 的作者的年龄。
4. order_by ：指定将查询的结果 据某个字段进行排序。如果要倒叙排序，那么可以在这个字段的
前面 一个负号。示例代 如下：
一定要注意的一点是，多个 order_by ，会把前面排序的规则给打乱，而使用后面的排序方式。比
如以下代 ：
他会 据作者的名字进行排序，而不是使用文 的创建时间。
5. values：用来指定在提取数据出来，需要提取哪些字段。默认情况下会把表中所有的字段全部都
提取出来，可以使用 values来进行指定，并且使用了 values方法后，提取出的 QuerySet 中的数
据类型不是模型，而是在 values方法中指定的字段和值形成的字典：
以上打印出来的 article 是类似于 {"title":"abc","content":"xxx"} 的形式。
如果在values中没有 递任何参数，那么将会返回这个恶模型中所有的属性。
6. values_list ：类似于 values。只不过返回的 QuerySet 中，存储的不是字典，而是元组。示例
代 如下：
那么在打印 articles 后，结果为 <QuerySet [(1,'abc'),(2,'xxx'),...]> 等。
如果在values_list 中只有一个字段。那么 可以 递 flat=True 来将结果扁平化。示例代 如
下： Article.objects.exclude(title__contains= 'hello')
 articles = Article.objects.annotate( author_name= F("author__name"))
 #  据创建的时间正序排序
 articles = Article.objects.order_by( "create_time")
 #  据创建的时间倒序排序
 articles = Article.objects.order_by( "-create_time")
 #  据作者的名字进行排序
 articles = Article.objects.order_by( "author__name")
 # 首先 据创建的时间进行排序，如果时间相同，则 据作者的名字进行排序
 articles = Article.objects.order_by( "create_time", 'author__name')
 articles = Article.objects.order_by( "create_time").order_by( "author__name")
 articles = Article.objects.values("title",'content')
 for article  in articles:
  print( article)
 articles = Article.objects.values_list( "id","title")
 print(articles)
7. all：获取这个 ORM模型的QuerySet 对象。
8. select_related ：在提取某个模型的数据的同时，也提前将相关联的数据提取出来。比如提取文
 数据，可以使用 select_related 将author信息提取出来，以后再次使用 article.author 的
时候就不需要再次去访问数据库了。可以减少数据库查询的次数。示例代 如下：
select_related 只能用在 一对多或者一对一中，不能用在 多对多或者多对一中。比如可以提前
获取文 的作者，但是不能通过作者获取他的文 ，或者是通过某篇文 获取这个文 所有的
签。
9. prefetch_related ：这个方法和 select_related 非常的类似，就是在访问多个表中的数据的时
候，减少查询的次数。这个方法是为了解决 多对一和多对多的关系的查询问题。比如要获取 题中
带有hello字符串的文 以及他的所有 签，示例代 如下：
但是如果在使用 article.tag_set 的时候，如果又创建了一个新的 QuerySet 那么会把之前的 SQL
优化给 坏掉。比如以下代 ：
那如果确实是想要在查询的时候指定过滤条件该如何做呢，这时候我们可以使用
django.db.models.Prefetch 来实现， Prefetch 这个可以提前定义好 queryset 。示例代 如
下： articles1 = Article.objects.values_list( "title")
 >> <QuerySet [("abc",),("xxx",),...] >
 articles2 = Article.objects.values_list( "title",flat=True)
 >> <QuerySet ["abc", 'xxx',...]>
 article = Article.objects.get(pk=1)
 >> article.author # 重新执行一次查询语句
 article = Article.objects.select_related( "author").get( pk=2)
 >> article.author # 不需要重新执行查询语句了
 from django.db import connection
 articles =
Article.objects.prefetch_related( "tag_set").filter (title__contains= 'hello')
 print(articles. query) # 通过这条命令查看在底层的SQL语句
 for article  in articles:
  print( "title:", article.title)
  print( article.tag_set.all())
 # 通过以下代 可以看出以上代 执行的sql语句
 for sql in connection. queries:
  print( sql)
 tags = Tag.obejcts .prefetch_related( "articles")
 for tag in tags:
  articles = tag.articles. filter(title__contains= 'hello') # 为filter方法会
重新生成一个QuerySet， 此会 坏掉之前的sql优化
 # 通过以下代 ，我们可以看到在使用了filter的，他的sql查询会更多，而没有使用filter的，只
有两次sql查询
 for sql in connection. queries:
  print( sql)
 为使用了 Prefetch ，即使在查询文 的时候使用了 filter，也只会发生两次查询操作。
10. defer：在一些表中，可能存在很多的字段，但是一些字段的数据量可能是比较庞大的，而此时
又不需要，比如我们在获取文 列表的时候，文 的内容我们是不需要的， 此这时候我们就可以
使用defer来过滤掉一些字段。这个字段跟 values有点类似，只不过 defer返回的不是字典，而
是模型。示例代 如下：
在看以上代 的 sql语句， 就可以看到，查找文 的字段，除了 title，其他字段都查找出来
了。当然， 也可以使用 article.title 来获取这个文 的 题，但是会重新执行一个查询的语
句。示例代 如下：
defer虽然能过滤字段，但是有些字段是不能过滤的，比如 id，即使 过滤了，也会提取出来。
11. only：跟defer类似，只不过 defer是过滤掉指定的字段，而 only是只提取指定的字段。
12. get：获取满足条件的数据。这个函数只能返回一条数据，并且如果给的条件有多条数据，那么这
个方法会抛出 MultipleObjectsReturned 错误，如果给的条件没有任何数据，那么就会抛出
DoesNotExit 错误。所以这个方法在获取数据的只能，只能有且只有一条。
13. create：创建一条数据，并且保存到数据库中。这个方法相当于先用指定的模型创建一个对象，
然后再调用这个对象的 save方法。示例代 如下： tags =
Tag.objects .prefetch_related( Prefetch( "articles", queryset= Article.objects.fil
ter(title__contains= 'hello'))).all()
 for tag in tags:
  articles = tag.articles. all()
  for article in articles:
  print( article)
 for sql in connection. queries:
  print( '='*30)
  print( sql)
articles = list(Article.objects.defer("title"))
for sql in connection. queries:
  print( '='*30)
  print( sql)
articles = list(Article.objects.defer("title"))
for article  in articles:
  #  为在上面提取的时候过滤了title
  # 这个地方重新获取title，将重新向数据库中进行一次查找操作
  print( article.title)
for sql in connection. queries:
  print( '='*30)
  print( sql)
article = Article(title='abc')
article.save()
# 下面这行代 相当于以上两行代
article = Article.objects.create(title='abc')
14. get_or_create ： 据某个条件进行查找，如果找到了那么就返回这条数据，如果没有查找到，那
么就创建一个。示例代 如下：
如果有 题等于 默认分类 的分类，那么就会查找出来，如果没有，则会创建并且存储到数据库中。
这个方法的返回值是一个元组，元组的第一个参数 obj是这个对象，第二个参数 created 代表是否
创建的。
15. bulk_create ：一次性创建多个数据。示例代 如下：
16. count：获取提取的数据的个数。如果想要知道总共有多少条数据，那么建议使用 count，而不是
使用len(articles) 这种。 为 count在底层是使用 select count(*) 来实现的，这种方式比使
用len函数更 的高效。
17. first和last：返回QuerySet 中的第一条和最后一条数据。
18. aggregate ：使用聚合函数。
19. exists：判断某个条件的数据是否存在。如果要判断某个条件的元 是否存在，那么建议使用
exists，这比使用 count或者直接判断 QuerySet 更有效得多。示例代 如下：
20. distinct ：去除掉那些重复的数据。这个方法如果底层数据库用的是 MySQL，那么不能 递任何
的参数。比如想要提取所有销售的价 超过80元的图书，并且 掉那些重复的，那么可以使用
distinct 来帮我们实现，示例代 如下：
需要注意的是，如果在 distinct 之前使用了 order_by ，那么 为 order_by 会提取order_by 中
指定的字段， 此再使用 distinct 就会 据多个字段来进行唯一化，所以就不会把那些重复的数
据 掉。示例代 如下：
那么以上代  为使用了 order_by ，即使使用了 distinct ，也会把重复的 book_id 提取出来。
21. update：执行更新操作，在 SQL底层走的也是 update命令。比如要将所有 category 为空的
article 的article 字段都更新为默认的分类。示例代 如下：obj,created = Category. objects.get_or_create( title='默认分类')
Tag.objects .bulk_create([
  Tag( name='111'),
  Tag( name='222'),
])
if Article.objects.filter(title__contains= 'hello').exists ():
  print( True)
比使用count更高效：
if Article.objects.filter(title__contains= 'hello').count() >  0:
  print( True)
也比直接判断QuerySet更高效：
if Article.objects.filter(title__contains= 'hello'):
  print( True)
books = Book.objects.filter(bookorder__price__gte= 80).distinct()
orders =
BookOrder. objects.order_by( "create_time").values ("book_id").distinct()
注意这个方法走的是更新的逻辑。所以更新完成后保存到数据库中不会执行 save方法， 此不会
更新auto_now 设置的字段。
22. delete： 除所有满足条件的数据。 除数据的时候，要注意 on_delete 指定的处理方式。
23. 切片操作：有时候我们查找数据，有可能只需要其中的一部分。那么这时候可以使用切片操作来帮
我们完成。 QuerySet 使用切片操作就跟列表使用切片操作是一 的。示例代 如下：
切片操作并不是把所有数据从数据库中提取出来再做切片操作。而是在数据库层面使用 LIMIE和
OFFSET来帮我们完成。所以如果只需要取其中一部分的数据的时候，建议大家使用切片操作。

三、什么时候 Django 会将QuerySet 转换为SQL去执
行：
生成一个 QuerySet 对象并不会马上转换为 SQL语句去执行。
比如我们获取 Book表下所有的图书：
我们可以看到在打印 connection.quries 的时候打印的是一个空的列表。说明上面的 QuerySet 并没有
真正的执行。
在以下情况下QuerySet 会被转换为 SQL语句执行：
1. 迭代：在遍历 QuerySet 对象的时候，会首先先执行这个 SQL语句，然后再把这个结果返回进行迭
代。比如以下代 就会转换为 SQL语句：
2. 使用步长做切片操作： QuerySet 可以类似于列表一 做切片操作。做切片操作本身不会执行 SQL
语句，但是如果如果在做切片操作的时候提供了步长，那么就会立马执行 SQL语句。需要注意的
是，做切片后不能再执行 filter方法，否则会报错。
3. 调用len函数：调用 len函数用来获取 QuerySet 中总共有多少条数据也会执行 SQL语句。
4. 调用list函数：调用 list函数用来将一个 QuerySet 对象转换为 list对象也会立马执行 SQL语
句。
5. 判断：如果对某个 QuerySet 进行判断，也会立马执行 SQL语句。Article.objects.filter(category__isnull= True).update (category_id= 3)
books = Book.objects.all()[1:3]
for book in books:
  print( book)
books = Book.objects.all()
print(connection. queries)
 for book in Book.objects.all():
  print( book)
ORM模型与表的同步

一、ORM模型同步到表中
1. 迁移命令：
1. makemigrations：将模型生成迁移脚本。模型所在的 app，必须放在 settings.py 中的
INSTALLED_APPS 中。这个命令有以下 个常用选项：
app_label：后面可以跟一个或者多个 app，那么就只会针对这 个app生成迁移脚本。如果
没有任何的app_label，那么会检查 INSTALLED_APPS 中所有的app下的模型，针对每一个app
都生成响应的迁移脚本。
--name：给这个迁移脚本指定一个名字。
--empty：生成一个空的迁移脚本。如果 想写自己的迁移脚本，可以使用这个命令来实现一
个空的文件，然后自己再在文件中写迁移脚本。
2. migrate：将新生成的迁移脚本。 射到数据库中。创建新的表或者修改表的结构。以下一些常用的
选项：
app_label：将某个 app下的迁移脚本 射到数据库中。如果没有指定，那么会将所有在
INSTALLED_APPS 中的app下的模型都 射到数据库中。
app_label migrationname：将某个 app下指定名字的 migration 文件 射到数据库中。
--fake：可以将指定的迁移脚本名字添 到数据库中。但是并不会把迁移脚本转换为SQL语
句，修改数据库中的表。
--fake-initial ：将第一次生成的迁移文件版本号记录在数据库中。但并不会真正的执行迁移脚
本。
3. showmigrations：查看某个app下的迁移文件。如果后面没有app，那么将查看 INSTALLED_APPS
中所有的迁移文件。
4. sqlmigrate：查看某个迁移文件在 射到数据库中的时候，转换的 SQL语句。

二、migrations 中的迁移版本和数据库中的迁移版本对不
上怎么办？
1. 找到哪里不一致，然后使用 python manage.py --fake [版本名字] ，将这个版本 记为已经
射。
2.  除指定 app下migrations 和数据库表 django_migrations 中和这个 app相关的版本号，然后
将模型中的字段和数据库中的字段保持一致，再使用命令 python manage.py makemigrations 重
新生成一个初始化的迁移脚本，之后再使用命令 python manage.py makemigrations --fake-
initial 来将这个初始化的迁移脚本 记为已经 射。以后再修改就没有问题了。
更多关于迁移脚本的。请查看官方文档： https://docs.djangoproject.com/en/5.0/topics/migrations/

三、 据已有的表自动生成模型：
在实际开发中，有些时候可能数据库已经存在了。如果我们用 Django来开发一个网站，读取的是之前已
经存在的数据库中的数据。那么该如何将模型与数据库中的表 射呢？ 据旧的数据库生成对应的 ORM
模型，需要以下 个步骤：
1. Django给我们提供了一个 inspectdb 的命令，可以非常方便的将已经存在的表，自动的生成模
型。想要使用 inspectdb 自动将表生成模型。首先需要在 settings.py 中配置好数据库相关信
息。不然就找不到数据库。示例代 如下：
比如有以下表：
article表：
tag表：
article_tag 表：
 DATABASES = {
  'default': {
  'ENGINE': 'django.db.backends.mysql',
  'NAME' : "migrations_demo" ,
  'HOST' : '127.0.0.1',
  'PORT' : '3306' ,
  'USER' : 'root' ,
  'PASSWORD': 'root'
  }
 }
front_user表：
那么通过 python manage.py inspectdb ，就会将表转换为模型后的代 ，显示在终端：
以上代 只是显示在终端。如果想要保存到文件中。那么可以使用 >重定向输出到指定的文
件。比如让他输出到 models.py 文件中。示例命令如下：from django.db import models
class ArticleArticle( models.Model):
  title = models.CharField( max_length= 100)
  content = models.TextField( blank=True, null= True)
  create_time = models.DateTimeField( blank=True, null= True)
  author = models.ForeignKey( 'FrontUserFrontuser', models .DO_NOTHING,
blank=True, null= True)
  class Meta:
  managed  = False
  db_table = 'article_article'
class ArticleArticleTags (models.Model):
  article = models.ForeignKey( ArticleArticle, models .DO_NOTHING)
  tag = models.ForeignKey( 'ArticleTag' , models .DO_NOTHING)
  class Meta:
  managed  = False
  db_table = 'article_article_tags'
  unique_together = (('article', 'tag'),)
class ArticleTag( models.Model):
  name = models.CharField( max_length= 100)
  class Meta:
  managed  = False
  db_table = 'article_tag'
class FrontUserFrontuser (models.Model):
  username = models.CharField( max_length= 100)
  telephone = models.CharField( max_length= 11)
  class Meta:
  managed  = False
  db_table = 'front_user_frontuser'
python manage.py inspectdb > models.py
以上的命令，只能在终端执行，不能在 pycharm->Tools->Run manage.py Task... 中使
用。
如果只是想要转换一个表为模型。那么可以指定表的名字。示例命令如下：
2. 修正模型：新生成的 ORM模型有些地方可能不太适合使用。比如模型的名字，表之间的关系等等。
那么以下选项还需要重新配置一下：
模型名：自动生成的模型，是 据表的名字生成的，可能不是 想要的。这时候模型的名字
可以改成任何 想要的。
模型所属app： 据自己的需要，将相应的模型放在对应的app中。放在同一个app中也是没
有任何问题的。只是不方便管理。
模型外键引用：将所有使用 ForeignKey 的地方，模型引用都改成字符串。这 不会产生模型
顺序的问题。另外，如果引用的模型已经移动到其他的app中了，那么还要 上这个app的前
缀。
让Django管理模型：将 Meta下的managed=False  掉，如果保留这个，那么以后这个模型
有任何的修改，使用 migrate 都不会 射到数据库中。
当有多对多的时候，应该也要修正模型。将中间表注释了，然后使用 ManyToManyField 来实
现多对多。并且，使用 ManyToManyField 生成的中间表的名字可能和数据库中那个中间表的
名字不一致，这时候肯定就不能正常连接了。那么可以通过 db_table 来指定中间表的名字。
示例代 如下：
表名：切记不要修改表的名字。不然 射到数据库中，会发生找不到对应表的错误。
3. 执行命令 python manage.py makemigrations 生成初始化的迁移脚本。方便后面通过 ORM来管理
表。这时候还需要执行命令 python manage.py migrate --fake-initial ， 为如果不使用 --
fake-initial ，那么会将迁移脚本会 射到数据库中。这时候迁移脚本会新创建表，而这个表之
前是已经存在了的，所以肯定会报错。此时我们只要将这个 0001-initial 的状态修改为已经
射，而不真正执行 射，下次再 migrate 的时候，就会忽略他。
4. 将Django的 心表 射到数据库中： Django中还有一些 心的表也是需要创建的。不然有些功能
是用不了的。比如 auth相关表。如果这个数据库之前就是使用 Django开发的，那么这些表就已经
存在了。可以不用管了。如果之前这个数据库不是使用 Django开发的，那么应该使用 migrate 命
令将Django中的 心模型 射到数据库中。python manage.py inspectdb article_article > models.py
class Article(models.Model):
 title = models.CharField( max_length= 100, blank= True, null= True)
 content = models.TextField( blank=True, null= True)
 author = models.ForeignKey( 'front.User' , models .SET_NULL, blank= True,
null=True)
 # 使用ManyToManyField模型到表，生成的中间表的规则是：article_tags
 # 但现在已经存在的表的名字叫做：article_tag
 # 可以使用db_table，指定中间表的名字
 tags = models.ManyToManyField( "Tag",db_table= 'article_tag')
 class Meta:
  db_table = 'article'
ORM查询作业

一、题目
假设有以下 ORM模型：
使用之前学到过的操作实现下面的查询操作：
1. 查询平均成绩大于60分的同学的id和平均成绩；
2. 查询所有同学的id、姓名、选课的数量、总成绩；
3. 查询姓“李”的老师的个数；
4. 查询没学过“李老师”课的同学的id、姓名；
5. 查询学过课程id为1和2的所有同学的id、姓名；
6. 查询学过“黄老师”所教的“所有课”的同学的id、姓名；
7. 查询所有课程成绩小于60分的同学的id和姓名；
8. 查询没有学全所有课的同学的id、姓名；from django.db import models
class Student(models.Model):
  """学生表"""
  name = models.CharField( max_length= 100)
  gender  = models.SmallIntegerField ()
  class Meta:
  db_table = 'student'
class Course(models.Model):
  """课程表"""
  name = models.CharField( max_length= 100)
  teacher  = models.ForeignKey( "Teacher", on_delete= models.SET_NULL, null=True)
  class Meta:
  db_table = 'course'
class Score(models.Model):
  """分数表"""
  student  = models.ForeignKey( "Student", on_delete= models.CASCADE)
  course  = models.ForeignKey( "Course", on_delete= models.CASCADE)
  number  = models.FloatField()
  class Meta:
  db_table = 'score'
class Teacher(models.Model):
  """老师表"""
  name = models.CharField( max_length= 100)
  class Meta:
  db_table = 'teacher'
9. 查询所有学生的姓名、平均分，并且按照平均分从高到低排序；
10. 查询各科成绩的最高和最低分，以如下形式显示：课程ID，课程名称，最高分，最低分；
11. 查询没门课程的平均成绩，按照平均成绩进行排序；
12. 统计总共有多少女生，多少男生；
13. 将“黄老师”的每一门课程都在原来的基础之上 5分；
14. 查询两门以上不及 的同学的id、姓名、以及不及 课程数；
15. 查询每门课的选课人数；

二、参考答案
1. 查询平均成绩大于60分的同学的id和平均成绩；
2. 查询所有同学的id、姓名、选课的数、总成绩；
3. 查询姓“李”的老师的个数；
4. 查询没学过“黄老师”课的同学的id、姓名；
5. 查询学过课程id为1和2的所有同学的id、姓名；
6. 查询学过“黄老师”所教的所有课的同学的学号、姓名； rows =
Student.objects.annotate( avg=Avg("score__number")).filter (avg__gte= 60).values
("id","avg")
 for row in rows:
  print( row)
 rows =
Student.objects.annotate( course_nums= Count("score__course"),total_score= Sum("
score__number"))
 .values("id","name","course_nums", "total_score")
 for row in rows:
  print( row)
 teacher_nums  = Teacher.objects.filter(name__startswith= "李").count()
 print(teacher_nums )
 rows = Student.objects.exclude(score__course__teacher__name ="黄老
师").values ('id','name')
 for row in rows:
  print( row)
 rows = Student.objects.filter(score__course__in =
[1,2]).distinct().values ('id','name')
 for row in rows:
  print( row)
7. 查询所有课程成绩小于60分的同学的id和姓名；
8. 查询没有学全所有课的同学的id、姓名；
9. 查询所有学生的姓名、平均分，并且按照平均分从高到低排序；
10. 查询各科成绩的最高和最低分，以如下形式显示：课程ID，课程名称，最高分，最低分：
11. 查询每门课程的平均成绩，按照平均成绩进行排序；
12. 统计总共有多少女生，多少男生； rows =
Student.objects.annotate( nums=Count("score__course", filter=Q(score__course__t
eacher__name ='黄老师')))
 .filter(nums=Course.objects.filter(teacher__name= '黄老
师').count()).values ('id','name')
 for row in rows:
  print( row)
 students = Student.objects.exclude(score__number__gt =60)
 for student  in students:
  print( student)
 students =
Student.objects.annotate( num=Count( F("score__course"))).filter (num__lt=Course
.objects.count()).values ('id','name')
 for student  in students:
  print( student)
 students = Student.objects.annotate( avg=Avg("score__number")).order_by( "-
avg").values ('name','avg')
 for student  in students:
  print( student)
courses =
Course.objects.annotate( min=Min("score__number"),max= Max("score__number")).va
lues("id",'name','min','max')
for course  in courses:
  print( course)
courses =
Course.objects.annotate(avg=Avg("score__number")).order_by('avg').values('id'
,'name','avg')
for course in courses:
  print(course)
rows =
Student.objects.aggregate( male_num= Count("gender", filter=Q(gender=1)),female_
num=Count( "gender", filter=Q(gender=2)))
print(rows)
13. 将“黄老师”的每一门课程都在原来的基础之上 5分；
14. 查询两门以上不及 的同学的id、姓名、以及不及 课程数；
15. 查询每门课的选课人数；rows = Score.objects.filter(course__teacher__name= '黄老
师').update (number=F("number") +5)
print(rows)
students =
Student.objects.annotate( bad_count= Count("score__number", filter=Q(score__numb
er__lt=60))).filter (bad_count__gte= 2).values ('id','name','bad_count')
for student  in students:
  print( student)
courses =
Course.objects.annotate( student_nums =Count("score__student")).values ('id','na
me','student_nums')
for course  in courses:
  print( course)
Django限制请求method

一、常用的请求method：
1. GET请求：GET请求一般用来向服务器索取数据，但不会向服务器提交数据，不会对服务器的状态
进行更改。比如向服务器获取某篇文 的详情。
2. POST请求：POST请求一般是用来向服务器提交数据，会对服务器的状态进行更改。比如提交一篇
文 给服务器。

二、限制请求装饰器：
Django内置的视图装饰器可以给视图提供一些限制。比如这个视图只能通过 GET的method访问等。以
下将介绍一些常用的内置视图装饰器。
1. django.http.decorators.http.require_http_methods ：这个装饰器需要 递一个允许访问的
方法的列表。比如只能通过 GET的方式访问。那么示例代 如下：
2. django.views.decorators.http.require_GET ：这个装饰器相当于是
require_http_methods(['GET']) 的简写形式，只允许使用 GET的method来访问视图。示例代
 如下：
3. django.views.decorators.http.require_POST ：这个装饰器相当于是
require_http_methods(['POST']) 的简写形式，只允许使用 POST的method来访问视图。示例
代 如下：
4. django.views.decorators.http.require_safe ：这个装饰器相当于是
require_http_methods(['GET','HEAD']) 的简写形式，只允许使用相对安全的方式来访问视
图。 为 GET和HEAD不会对服务器产生增 改的行为。 此是一种相对安全的请求方式。示例代
 如下： from django.views.decorators. http import require_http_methods
 @require_http_methods(["GET"])
 def my_view (request):
  pass
 from django.views.decorators. http import require_GET
 @require_GET
 def my_view (request):
  pass
 from django.views.decorators. http import require_POST
 @require_POST
 def my_view (request):
  pass
 from django.views.decorators. http import require_safe
 @require_safe
 def my_view (request):
  pass
页面重定向
重定向分为永久性重定向和暂时性重定向，在页面上体现的操作就是浏览器会从一个页面自动跳转到另
外一个页面。比如用户访问了一个需要权限的页面，但是该用户当前并没有登录， 此我们应该给他重
定向到登录页面。
永久性重定向：http的状态 是301 ，多用于旧网址被废弃了要转到一个新的网址确保用户的访
问，最经典的就是京东网站， 输入 www.jingdong.com 的时候，会被重定向到 www.jd.com ，
为jingdong.com 这个网址已经被废弃了，被改成jd.com，所以这种情况下应该用永久重定向。
暂时性重定向：http的状态 是302 ，表示页面的暂时性跳转。比如访问一个需要权限的网址，如
果当前用户没有登录，应该重定向到登录页面，这种情况下，应该用暂时性重定向。
在Django中，重定向是使用 redirect(to, *args, permanent=False, **kwargs) 来实现的。 to是
一个url，permanent 代表的是这个重定向是否是一个永久的重定向，默认是 False。关于重定向的使
用，请看以下例子：
from django.shortcuts import reverse,redirect
def profile (request):
  if request .GET.get("username"):
  return HttpResponse ("%s，欢迎来到个人中心页面！")
  else:
  return redirect( reverse("user:login" ))
WSGIRequest对象
Django在接收到http请求之后，会 据http请求携带的参数以及报文信息创建一个 WSGIRequest 对象，
并且作为视图函数第一个参数 给视图函数。也就是我们经常看到的 request 参数。在这个对象上我们
可以找到客户端上 上来的所有信息。这个对象的完整路径是
django.core.handlers.wsgi.WSGIRequest 。

一、WSGIRequest对象常用属性和方法：
1. WSGIRequest 对象常用属性：
WSGIRequest 对象上大部分的属性都是只读的。 为这些属性是从客户端上 上来的，没必要做任何的
修改。以下将对一些常用的属性进行讲解：
1. path：请求服务器的完整“路径”，但不包含域名和参数。比如
http://www.baidu.com/xxx/yyy/ ，那么path就是/xxx/yyy/ 。
2. method：代表当前请求的 http方法。比如是 GET还是POST。
3. GET：一个django.http.request.QueryDict 对象。操作起来类似于字典。这个属性中包含了所
有以?xxx=xxx 的方式上 上来的参数。
4. POST：也是一个 django.http.request.QueryDict 对象。这个属性中包含了所有以 POST方式上
 上来的参数。
5. FILES：也是一个 django.http.request.QueryDict 对象。这个属性中包含了所有上 的文件。
6. COOKIES ：一个 准的Python字典，包含所有的 cookie，键值对都是字符串类型。
7. session ：一个类似于字典的对象。用来操作服务器的 session 。
8. META：存储的客户端发送上来的所有 header信息。
9. CONTENT_LENGTH ：请求的正文的长度（是一个字符串）。
10. CONTENT_TYPE ：请求的正文的MIME类型。
11. HTTP_ACCEPT ：响应可接收的Content-Type 。
12. HTTP_ACCEPT_ENCODING ：响应可接收的编 。
13. HTTP_ACCEPT_LANGUAGE ： 响应可接收的语言。
14. HTTP_HOST ：客户端发送的HOST值。
15. HTTP_REFERER ：在访问这个页面上一个页面的url。
16. QUERY_STRING ：单个字符串形式的查询字符串（未解析过的形式）。
17. REMOTE_ADDR ：客户端的IP地址。如果服务器使用了 nginx做反向代理或者负载均衡，那么这个值
返回的是 127.0.0.1 ，这时候可以使用 HTTP_X_FORWARDED_FOR 来获取，所以获取 ip地址的代
片段如下：
  if request.META.has_key('HTTP_X_FORWARDED_FOR'):
  ip =  request .META['HTTP_X_FORWARDED_FOR']
  else:
  ip = request.META['REMOTE_ADDR']
18. REMOTE_HOST ：客户端的主机名。
19. REQUEST_METHOD ：请求方法。一个字符串类似于 GET或者POST。
20. SERVER_NAME ：服务器域名。
21. SERVER_PORT ：服务器端口号，是一个字符串类型。
2. WSGIRequest 对象常用方法：
1. is_secure() ：是否是采用 https协议。
2. get_host() ：服务器的域名。如果在访问的时候还有端口号，那么会 上端口号。比如
www.baidu.com:9000 。
3. get_full_path() ：返回完整的path。如果有查询字符串，还会 上查询字符串。比
如/music/bands/?print=True 。
4. get_raw_uri() ：获取请求的完整 url。

二、QueryDict 对象：
我们平时用的 request.GET 和request.POST 都是QueryDict 对象，这个对象继承自 dict， 此用法
跟dict相差  。其中用得比较多的是 get方法和getlist 方法。
1. get方法：用来获取指定 key的值，如果没有这个 key，那么会返回 None。
2. getlist 方法：如果浏览器上 上来的 key对应的值有多个，那么就需要通过这个方法获取。
HttpResponse对象
Django服务器接收到客户端发送过来的请求后，会将提交上来的这些数据封装成一个 HttpRequest 对象
 给视图函数。那么视图函数在处理完相关的逻辑后，也需要返回一个响应给浏览器。而这个响应，我
们必须返回 HttpResponseBase 或者他的子类的对象。而 HttpResponse 则是HttpResponseBase 用得
最多的子类。那么接下来就来介绍一下 HttpResponse 及其子类。

一、常用属性：
1. content：返回的内容。
2. status_code：返回的HTTP响应状态 。
3. content_type：返回的数据的MIME类型，默认为 text/html 。浏览器会 据这个属性，来显示数
据。如果是 text/html ，那么就会解析这个字符串，如果 text/plain ，那么就会显示一个纯文
本。常用的 Content-Type 如下：
text/html（默认的，html文件）
text/plain（纯文本）
text/css（css文件）
text/javascript（js文件）
multipart/form-data（文件提交）
application/json （json 输）
application/xml（xml文件）
4. 设置请求头： response['X-Access-Token'] = 'xxxx' 。
二、常用方法：
1. set_cookie：用来设置 cookie信息。后面讲到授权的时候会着重讲到。
2. delete_cookie：用来 除 cookie信息。
3. write： HttpResponse 是一个类似于文件的对象，可以用来写入数据到数据体（content）中。

三、JsonResponse 类：
用来对象 dump成json字符串，然后返回将 json字符串封装成 Response 对象返回给浏览器。并且他的
Content-Type 是application/json 。示例代 如下：
默认情况下 JsonResponse 只能对字典进行 dump，如果想要对非字典的数据进行 dump，那么需要给
JsonResponse  递一个 safe=False 参数。示例代 如下：from django.http import JsonResponse
def index( request):
  return  JsonResponse ({"username": "zhiliao", "age":18})
以上代 会报错，应该在使用 HttpResponse 的时候， 入一个 safe=False 参数，示例代 如下：from django.http import JsonResponse
def index( request):
  persons  = [' 三','李四','王五']
  return  HttpResponse (persons)
return HttpResponse (persons,safe=False)
生成CSV文件：
有时候我们做的网站，需要将一些数据，生成有一个 CSV文件给浏览器，并且是作为附件的形式下载下
来。以下将讲解如何生成 CSV文件。

一、生成小的CSV文件：
这里将用一个生成小的 CSV文件为例，来把生成 CSV文件的技术要点讲到位。我们用 Python内置的
csv模块来处理 csv文件，并且使用 HttpResponse 来将csv文件返回回去。示例代 如下：
这里再来对每个部分的代 进行解释：
1. 我们在初始化 HttpResponse 的时候，指定了 Content-Type 为text/csv ，这将告诉浏览器，这
是一个csv 式的文件而不是一个 HTML 式的文件，如果用默认值，默认值就是 html，那么浏览
器将把csv 式的文件按照 html 式输出，这肯定不是我们想要的。
2. 第二个我们还在 response 中添 一个 Content-Disposition 头，这个东西是用来告诉浏览器该如
何处理这个文件，我们给这个头的值设置为 attachment; ，那么浏览器将不会对这个文件进行显
示，而是作为附件的形式下载，第二个 filename="somefilename.csv" 是用来指定这个 csv文件
的名字。
3. 我们使用 csv模块的writer方法，将相应的数据写入到 response 中。

二、将csv文件定义成模板：
我们还可以将 csv 式的文件定义成模板，然后使用 Django内置的模板系统，并给这个模板 入一个
Context 对象，这 模板系统就会 据 入的 Context 对象，生成具体的 csv文件。示例代 如下：
模板文件：
视图函数：import csv
from django.http import HttpResponse
def csv_view( request):
  response = HttpResponse (content_type ='text/csv')
  response[ 'Content-Disposition'] =  'attachment; filename="somefilename.csv"'
  writer  = csv.writer (response)
  writer .writerow(['username', 'age', 'height', 'weight'])
  writer .writerow(['zhiliao', '18', '180', '110'])
  return  response
{% for row in data %}"{{ row.0|addslashes }}", "{{ row.1|addslashes }}", "{{
row.2|addslashes }}", "{{ row.3|addslashes }}", "{{ row.4|addslashes }}"
{% endfor %}
from django.http import HttpResponse

三、生成大的CSV文件：
以上的例子是生成的一个小的 csv文件，如果想要生成大型的 csv文件，那么以上方式将有可能会发生
超时的情况（服务器要生成一个大型csv文件，需要的时间可能会超过浏览器默认的超时时间）。这时候
我们可以借助另外一个类，叫做 StreamingHttpResponse 对象，这个对象是将响应的数据作为一个流返
回给客户端，而不是作为一个整体返回。示例代 如下：
这里我们构建了一个非常大的数据集 rows，并且将其变成一个迭代器。然后 为
StreamingHttpResponse 的第一个参数只能是一个生成器， 此我们使用圆括号
(writer.writerow(row) for row in rows) ，并且 为我们要写的文件是 csv 式的文件， 此需
要调用writer.writerow 将row变成一个 csv 式的字符串。而调用 writer.writerow 又需要一个中
间的容器， 此这里我们定义了一个非常简单的类 Echo，这个类只实现一个 write方法，以后在执行
csv.writer(pseudo_buffer) 的时候，就会调用 Echo.writer 方法。
注意：StreamingHttpResponse 会启动一个进程来和客户端保持长连接，所以会很消耗资源。所以如果
不是特殊要求，尽量少用这种方法。
 from django.template import loader, Context
def some_view( request):
  response = HttpResponse (content_type ='text/csv')
  response[ 'Content-Disposition'] =  'attachment; filename="somefilename.csv"'
  csv_data = (
  ('First row', 'Foo', 'Bar', 'Baz'),
  ('Second row' , 'A', 'B', 'C', '"Testing"', "Here's a quote"),
  )
  t = loader.get_template ('my_template_name.txt')
  response. write(t.render({"data" : csv_data}))
  return  response
class Echo:
  """
  定义一个可以执行写操作的类，以后调用csv.writer的时候，就会执行这个方法
  """
  def write(self, value):
  return value
def large_csv( request):
  rows = (["Row {}". format(idx), str( idx)] for idx in range(655360))
  pseudo_buffer = Echo()
  writer  = csv.writer (pseudo_buffer)
  response = StreamingHttpResponse((writer .writerow( row) for row in
rows),content_type ="text/csv")
  response[ 'Content-Disposition'] =  'attachment; filename="somefilename.csv"'
  return  response
四、关于StreamingHttpResponse：
这个类是专门用来处理流数据的。使得在处理一些大型文件的时候，不会 为服务器处理时间过长而到
时连接超时。这个类不是继承自 HttpResponse ，并且跟 HttpResponse 对比有以下 点区别：
1. 这个类没有属性 content ，相反是 streaming_content 。
2. 这个类的 streaming_content 必须是一个可以迭代的对象。
3. 这个类没有 write方法，如果给这个类的对象写入数据将会报错。
注意：StreamingHttpResponse 会启动一个进程来和客户端保持长连接，所以会很消耗资源。所以如果
不是特殊要求，尽量少用这种方法。
类视图
在写视图的时候， Django除了使用函数作为视图，也可以使用类作为视图。使用类视图可以使用类的一
些特性，比如继承等。

一、View：
django.views.generic.base.View 是主要的类视图，所有的类视图都是继承自他。如果我们写自己的类
视图，也可以继承自他。然后再 据当前请求的 method，来实现不同的方法。比如这个视图只能使用
get的方式来请求，那么就可以在这个类中定义 get(self,request,*args,**kwargs) 方法。以此类
推，如果只需要实现 post方法，那么就只需要在类中实现 post(self,request,*args,**kwargs) 。
示例代 如下：
类视图写完后，还应该在 urls.py 中进行 射， 射的时候就需要调用 View的类方法 as_view() 来进
行转换。示例代 如下：
除了get方法，View还支持以下方法
['get','post','put','patch','delete','head','options','trace'] 。
如果用户访问了 View中没有定义的方法。比如 的类视图只支持 get方法，而出现了 post方法，那么
就会把这个请求转发给 http_method_not_allowed(request,*args,**kwargs) 。示例代 如下：
urls.py 中的 射如下：
如果 在浏览器中访问 addbook/ ， 为浏览器访问采用的是 get方法，而 addbook 只支持post方法，
 此以上视图会返回您当前采用的 method是：GET，本视图只支持使用 post请求！。
其实不管是 get请求还是 post请求，都会走 dispatch(request,*args,**kwargs) 方法，所以如果实
现这个方法，将能够对所有请求都处理到。from django.views import View
class BookDetailView( View):
  def get(self, request,*args,**kwargs ):
  return render(request,'detail.html')
urlpatterns = [
  path( "detail/<book_id>/", views.BookDetailView. as_view(),name= 'detail')
]
class AddBookView( View):
  def post(self,request,*args,**kwargs ):
  return HttpResponse ("书籍添 成功！")
  def http_method_not_allowed (self, request , *args, **kwargs ):
  return HttpResponse ("您当前采用的method是：%s，本视图只支持使用post请求！" %
request.method)
path("addbook/", views.AddBookView. as_view(),name= 'add_book')

二、TemplateView：
django.views.generic.base.TemplateView ，这个类视图是专门用来返回模版的。在这个类中，有两
个属性是经常需要用到的，一个是 template_name ，这个属性是用来存储模版的路径， TemplateView
会自动的渲染这个变量指向的模版。另外一个是 get_context_data ，这个方法是用来返回上下文数据
的，也就是在给模版 的参数的。示例代 如下：
在urls.py 中的 射代 如下：
如果在模版中不需要 递任何参数，那么可以直接只在 urls.py 中使用TemplateView 来渲染模版。示
例代 如下：

三、ListView：
在网站开发中，经常会出现需要列出某个表中的一些数据作为列表展示出来。比如文 列表，图书列表
等等。在 Django中可以使用 ListView 来帮我们快速实现这种需求。示例代 如下：from django.views.generic.base import TemplateView
class HomePageView (TemplateView ):
  template_name = "home.html"
  def get_context_data( self, **kwargs ):
  context = super().get_context_data( **kwargs )
  context['username'] =  "知了黄勇"
  return context
from django.urls import path
from myapp.views import HomePageView
urlpatterns = [
  path( '', HomePageView .as_view(), name= 'home'),
]
from django.urls import path
from django.views.generic import TemplateView
urlpatterns = [
  path( 'about/', TemplateView .as_view(template_name= "about.html" )),
]
class ArticleListView( ListView):
  model = Article
  template_name = 'article_list.html'
  paginate_by = 10
  context_object_name = 'articles'
  ordering = 'create_time'
对以上代 进行解释：
1. 首先ArticleListView 是继承自 ListView 。
2. model：重写model类属性，指定这个列表是给哪个模型的。
3. template_name ：指定这个列表的模板。
4. paginate_by ：指定这个列表一页中展示多少条数据。
5. context_object_name ：指定这个列表模型在模板中的参数名称。
6. ordering ：指定这个列表的排序方式。
7. page_kwarg ：获取第 页的数据的参数名称。默认是 page。
8. get_context_data ：获取上下文的数据。
9. get_queryset ：如果 提取数据的时候，并不是要把所有数据都返回，那么 可以重写这个方
法。将一些不需要展示的数据给过滤掉。

四、Paginator 和Page类：
Paginator 和Page类都是用来做分页的。他们在 Django中的路径为
django.core.paginator.Paginator 和django.core.paginator.Page 。以下对这两个类的常用属性
和方法做解释：
1. Paginator常用属性和方法：
1. count：总共有多少条数据。
2. num_pages ：总共有多少页。
3. page_range ：页面的区间。比如有三页，那么就 range(1,4) 。
2. Page常用属性和方法：
1. has_next ：是否还有下一页。
2. has_previous ：是否还有上一页。
3. next_page_number ：下一页的页 。
4. previous_page_number ：上一页的页 。
5. number：当前页。
6. start_index ：当前这一页的第一条数据的索引值。
7. end_index ：当前这一页的最后一条数据的索引值。  page_kwarg = 'page'
  def get_context_data( self, **kwargs ):
  context = super(ArticleListView, self).get_context_data( **kwargs )
  print(context)
  return context
  def get_queryset (self):
  return Article.objects.filter(id__lte=89)
五、给类视图添 装饰器：
在开发中，有时候需要给一些视图添 装饰器。如果用函数视图那么非常简单，只要在函数的上面写上
装饰器就可以了。但是如果想要给类添 装饰器，那么可以通过以下两种方式来实现：
1. 装饰dispatch方法：
2. 直接装饰在整个类上：  from django.utils.decorators import method_decorator
def login_required( func):
  def wrapper(request,*args,**kwargs ):
  if request.GET.get("username"):
  return  func(request,*args,**kwargs )
  else:
  return  redirect( reverse('index'))
  return  wrapper
class IndexView( View):
  def get(self, request,*args,**kwargs ):
  return HttpResponse ("index")
  @method_decorator (login_required)
  def dispatch( self, request , *args, **kwargs ):
  super(IndexView, self).dispatch( request,*args,**kwargs )
from django.utils.decorators import method_decorator
def login_required( func):
  def wrapper(request,*args,**kwargs ):
  if request.GET.get("username"):
  return  func(request,*args,**kwargs )
  else:
  return  redirect( reverse('login'))
  return  wrapper
@method_decorator (login_required, name='dispatch')
class IndexView( View):
  def get(self, request,*args,**kwargs ):
  return HttpResponse ("index")
  def dispatch( self, request , *args, **kwargs ):
  super(IndexView, self).dispatch( request,*args,**kwargs )
错误处理
在一些网站开发中。经常会需要捕获一些错误，然后将这些错误返回比较优美的界面，或者是将这个错
误的请求做一些日志保存。那么我们本节就来讲讲如何实现。
一、常用的错误 ：
404：服务器没有指定的url。
403：没有权限访问相关的数据。
405：请求的 method错误。
400：bad request ，请求的参数错误。
500：服务器内部错误，一般是代 出bug 了。
502：一般部署的时候见得比较多，一般是 nginx启动了，然后 uwsgi有问题。
二、自定义错误模板：
在碰到比如 404，500错误的时候，想要返回自己定义的模板。那么可以直接在 templates 文件夹下创
建相应错误代 的 html模板文件。那么以后在发生相应错误后，会将指定的模板返回回去。

三、错误处理的解决方案：
对于404和500这种自动抛出的错误。我们可以直接在 templates 文件夹下新建相应错误代 的模板文
件。而对于其他的错误，我们可以专门定义一个 app，用来处理这些错误。

分页
在Django中实现分页功能非常简单。 为 Django已经内置了两个处理分类的类。分别是 Paginator 和
Page。Paginator 用来管理整个分类的一些属性， Page用来管理当前这个分页的一些属性。通过这两
个类，就可以轻松的实现分页效果。以下对这两个类进行讲解。
一、Paginator 类：
Paginator 是用来控制整个分页的逻辑的。比如总共有多少页，页 区间等等。都可以从他上面来获
取。
1. 创建Paginator对象：
class Paginator(object_list, per_page, orphans=0, allow_empty_first_page=True) ，其中
的参数解释如下：
1. object_list ：列表，元组， QuerySet 或者是任何可以做切片操作的对象。会将这个里面的对象
进行分页。
2. per_page ：分页中，一页展示多少条数据。
3. orphans ：用来控制最后一页元 的个人如果少于 orphans 指定的个数的时候，就会将多余的添
到上一页中。
4. allow_empty_first_page ：如果object_list 没有任何数据，并且这个参数设置为 True，那么
就会抛出 EmptyPage 异常。
2. 常用属性和方法：
1. Paginator.page(number) ：获取number这页的Page对象。
2. count： 进来的 object_list 总共的数量。
3. num_pages ：总共的页数。
4. page_range ：页 的列表。比如 [1,2,3,4] 。
二、Page类：
常用属性和方法：
1. has_next() ：是否还有下一页。
2. has_previous() ：是否还有上一页。
3. next_page_number() ：下一页的页 。
4. previous_page_number() ：上一页的页 。
5. object_list ：在当前这页上的对象列表。
6. number：当前的页 。
7. paginator ：获取Paginator 对象。
表单：

一、HTML中的表单：
单纯从前端的 html来说，表单是用来提交数据给服务器的,不管后台的服务器用的是 Django还是PHP语
言还是其他语言。只要把 input 签放在 form 签中，然后再添 一个提交按钮，那么以后点击提交按
钮，就可以将 input 签中对应的值提交给服务器了。

二、Django 中的表单：
Django中的表单丰富了 统的 HTML语言中的表单。在 Django中的表单，主要做以下两件事：
1. 渲染表单模板。
2. 表单验证数据是否合法。

三、Django 中表单使用流程：
在讲解Django表单的具体每部分的细节之前。我们首先先来看下整体的使用流程。这里以一个做一个留
言板为例。首先我们在后台服务器定义一个表单类，继承自 django.forms.Form 。示例代 如下：
然后在视图中， 据是 GET还是POST请求来做相应的操作。如果是 GET请求，那么返回一个空的表单，
如果是POST请求，那么将提交上来的数据进行 验。示例代 如下：# forms.py
class MessageBoardForm( forms.Form):
  title = forms.CharField( max_length= 3,label=' 题',min_length= 2,error_messages=
{"min_length" :' 题字符段不符合要求！'})
  content  = forms.CharField( widget=forms.Textarea, label='内容')
  email = forms.EmailField( label='邮箱')
  reply = forms.BooleanField (required= False,label='回复')
# views.py
class IndexView( View):
  def get(self, request):
  form = MessageBoardForm()
  return render(request,'index.html' ,{'form' :form})
  def post(self,request):
  form = MessageBoardForm( request.POST)
  if form.is_valid():
  title = form.cleaned_data .get('title' )
  content  = form.cleaned_data .get('content')
  email = form.cleaned_data .get('email' )
  reply = form.cleaned_data .get('reply' )
  return  HttpResponse ('success')
  else:
  print( form.errors)
在使用GET请求的时候，我们 了一个 form给模板，那么以后模板就可以使用 form来生成一个表单的
html代 。在使用 POST请求的时候，我们 据前端上 上来的数据，构建一个新的表单，这个表单是
用来验证数据是否合法的，如果数据都验证通过了，那么我们可以通过 cleaned_data 来获取相应的数
据。在模板中渲染表单的 HTML代 如下：
我们在最外面给了一个 form 签，然后在里面使用了 table 签来进行美化，在使用 form对象渲染的
时候，使用的是 table的方式，当然还可以使用 ul的方式（ as_ul），也可以使用 p 签的方式
（as_p），并且在后面我们还 上了一个提交按钮。这 就可以生成一个表单了。  return  HttpResponse ('fail')
<form action="" method="post">
  <table>
  <tr>
  <td></td>
  <td><input type="submit" value="提交"></td>
  </tr>
  </table>
</form>
表单验证

一、常用的Field：
使用Field可以是对数据验证的第一步。 期望这个提交上来的数据是什么类型，那么就使用什么类型
的Field。
1. CharField：
用来接收文本。
参数：
max_length：这个字段值的最大长度。
min_length：这个字段值的最小长度。
required：这个字段是否是必须的。默认是必须的。
error_messages ：在某个条件验证失败的时候，给出错误信息。
2. EmailField：
用来接收邮件，会自动验证邮件是否合法。
错误信息的key： required 、invalid 。
3. FloatField：
用来接收浮点类型，并且如果验证通过后，会将这个字段的值转换为浮点类型。
参数：
max_value：最大的值。
min_value：最小的值。
错误信息的key： required 、invalid 、max_value 、min_value 。
4. IntegerField：
用来接收整形，并且验证通过后，会将这个字段的值转换为整形。
参数：
max_value：最大的值。
min_value：最小的值。
错误信息的key： required 、invalid 、max_value 、min_value 。
4. URLField ：
用来接收 url 式的字符串。
错误信息的key： required 、invalid 。

二、常用验证器：
在验证某个字段的时候，可以 递一个 validators 参数用来指定验证器，进一步对数据进行过滤。验证
器有很多，但是很多验证器我们其实已经通过这个 Field或者一些参数就可以指定了。比如
EmailValidator ，我们可以通过 EmailField 来指定，比如 MaxValueValidator ，我们可以通过
max_value 参数来指定。以下是一些常用的验证器：
1. MaxValueValidator ：验证最大值。
2. MinValueValidator ：验证最小值。
3. MinLengthValidator ：验证最小长度。
4. MaxLengthValidator ：验证最大长度。
5. EmailValidator ：验证是否是邮箱 式。
6. URLValidator ：验证是否是 URL 式。
7. RegexValidator ：如果还需要更 复杂的验证，那么我们可以通过正则表达式的验证器
RegexValidator 。比如现在要验证手机号 是否合 ，那么我们可以通过以下代 实现：

三、自定义验证：
有时候对一个字段验证，不是一个长度，一个正则表达式能够写清楚的，还需要一些其他复杂的逻辑，
那么我们可以对某个字段，进行自定义的验证。比如在注册的表单验证中，我们想要验证手机号 是否
已经被注册过了，那么这时候就需要在数据库中进行判断才知道。对某个字段进行自定义的验证方式
是，定义一个方法，这个方法的名字定义规则是：clean_fieldname 。如果验证失败，那么就抛出一个
验证错误。比如要验证用户表中手机号 之前是否在数据库中存在，那么可以通过以下代 实现：
以上是对某个字段进行验证，如果验证数据的时候，需要针对多个字段进行验证，那么可以重写 clean
方法。比如要在注册的时候，要判断提交的两个密 是否相等。那么可以使用以下代 来完成： class MyForm(forms.Form):
  telephone = forms.CharField( validators=
[validators. RegexValidator( "1[345678]\d{9}", message='请输入正确 式的手机号
 ！')])
class MyForm(forms.Form):
  telephone = forms.CharField( validators=
[validators. RegexValidator( "1[345678]\d{9}", message='请输入正确 式的手机号 ！')])
  def clean_telephone( self):
  telephone = self.cleaned_data .get('telephone')
  exists = User.objects.filter(telephone= telephone).exists ()
  if exists:
  raise forms.ValidationError( "手机号 已经存在！")
  return telephone

四、提取错误信息：
如果验证失败了，那么有一些错误信息是我们需要 给前端的。这时候我们可以通过以下属性来获取：
1. form.errors ：这个属性获取的错误信息是一个包含了 html 签的错误信息。
2. form.errors.get_json_data() ：这个方法获取到的是一个字典类型的错误信息。将某个字段的
名字作为 key，错误信息作为值的一个字典。
3. form.as_json() ：这个方法是将 form.get_json_data() 返回的字典 dump成json 式的字符
串，方便进行 输。
4. 上述方法获取的字段的错误值，都是一个比较复杂的数据。比如以下：
那么如果我只想把错误信息放在一个列表中，而不要再放在一个字典中。这时候我们可以定义一个方
法，把这个数据重新整理一份。实例代 如下：
这 就可以把某个字段所有的错误信息直接放在这个列表中。class MyForm(forms.Form):
  telephone = forms.CharField( validators=
[validators. RegexValidator( "1[345678]\d{9}", message='请输入正确 式的手机号 ！')])
  pwd1 = forms.CharField( max_length= 12)
  pwd2 = forms.CharField( max_length= 12)
  def clean(self):
  cleaned_data  = super().clean()
  pwd1 = cleaned_data .get('pwd1' )
  pwd2 = cleaned_data .get('pwd2' )
  if pwd1 != pwd2:
  raise forms.ValidationError( '两个密 不一致！')
{'username': [{'message': 'Enter a valid URL.', 'code' : 'invalid'}, {'message':
'Ensure this value has at most 4 characters (it has 22).' , 'code' :
'max_length' }]}
class MyForm(forms.Form):
  username = forms.URLField( max_length= 4)
  def get_errors( self):
  errors = self.errors.get_json_data()
  new_errors = {}
  for key,message_dicts in errors.items():
  messages = []
  for message in message_dicts:
  messages. append(message['message'])
  new_errors[ key] = messages
  return new_errors
ModelForm：

一、基本使用
大家在写表单的时候，会发现表单中的 Field和模型中的 Field基本上是一模一 的，而且表单中需要
验证的数据，也就是我们模型中需要保存的。那么这时候我们就可以将模型中的字段和表单中的字段进
行绑定。
比如现在有个Article 的模型。示例代 如下：
那么在写表单的时候，就不需要把 Article 模型中所有的字段都一个个重复写一遍了。示例代 如下：
MyForm是继承自 forms.ModelForm ，然后在表单中定义了一个 Meta类，在Meta类中指定了
model=Article ，以及fields="__all__" ，这 就可以将 Article 模型中所有的字段都复制过来，进
行验证。如果只想针对其中 个字段进行验证，那么可以给 fields指定一个列表，将需要的字段写进
去。比如只想验证 title和content ，那么可以使用以下代 实现：
如果要验证的字段比较多，只是除了少数 个字段不需要验证，那么可以使用 exclude 来代替
fields。比如我不想验证 category ，那么示例代 如下：
 from django.db import models
from django.core import validators
class Article(models.Model):
  title = models.CharField( max_length= 10,validators=
[validators. MinLengthValidator (limit_value= 3)])
  content  = models.TextField()
  author  = models.CharField( max_length= 100)
  category = models.CharField( max_length= 100)
  create_time = models.DateTimeField( auto_now_add =True)
from django import forms
class MyForm(forms.ModelForm):
  class Meta:
  model = Article
  fields = "__all__"
from django import forms
class MyForm(forms.ModelForm):
  class Meta:
  model = Article
  fields = ['title' ,'content']
class MyForm(forms.ModelForm):
  class Meta:
  model = Article
  exclude = ['category']
二、自定义错误消息：
使用ModelForm ， 为字段都不是在表单中定义的，而是在模型中定义的， 此一些错误消息 法在字
段中定义。那么这时候可以在 Meta类中，定义 error_messages ，然后把相应的错误消息写到里面去。
示例代 如下：

三、save方法：
ModelForm 还有save方法，可以在验证完成后直接调用 save方法，就可以将这个数据保存到数据库中
了。示例代 如下：
这个方法必须要在 clean没有问题后才能使用，如果在 clean之前使用，会抛出异常。另外，我们在调
用save方法的时候，如果 入一个 commit=False ，那么只会生成这个模型的对象，而不会把这个对象
真正的插入到数据库中。比如表单上验证的字段没有包含模型中所有的字段，这时候就可以先创建对
象，再 据填充其他字段，把所有字段的值都补充完成后，再保存到数据库中。示例代 如下：class MyForm(forms.ModelForm):
  class Meta:
  model = Article
  exclude = ['category']
  error_messages  = {
  'title' :{
  'max_length' : '最多不能超过10个字符！',
  'min_length' : '最少不能少于3个字符！'
  },
  'content': {
  'required': '必须输入content！',
  }
  }
form = MyForm(request.POST)
if form.is_valid():
  form. save()
  return  HttpResponse ('succes')
else:
  print( form.get_errors())
  return  HttpResponse ('fail')
form = MyForm(request.POST)
if form.is_valid():
  article  = form.save(commit=False)
  article .category = 'Python'
  article .save()
  return  HttpResponse ('succes')
else:
  print( form.get_errors())
  return  HttpResponse ('fail')
文件上 ：
文件上 是网站开发中非常常见的功能。这里详细讲述如何在 Django中实现文件的上 功能。

一、前端HTML代 实现：
1. 在前端中，我们需要填入一个 form 签，然后在这个 form 签中指定
enctype="multipart/form-data" ，不然就不能上 文件。
2. 在form 签中添 一个 input 签，然后指定 input 签的name，以及type="file" 。
以上两步的示例代 如下：

二、后端的代 实现：
后端的主要工作是接收文件。然后存储文件。接收文件的方式跟接收 POST的方式是一 的，只不过是通
过FILES来实现。示例代 如下：
以上代 通过 request.FILES 接收到文件后，再写入到指定的地方。这 就可以完成一个文件的上 功
能了。

三、使用模型来处理上 的文件：
在定义模型的时候，我们可以给存储文件的字段指定为 FileField ，这个Field可以 递一个
upload_to 参数，用来指定上 上来的文件保存到哪里。比如我们让他保存到项目的 files文件夹下，
那么示例代 如下：<form action="" method="post" enctype="multipart/form-data">
  <input type="file" name="myfile">
</form>
def save_file( file):
  with open('somefile.txt', 'wb') as fp:
  for chunk in file.chunks():
  fp. write(chunk)
def index( request):
  if request .method == 'GET':
  form = MyForm()
  return render(request,'index.html' ,{'form' :form})
  else:
  myfile = request.FILES.get('myfile')
  save_file( myfile)
  return HttpResponse ('success')
# models.py
class Article(models.Model):
调用完article.save() 方法，就会把文件保存到 files下面，并且会将这个文件的路径存储到数据库
中。

四、指定MEDIA_ROOT 和MEDIA_URL ：
以上我们是使用了 upload_to 来指定上 的文件的目录。我们也可以指定 MEDIA_ROOT ，就不需要在
FielField 中指定upload_to ，他会自动的将文件上 到 MEDIA_ROOT 的目录下。
然后我们可以在 urls.py 中添 MEDIA_ROOT 目录下的访问路径。示例代 如下：
如果我们同时指定 MEDIA_ROOT 和upload_to ，那么会将文件上 到 MEDIA_ROOT 下的upload_to 文件
夹中。示例代 如下：
  title = models.CharField( max_length= 100)
  content  = models.TextField()
  thumbnail = models.FileField( upload_to= "files")
# views.py
def index( request):
  if request .method == 'GET':
  return render(request,'index.html' )
  else:
  title = request.POST.get('title' )
  content = request.POST.get('content')
  thumbnail = request.FILES.get('thumbnail')
  article = Article(title=title, content =content, thumbnail= thumbnail)
  article.save()
  return HttpResponse ('success')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
from django.urls import path
from front import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
  path( '', views. index),
] + static(settings. MEDIA_URL, document_root= settings. MEDIA_ROOT)
class Article(models.Model):
  title = models.CharField( max_length= 100)
  content  = models.TextField()
  thumbnail = models.FileField( upload_to= "%Y/%m/%d/")
五、限制上 的文件拓展名：
如果想要限制上 的文件的拓展名，那么我们就需要用到表单来进行限制。我们可以使用普通的 Form表
单，也可以使用 ModelForm ，直接从模型中读取字段。示例代 如下：
六、上 图片：
上 图片跟上 普通文件是一 的。只不过是上 图片的时候 Django会判断上 的文件是否是图片的
式（除了判断后缀名，还会判断是否是可用的图片）。如果不是，那么就会验证失败。我们首先先来定
义一个包含 ImageField 的模型。示例代 如下：
 为要验证是否是合 的图片， 此我们还需要用一个表单来进行验证。表单我们直接就使用
ModelForm 就可以了。示例代 如下：
注意：使用ImageField，必须要先安装Pillow库：pip install pillow# models.py
class Article(models.Model):
  title = models.CharField( max_length= 100)
  content  = models.TextField()
  thumbnial = models.FileField( upload_to= '%Y/%m/%d/', validators=
[validators. FileExtensionValidator(['txt', 'pdf'])])
# forms.py
class ArticleForm( forms.ModelForm):
  class Meta:
  model = Article
  fields = "__all__"
class Article(models.Model):
  title = models.CharField( max_length= 100)
  content  = models.TextField()
  thumbnail = models.ImageField( upload_to= "%Y/%m/%d/")
class MyForm(forms.ModelForm):
  class Meta:
  model = Article
  fields = "__all__"
cookie和session
一、Cookie 介绍
1. cookie：在网站中，http请求是 状态的。也就是说即使第一次和服务器连接后并且登录成功后，
第二次请求服务器依然不能知道当前请求是哪个用户。 cookie的出现就是为了解决这个问题，第
一次登录后服务器返回一些数据（cookie）给浏览器，然后浏览器保存在本地，当该用户发送第二
次请求的时候，就会自动的把上次请求存储的 cookie数据自动的携带给服务器，服务器通过浏览
器携带的数据就能判断当前用户是哪个了。 cookie存储的数据量有限，不同的浏览器有不同的存
储大小，但一般不超过4KB 。 此使用 cookie只能存储一些小量的数据。
2. session: session和cookie的作用有点类似，都是为了存储用户相关的信息。不同的是， cookie是
存储在本地浏览器， session 是一个思路、一个概念、一个服务器存储授权信息的解决方案，不同
的服务器，不同的框架，不同的语言有不同的实现。虽然实现不一 ，但是他们的目的都是服务器
为了方便存储数据的。session 的出现，是为了解决 cookie存储数据不安全的问题的。
3. cookie和session使用： web开发发展至今， cookie和session 的使用已经出现了一些非常成熟的
方案。在如今的市场或者企业里，一般有两种存储方式：
存储在服务端：通过 cookie存储一个 sessionid ，然后具体的数据则是保存在 session
中。如果用户已经登录，则服务器会在 cookie中保存一个 sessionid ，下次再次请求的时
候，会把该 sessionid 携带上来，服务器 据 sessionid 在session 库中获取用户的
session 数据。就能知道该用户到底是谁，以及之前保存的一些状态信息。这种专业术语叫做
server side session 。Django把session 信息默认存储到数据库中，当然也可以存储到
其他地方，比如缓存中，文件系统中等。存储在服务器的数据会更 的安全，不容易被窃取。
但存储在服务器也有一定的弊端，就是会 用服务器的资源，但现在服务器已经发展至今，一
些session 信息还是绰绰有余的。
将session 数据 密，然后存储在 cookie中。这种专业术语叫做 client side session 。
flask框架默认采用的就是这种方式，但是也可以替换成其他形式。

二、在django中操作cookie
1.  设置cookie ：
设置cookie是设置值给浏览器的。 此我们需要通过 response 的对象来设置，设置 cookie可以通过
response.set_cookie 来设置，这个方法的相关参数如下：
1. key：这个cookie的key。
2. value：这个cookie的value。
3. max_age ：最长的生命周期。单位是秒。
4. expires ：过期时间。跟 max_age 是类似的，只不过这个参数需要 递一个具体的日期，比如
datetime 或者是符合日期 式的字符串。如果同时设置了 expires 和max_age ，那么将会使用
expires 的值作为过期时间。
5. path：对域名下哪个路径有效。默认是对域名下所有路径都有效。
6. domain：针对哪个域名有效。默认是针对主域名下都有效，如果只要针对某个子域名才有效，那
么可以设置这个属性.
7. secure：是否是安全的，如果设置为 True，那么只能在 https协议下才可用。
8. httponly ：默认是 False。如果为 True，那么在客户端不能通过 JavaScript 进行操作。
2.  除cookie：
通过delete_cookie 即可 除 cookie。实际上 除 cookie就是将指定的 cookie的值设置为空的字符
串，然后使用将他的过期时间设置为 0，也就是浏览器关闭后就过期。
3. 获取cookie：
获取浏览器发送过来的 cookie信息。可以通过 request.COOKIES 来或者。这个对象是一个字典类型。
比如获取所有的 cookie，那么示例代 如下：

三、在Django 中操作session ：
django中的session 默认情况下是存储在服务器的数据库中的，在表中会 据 sessionid 来提取指定
的session 数据，然后再把这个 sessionid 放到cookie中发送给浏览器存储，浏览器下次在向服务器
发送请求的时候会自动的把所有 cookie信息都发送给服务器，服务器再从 cookie中获取sessionid ，
然后再从数据库中获取 session 数据。但是我们在操作 session 的时候，这些细节压 就不用管。我们
只需要通过 request.session 即可操作。示例代 如下：
session 常用的方法如下：
1. get：用来从 session 中获取指定值。
2. pop：从session 中 除一个值。
3. keys：从session 中获取所有的键。
4. items：从session 中获取所有的值。
5. clear：清除当前这个用户的 session 数据。
6. flush： 除session 并且 除在浏览器中存储的 session_id ，一般在注销的时候用得比较多。
7. set_expiry(value) ：设置过期时间。
整形：代表秒数，表示多少秒后过期。
0：代表只要浏览器关闭， session 就会过期。
None：会使用全局的 session 配置。在 settings.py 中可以设置 SESSION_COOKIE_AGE 来
配置全局的过期时间。默认是 1209600 秒，也就是2周的时间。
8. clear_expired ：清除过期的 session 。Django并不会清除过期的 session ，需要定期手动的
清理，或者是在终端，使用命令行 python manage.py clearsessions 来清除过期的 session 。
 cookies = request.COOKIES
for cookie_key, cookie_value  in cookies.items():
  print( cookie_key, cookie_value )
def index( request):
  request .session.get('username')
  return  HttpResponse ('index')
四、修改session 的存储机制：
默认情况下， session 数据是存储到数据库中的。当然也可以将 session 数据存储到其他地方。可以通
过设置SESSION_ENGINE 来更改session 的存储位置，这个可以配置为以下 种方案：
1. django.contrib.sessions.backends.db ：使用数据库。默认就是这种方案。
2. django.contrib.sessions.backends.file ：使用文件来存储session。
3. django.contrib.sessions.backends.cache ：使用缓存来存储session。想要将数据存储到缓存
中，前提是 必须要在 settings.py 中配置好 CACHES，并且是需要使用 Memcached ，而不能使用
纯内存作为缓存。
4. django.contrib.sessions.backends.cached_db ：在存储数据的时候，会将数据先存到缓存
中，再存到数据库中。这 就可以保证万一缓存系统出现问题，session数据也不会丢失。在获取数
据的时候，会先从缓存中获取，如果缓存中没有，那么就会从数据库中获取。
5. django.contrib.sessions.backends.signed_cookies ：将session 信息 密后存储到浏览器
的cookie中。这种方式要注意安全，建议设置 SESSION_COOKIE_HTTPONLY=True ，那么在浏览器
中不能通过 js来操作session 数据，并且还需要对 settings.py 中的SECRET_KEY 进行保密，
为一旦别人知道这个 SECRET_KEY ，那么就可以进行解密。另外还有就是在 cookie中，存储的数据
不能超过 4k。