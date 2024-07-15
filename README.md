# E – commerce webapp Created Using [Python – Django Framework] 


## Features:

- [x] product preview
- [x] user can create account 
- [x] product add to cart 
- [x] edit cart
- [x] order updates 
- [x] product description view 

## Administrator Can
1. Add products, product details
2. Editable Oderstatus 
3. Search product 
4. Manage Candidates (CRUD)


## User Can
1. Register
2. Login
3. Order product
4. View product details 
5. View order status 
5. View cart details 




### Pre-Requisites:
1.	Install Git Version Control
[ https://git-scm.com/ ]

2.	Install Python Latest Version
[ https://www.python.org/downloads/ ]

Creator environment is: cartz

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```
For Linux
```
$  virtualenv .
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```

For Linux
```
$  source bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/karnnan1947/cart.git
```

Then, Enter the project
```
$  cd kcart
```

**4. Install Requirements from ‘requirements.txt’**
```python
$  pip3 install -r requirements.txt
```

**5. Run migrations**
```python 
$  python manage.py makemigrations
```

**5.1 and Migrate**
```python 
$  python manage.py migrate
```

**6. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

Command for Linux:
```python
$ python3 manage.py runserver
```

**7. Login Credentials**

Create Super User 
Command for PC:
```
$  python manage.py createsuperuser
```

Command for Mac:
```
$  python3 manage.py createsuperuser
```

Command for Linux:
```
$  python3 manage.py createsuperuser
```


## Open to contribution ?
Yeah. Pull requests are welcomed.

## Having any issue using this ?
Please, let us know. Open up an issue.
