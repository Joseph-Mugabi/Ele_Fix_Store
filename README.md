![The logo](landing_page/images/screen-shot.PNG)

* **The primary objective of a data storage engine is to efficiently and effectively store,
manage, and retrieve data in a way that meets the needs of the application or system that
it supports ```client```.**
```
Data Storage Engine is a software componant that is responsible for managing the Storage and Retrieval of Data on the Database system.
It's the core componant of a database management system and is responsible for providing efficient and reliable access to data on stored 
on the storage engine. DataStorageEngine is designed to handle all aspects of data storage, such as data organisation, indexing, 
caching and Retrieval. it provides a layer of abstraction  between the application and the phyical storage device, allowing 
applications to interact with the data in a consistent and controlled way. And  the storage engine manages data in the form 
of JSON strings and tables, which are organised into the databases. 
**it plays an important role in the performance and reliability of a database system.**
```

## Users
![User](landing_page/images/sel.frm.tbl.users.PNG)

* 🖥️ Checkout on my landing_page @ [<span style="color: blue;">DataStorageEngine</span>](http://www.jinsights.tech/landing_page.html)  
* ⚡ Author: **Mugabi Joseph**, Backend Engineer, Kampala Uganda | [![Linkedin](https://img.shields.io/badge/LinkedIn-+22K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/mugabijoseph)
* ⚡ peer: **Mubarak Wantimba**, Backend Engineer, Kampala Uganda | [![Linkedin](https://img.shields.io/badge/LinkedIn-+22K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/mubarak-wantimba-3025a820a/)
* ⚡ peer:  **Melvin Renish Okago**, FrontEnd Engineer, Nairobi Kenya | [![Linkedin](https://img.shields.io/badge/LinkedIn-+22K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/fabrizia-renish-993498246/)
* ⚡ Contact: [Joseph Mugabi](https://twitter.com/joseph_mugabi) | mugabijoshgreen@gmail.com
---
## Usage
* **python3 -m api.v1.app**
```
josephgreen@JosephGreen-Mugabi:~/Data_Storage_EngineV1$ python3 -m api.v1.app
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5001
 * Running on http://172.25.51.70:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 477-478-267
127.0.0.1 - - [12/Jun/2023 10:02:42] "GET /api/v1/users HTTP/1.1" 200 -
127.0.0.1 - - [12/Jun/2023 10:03:18] "GET /api/v1/users/6697e340-5b28-45ad-b426-25cb30d53907 HTTP/1.1" 200 -
127.0.0.1 - - [12/Jun/2023 10:04:12] "PUT /api/v1/users/6697e340-5b28-45ad-b426-25cb30d53907 HTTP/1.1" 200 -
127.0.0.1 - - [12/Jun/2023 10:04:22] "GET /api/v1/users/6697e340-5b28-45ad-b426-25cb30d53907 HTTP/1.1" 200 -
```
* **curl -X GET http://0.0.0.0:5001/api/v1/users**
```
[
  {
    "__class__": "User",
    "contact": "91788422721",
    "created_at": "2023-04-13T13:24:54.015073",
    "email": "datastorageengine2@mail.com",
    "first_name": "John",
    "id": "55c664ea-1029-4a72-8a49-b40136e49051",
    "last_name": "Tubone",
    "location": "'San",
    "password": "********************************",
    "updated_at": "2023-06-03T13:50:25.275503"
  },
  {
    "__class__": "User",
    "contact": "0788422721",
    "created_at": "2023-06-03T07:48:13.413799",
    "email": "mugabijoshgreen@gmail.com",
    "first_name": "Joseph",
    "id": "c48c778e-c0c9-4676-b6a7-b1c87eb9734d",
    "last_name": "mugabi",
    "location": "Entebbe - Kampala Uganda",
    "password": "********************************",
    "updated_at": "2023-06-03T13:00:48.673175"
  }
]
```
*  **echo 'create User email="panda@gmail.com" password="were" last_name="were"' | DSE_USER=data_stor_eng_dev DSE_PWD=pwd 
DSE_HOST=localhost DSE_DB=data_stor_eng_dev_db DSE_TYPE_STORAGE=db ./console.py**
```
[[User] (7a6cce58-75ec-482f-9df0-b1bd4597c2b6) {'email': 'lourdel@gmail.com', 'last_name': 'lourdel', 'contact': '+256750852947',
 'created_at': '2023-06-03T14:54:21.000000', 'updated_at': '2023-06-03T14:54:21.000000', 'first_name': 'Engineer', 'location': 
 'Kampala-Uganda', 'id': '7a6cce58-75ec-482f-9df0-b1bd4597c2b6', '__class__': 'User'}, [User] (b6b90f81-8511-472b-af44-b7ad97b9cd91) 
 {'email': 'gui@hbtn.io', 'last_name': 'Joel', 'contact': '+25678842722', 'created_at': '2023-06-09T10:56:11.000000', 'updated_at': 
 '2023-06-09T18:00:54.000000', 'first_name': 'paul', 'location': 'katabi', 'id': 'b6b90f81-8511-472b-af44-b7ad97b9cd91', '__class__': 'User'}]
 ```
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