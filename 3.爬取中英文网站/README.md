## 中英文网站文章爬取

#### 一、概述

​	该程序主要是爬取http://www.kekenet.com网站的文章。文章分别有中英两种语言，程序能够自动按顺序爬取每篇文章数据并且将中英文文本存入MySQL数据库中。程序是在Python2.7.13版本下开发，数据库版本是MySql5.7。

**程序运行如下图所示：**

![运行效果](https://github.com/kaishuibaicai/mini-Python-Projects/blob/master/3.%E7%88%AC%E5%8F%96%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BD%91%E7%AB%99/img/%E8%BF%90%E8%A1%8C%E6%95%88%E6%9E%9C.JPG?raw=true)

**保存到数据库中的数据：**

![数据效果](https://github.com/kaishuibaicai/mini-Python-Projects/blob/master/3.%E7%88%AC%E5%8F%96%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BD%91%E7%AB%99/img/%E6%95%B0%E6%8D%AE%E6%95%88%E6%9E%9C.JPG?raw=true)

**英文文本：**

![英文文本](https://github.com/kaishuibaicai/mini-Python-Projects/blob/master/3.%E7%88%AC%E5%8F%96%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BD%91%E7%AB%99/img/%E8%8B%B1%E6%96%87%E6%95%B0%E6%8D%AE%E6%95%88%E6%9E%9C.JPG?raw=true)

**中文文本：**

![中文文本](https://github.com/kaishuibaicai/mini-Python-Projects/blob/master/3.%E7%88%AC%E5%8F%96%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BD%91%E7%AB%99/img/%E4%B8%AD%E6%96%87%E6%95%B0%E6%8D%AE%E6%95%88%E6%9E%9C.JPG?raw=true)



#### 二、运行说明

1. 首先在cmd中登录MySql时输入，创建`zn-enpost`数据库。
2. 运行`CreateTable.py`文件来创建`znenpost`