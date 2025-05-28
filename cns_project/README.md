# **CNS Project**

This project implements Caesar Cipher encryption/decryption, and Vigenère Cipher encryption/decryption tool using Django. The tool allows users to input text through a web interface, and display the output to the users.

## **Project Structure**
    db.sqlite3
    manage.py
    README.md
    cipher_app/
        admin.py
        apps.py
        models.py
        tests.py
        urls.py
        views.py
        __init__.py
        migrations/
            __init__.py
    cns_project/
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py
    static/
        script.js
        style.css
        styles.css
        Wonderhoy.jpg
    templates/
        caesar.html
        homepage.html
        vigenere.html

## **Setup**
#### 1. Extract the project files to your preferred location
#### 2. Set up a virtual environment
```
python -m venv venv
```
#### 3. Activate the virtual environment
- On Windows:
```
venv\Scripts\activate
```
- On macOS/Linux:
```
source venv/bin/activate
```
#### 4. Install dependencies
```
pip install django
```
#### 5. Run development server
```
python manage.py runserver
```
#### 6. Access the application
Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Implementation

### Key Files
- `views.py`: contains logic for the cipher implementations
- `urls.py`: defines applications routes



sorry guys i know the code is hard to read TT