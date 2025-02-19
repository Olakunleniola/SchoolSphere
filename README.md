# SchoolSphere
SchoolSphere is a multi-tenant school management application designed for schools to register, generate a unique subdomain, and manage their own dashboard. The landing page (for school registration) is built with Django templates, while each school's dashboard can embed a React application for rich interactivity.

## Features
* School Registration:
    Schools register on the main landing page, which automatically creates a unique slug and subdomain (e.g., binta-schools.lvh.me for local testing) and an admin user.

* Multi-Tenant Architecture:
    Each school accesses its own dashboard via its subdomain, enabling separate contexts for school-specific data.

* Custom User Model:
    A custom user model supports various roles (student, admin, teacher, parent) for flexible user management.

* Dashboard Powered by React:
    The dashboard is designed to embed a React application for dynamic functionality.


## Setup Instructions
### Prerequisites
* Python 3.8+
* Pipenv (or another virtual environment tool)
* Node.js and npm (for building the React frontend)

### Installation
* Clone the repository:
    ```bash
    git clone <repository_url>
    cd SCHOOLSPHERE
    ```

* Set up the Python environment:
    ```bash
    pipenv install
    pipenv shell
    ```

* Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

* Create a superuser (if needed):
    ```bash
    python manage.py createsuperuser
    ```

### Running the Django Server
For local development, start the Django server:
```bash
python manage.py runserver
```

**Testing Subdomains Locally:**
* Use a domain like lvh.me which always resolves to 127.0.0.1.
* For example:
    * Main site: http://www.lvh.me:8000
    * School dashboard: http://binta-schools.lvh.me:8000

Make sure your ALLOWED_HOSTS in settings.py includes .lvh.me (e.g., ALLOWED_HOSTS = ['.lvh.me', '127.0.0.1']).

### Building the React Dashboard
1. Navigate to the frontend folder:
    ```bash
    cd frontend
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Run the React development server (optional for development):
    ```bash
    npm start
    ```

4. For production, build the React app:
    ```bash
    npm run build
    ```

    Then, configure Django to serve the build artifacts (e.g., copy the build files into the static/ folder).

### Configuration Details
* Custom User Model:
    Defined in the apps/user (or apps/accounts) app and registered via AUTH_USER_MODEL in schoolsphere/settings.py.

* Subdomain Routing:
    Configured using django-hosts in schoolsphere/hosts.py and custom middleware in middleware/subdomain.py.

* Templates & Static Files:
    Global templates are stored in schoolsphere/templates/, and app-specific templates reside within each app’s templates/ folder.

### Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

### License
This project is licensed under the MIT [License](https://).