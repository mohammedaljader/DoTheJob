# DoTheJob
DoTheJob website helps teams get work done faster.  Collaborate, manage projects and increase your productivity. It's possible with DoTheJob website.
![image](https://user-images.githubusercontent.com/78910660/160812073-316f6292-c18b-4e2d-bd81-03124590ccba.png)


# Installation
## Frontend 
- **cd** into **/frontend**
- run **npm install** to grab the necessary dependencies 
- run **npm start** to start the server

## Database 
- Install MySql
- Create a database called **"trello"**
- Create two tables called **"card" and "task"**
- **"card"** table has **"card_id", "card_title"** (**"card_id"** is auto increment primary key)
- **"task"** table has **"task_id", "task_title", "task_completed", "card_id"** (**"task_id"** is auto increment primary key and **"card_id"** is a foreign key references to the primary key of **"card"** table **"card_id"**)

## Backend 
- **cd** into **/Backend**
- install the following dependencies **"pip install fastapi uvicorn"** and **"pip install sqlalchemy"**
- Then, run the server with the command **"uvicorn main:app --reload"**

# Technologies Used
### **Front-end / Client Side tools:**
-  **HTML5** 
-  **CSS3**
-  **JavaScript** 
-  **React.js** - progressive JavaScript framework for building user interfaces.

### **Back-end / Server Side tools:**
-  **Python**
-  **FastAPI**
-  **MySQL**

### Database diagram of the project 
![image](https://user-images.githubusercontent.com/78910660/160811169-22d2a5d4-ab50-440c-b6a0-30c25473d75c.png)

# Tests
### Integration Tests using Newman and Postman
![image](https://user-images.githubusercontent.com/78910660/160815953-27e2cf95-641d-40a0-ba77-43ea61d69099.png)
![image](https://user-images.githubusercontent.com/78910660/160815991-9c452348-f473-425b-a4eb-63d2044eefb8.png)
![image](https://user-images.githubusercontent.com/78910660/160816035-96c0f47b-ca6b-4cd7-8864-7a11c909e2ed.png)

