# <img src="https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white"></img> <img src="https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white"></img> <img src="https://img.shields.io/badge/JAVASCRIPT-239120?style=for-the-badge&logo=javascript&logoColor=white"></img> ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)


# Libraria

Libraria is an Online Library that helps users to borrow books at ease with the digitalization of the library management system. 

### Preview
![Untitled design](https://github.com/Satyam0204/Online-Library-Management-System/assets/97899114/1e5acf25-ed56-4026-a9e5-82d3683ce096)


## Features:
- An optimized Search Functionality with real-time suggestions from the backend.
- A  proper filtration system to browse through books efficiently.
- Users can give feedback to the books in form of reviews and upvotes/downvotes
- A custom admin side for managing books, issuals, and handle queries. Also, a super moderator can add or remove more users to the admin role.
- users can request any book if it is out of stock.


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
