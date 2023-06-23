# <img src="https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white"></img> <img src="https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white"></img> <img src="https://img.shields.io/badge/JAVASCRIPT-239120?style=for-the-badge&logo=javascript&logoColor=white"></img> ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)


# Libraria

Libraria is an Online Library which helps users to borrow books at ease with digitalization of the library manangement system. 


## Features:
- An optimized Search Functionality with realtime suggestions from backend.
- A  proper filtraion system to browse through books efficiently.
- Users can give feedback to the books in form of reviews and upvotes/downvotes
- A custom admin side for to manage books, issuals and handle querries. Also a supermoderator can add or remove more users to admin role.
- users can request for any book if it is out of stock.


## Run Locally

Clone the project

```bash
  git clone https://github.com/Satyam0204/Online-Library-Management-System.git
```

Go to the project directory

```bash
  cd Online-Library-Management-System/django/mysite/
```
Setup virtual environment
 
```
    python3 -m venv env
    source env/bin/activate
```

Install dependencies

```bash
   pip install -r requirements.txt
```

Configure Database 

```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
```

Start server
```
python3 manage.py runserver 
```


## Authors:
 [Satyam0204](https://www.github.com/Satyam0204)