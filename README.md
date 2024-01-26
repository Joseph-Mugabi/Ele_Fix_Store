![](https://github.com/Joseph-Mugabi/Ele_Fix_Store/blob/master/web_flask/static/images/logooo.PNG?raw=true)

* **The primary role of the Electronic Emporium E-Shop project is to serve as an online platform 
for the retail of electronics and electrical products. The project aims to provide users 
with a seamless and enjoyable shopping experience while offering a diverse range of high-quality 
electronic and electrical items. The e-shop serves as a virtual storefront where customers can 
browse through products, obtain detailed information, make secure transactions, and have their 
chosen items delivered to their preferred locations.```client```.**
```
 Ele_fix_store is a dynamic and user-centric e-commerce platform designed to cater to the 
 diverse needs of consumers seeking high-quality electronics and electrical products. 
 The platform is crafted with a focus on seamless user experience, modern design aesthetics, and robust functionality
**it plays an important role in the performance and reliability online shopping system.**
```


* 🖥️ Checkout on my landing_page @ [<span style="color: blue;">Ele_Fix_Store</span>](http://www.jinsights.tech/landing_page.html)  
* ⚡ Author: **Mugabi Joseph**, Backend Engineer, Kampala Uganda | [![Linkedin](https://img.shields.io/badge/LinkedIn-+22K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/mugabijoseph)
* ⚡ Contact: [Joseph Mugabi](https://twitter.com/joseph_mugabi) | mugabijoshgreen@gmail.com
---
## Usage
* **python3 -m api.v1.app**
```
josephgreen@JosephGreen-Mugabi:~/Ele_Fix_Store$ python3 -m api.v1.app
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5001
 * Running on http://172.20.233.199:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 155-833-322
http://172.20.233.199:5001172.20.224.1 - - [26/Jan/2024 02:52:25] "GET /api/v1/customers HTTP/1.1" 200 -
172.20.224.1 - - [26/Jan/2024 02:52:25] "GET /favicon.ico HTTP/1.1" 404 -
```

mysql> select * from users;
+---------------------------+----------------------------------+------------+-----------+----------------+---------------+--------------------------------------+---------------------+---------------------+
| email                     | password                         | first_name | last_name | location       | contact       | id                                   | created_at          | updated_at          |
+---------------------------+----------------------------------+------------+-----------+----------------+---------------+--------------------------------------+---------------------+---------------------+
| mugabijoshgreen@gmail.com | 827ccb0eea8a706c4c34a16891f84e7b | Joseph     | Mugabi    | NULL           | +256788422721 | 0a422ab7-da9e-4405-869d-78d6f0c34e64 | 2023-06-03 11:27:51 | 2023-06-03 11:27:51 |
| lourdel@gmail.com         | 3d0c1f4b3f42eea59f1ad447a6a4b254 | Engineer   | lourdel   | Kampala-Uganda | +256750852947 | 7a6cce58-75ec-482f-9df0-b1bd4597c2b6 | 2023-06-03 14:54:21 | 2023-06-03 14:54:21 |
| gui@hbtn.io               | f4ce007d8e84e0910fbdd7a06fa1692d | paul       | Joel      | katabi         | +25678842722  | b6b90f81-8511-472b-af44-b7ad97b9cd91 | 2023-06-09 10:56:11 | 2023-06-09 18:00:54 |
+---------------------------+----------------------------------+------------+-----------+----------------+---------------+--------------------------------------+---------------------+---------------------+
3 rows in set (0.00 sec)
```
---
## Technology And Architecture
**MYSQL and JSON** for Databases, a layer of abstraction in SQLAlchemy, internal APIs to expose the databases to other APIs to be served
interface content from the client[FrontEnd]. The Storage engine without a schema is nothing less than storage engine, so i came with a 
schema and did the mapping of all data in SQLAlchemy. Since i needed a data layer of abstraction to that would handle a certain information
or data to make it easy for the ```client(FrontEnd)``` to access the data storage engine.

[www.jinsights.tech](www.jinsights.tech/landing_page.html)
[linkedin](https://www.linkedin.com/pulse/am-happy-honored-share-you-my-complete-foundation-portfolio-joseph)
[twitter](https://twitter.com/joseph_mugabi/status/1668571291639590913?s=20)