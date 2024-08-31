import os

# Set the root directory of your Django project
project_dir = 'E:/srikanth/Django/DRF/elastic_search/myproject'

# Walk through all directories and remove migration files
for root, dirs, files in os.walk(project_dir):
    if 'migrations' in dirs:
        migrations_dir = os.path.join(root, 'migrations')
        for file in os.listdir(migrations_dir):
            if file.endswith('.py') and file != '__init__.py':
                os.remove(os.path.join(migrations_dir, file))

print("Migration files removed.")
