# technoland store

This project is a simple e-commerce store built with Django, featuring product management, shopping cart functionality, and order processing.

<a href="https://technoland.liara.run " >technoland</a>
## Features

- **User Authentication**: User registration, login, and profile management.
- **Product Management**: Add, update, delete, and view products with descriptions, prices, and categories.
- **Shopping Cart**: Add items to cart, adjust quantities, and remove items.
- **Order Processing**: Place orders and manage order status.
- **Admin Panel**: Manage products, orders, and users through Django’s built-in admin panel.
- **Responsive Design**: Mobile-friendly layout.
- **Merchant ID**: Set your Merchant ID in **settings.py**.


## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default), easily switchable to PostgreSQL, MySQL, etc.
- **Deployment**: Docker, Gunicorn, Nginx (optional)

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes. 



### Installation Steps
```bash
git clone [https://github.com/Mohammadparsa1384/technoland-store.git]
cd technoland
```
### Create venv
```bash
python -m venv venv
`venv\Scripts\activate`
```
### Install requirements and start project
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
   
