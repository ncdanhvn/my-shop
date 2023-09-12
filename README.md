# My Shop - Django Online Store API

"My Shop" is a Django-based online store project that provides a set of RESTful APIs for managing products, collections, customers, carts, orders, and tags. This project is designed to serve as a foundation for building a robust e-commerce platform.

## Functions

- **Product Management**: Create, retrieve, update, and delete product listings.
- **Customer Accounts**: Manage customer accounts, including registration and authentication.
- **Shopping Cart**: Allow customers to add and remove products from their shopping carts.
- **Order Management**: Process and track customer orders.
- **Tagging and Collection System**: Categorize products with tags and collections for easier browsing.

## Features

- **Microservice Architecture**: The project is structured with microservices in mind. 'shop' and 'tag' apps are designed to be reusable in other projects.

- **Integration Tests**: Comprehensive integration tests are in place to ensure the correct behavior of API endpoints.

- **Authentication and Security**: API endpoints are secured with authentication to protect sensitive data and restrict access. User authentication and authorization are implemented to ensure data privacy.

- **Background Services & Caching**: Included example implementation for background scheduled periodic service and caching

- **Admin Panel**: An intuitive admin panel is provided for easy management of products, customers, collections, tags...

## Technologies Used

- **Django**: The backend framework for building the APIs.
- **Django REST framework**: For creating RESTful APIs with Django.
- **MySQL**: The default database used for development.
- **Other Python libraries**: django-debug-toolbar, drf-nested-routers, django-redis, celery, pytest

## Getting Started

- Unfortunately by utilizing Celery library, this repository is only avaiable to run from **Linux** or **Mac** environment. If you are on **Windows**, please using **WSL**

- **Config the database**. You will need an MySQL server up and running. Configure database with root username and password in **`myshop > settings.py > DATABASES`**  
Open mysql shell and run create database command

    ```MySQL
    CREATE DATABASE myshop;
    ```

- You also need an Redis instance running.

- Make sure you have `python` and `pipenv` installed on your machine

- Steps:
  - Clone the repository:

    ```bash
    git clone https://github.com/ncdanhvn/myshop.git
    cd my-shop
    ```

  - Install the dependencies and activate virtual environment:

    ```bash
    pipenv install
    pipenv shell
    ```

  - Run migrations and populate database with dummy data

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py seed_db
    ```

  - Run server:
  
    ```bash
    python3 manage.py runserver
    ```
