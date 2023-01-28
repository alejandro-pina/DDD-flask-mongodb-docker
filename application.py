import os
import click
from app import create_app

print(' 🟡 Starting aplication...')
print(' 🟡',os.getenv('FLASK_CONFIG'))
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

def user_admin():
    from app.api.user.infractucture.controllers._init_db_user__controller import InitDBController
    from app.api.user.infractucture.dtos.register_user__dto import CreateUserDTO

    name     = str(os.environ.get('APP_USER_ADMIN')) if os.environ.get('APP_USER_ADMIN') else 'admin'
    email    = str(os.environ.get('APP_USER_EMAIL')) if os.environ.get('APP_USER_EMAIL') else 'admin@admin.com'
    password = str(os.environ.get('APP_PASS')) if os.environ.get('APP_PASS') else 'admin123456789'

    admin_user = CreateUserDTO(
        name     = name, 
        email    = email, 
        password = password
    )

    InitDBController(admin_user).execute()

@app.cli.command()
def deploy():
    """Run deployment tasks."""
    print(' 🟢 aplication ready.')
    user_admin()
    

@app.cli.command()
def dev():
    """Run dev tasks."""
    print(' 🟢 DEV aplication ready.')
    user_admin()

@app.cli.command()
def itests():
    """Run the unit tests."""
    print('  🧪 TEST with aplication ready.')

    import unittest
    """Is best job with localhost"""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

