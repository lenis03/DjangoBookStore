# Bookstore Project

This is a bookstore web application built with Python and Django. It allows users to view, edit, and add books to their collection. User authentication is implemented using Django Allauth, which includes email verification.

## Features

- User authentication with email verification (Django Allauth).
- CRUD functionality for books:
  - Create, Read, Update, Delete books.
- Admin interface for book management
- (Class-Based Views).

## Technologies Used

- Python 3.x
- Django 3.x
- Django Allauth
- HTML/CSS (Bootstrap for styling)

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system.
- Pip package manager.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/lenis03/DjangoBookStore.git
cd bookstore
```
Create a virtual environment:

```bash
python -m venv env
```
Activate the virtual environment:
On Windows:

```bash
.\env\Scripts\activate
```
On macOS/Linux:
```bash
source env/bin/activate
Install dependencies:
```

```bash
pip install -r requirements.txt
```
Apply migrations:

```bash
python manage.py migrate
Create a superuser (admin):
```

```bash
python manage.py createsuperuser
```
Start the development server:
```bash
python manage.py runserver
```
Open your web browser and go to http://127.0.0.1:8000/ to view the application.

## Usage
Navigate to http://127.0.0.1:8000/ to access the bookstore application.
Use the admin interface at http://127.0.0.1:8000/admin/ to manage books and users (requires admin credentials).
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

