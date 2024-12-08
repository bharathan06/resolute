# Variables
PYTHON = python  # Or the specific Python version you're using
MANAGE = $(PYTHON) manage.py

# Run the development server
run:
	$(MANAGE) runserver

# Apply migrations
migrate:
	$(MANAGE) migrate

# Make migrations
mm:
	$(MANAGE) makemigrations

# Collect static files
collectstatic:
	$(MANAGE) collectstatic --noinput

# Run tests
test:
	$(MANAGE) test

# Create a superuser
createsuperuser:
	$(MANAGE) csu

# Install dependencies
install:
	pip install -r requirements.txt
