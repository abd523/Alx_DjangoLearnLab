# 📝 Django Blog

A simple and clean blogging platform built with **Django**.  
Users can create, edit, and delete blog posts, as well as view posts from others.  
This project is great for learning Django fundamentals such as models, views, templates, and authentication.

---

## 🚀 Features

- ✍️ Create, edit, and delete blog posts  
- 🔐 User authentication (login, register, logout)  
- 🗂️ Categorize and filter posts  
- 💬 Comment section for posts  
- 🧑‍💻 Admin dashboard to manage content  
- 📱 Responsive design with Bootstrap

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default)
- **Version Control:** Git & GitHub

---

## ⚙️ Installation

Follow these steps to run the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/django-blog.git

# 2. Navigate to the project folder
cd django-blog

# 3. Create a virtual environment
python -m venv venv

# 4. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Run database migrations
python manage.py migrate

# 7. Create a superuser (for admin access)
python manage.py createsuperuser

# 8. Start the development server
python manage.py runserver
