import setuptools

dependencies = [
    "blinker==1.8.2",
    "click==8.1.7",
    "Flask==3.0.3",
    "Flask-SQLAlchemy==3.1.1",
    "greenlet==3.0.3",
    "gunicorn==22.0.0",
    "itsdangerous==2.2.0",
    "Jinja2==3.1.4",
    "MarkupSafe==2.1.5",
    "packaging==24.1",
    "psycopg2-binary==2.9.9",
    "SQLAlchemy==2.0.31",
    "typing_extensions==4.12.2",
    "Werkzeug==3.0.3"
]

try:
    pkg_resources.require(dependencies)
    print("No conflicts found.")
except pkg_resources.VersionConflict as e:
    print(f"Conflict found: {e}")
except pkg_resources.DistributionNotFound as e:
    print(f"Distribution not found: {e}")