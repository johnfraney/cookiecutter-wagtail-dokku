# {{cookiecutter.project_name}}

{{cookiecutter.description}}

![Made with Cookiecutter Wagtail Dokku](https://img.shields.io/badge/built%20with-Cookiecutter%20Wagtail%20Dokku-ff69b4.svg)

{% if cookiecutter.open_source_license != "Not open source" %}

License: {{cookiecutter.open_source_license}}
{% endif %}


## Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report::

```
coverage run manage.py test
coverage html
open htmlcov/index.html
```


## Running tests with py.test

```
$ pytest
```


## Deployment

The following details how to deploy this application.

### Configure Dokku on the server
```
dokku apps:create {{cookiecutter.project_slug}}

# Install Postgres
dokku plugin:install https://github.com/dokku/dokku-postgres.git postgres
dokku postgres:create {{cookiecutter.project_slug}}_db
dokku postgres:link {{cookiecutter.project_slug}}_db {{cookiecutter.project_slug}}


# Install Redis
dokku plugin:install https://github.com/dokku/dokku-redis.git redis
dokku redis:create {{cookiecutter.project_slug}}_redis
dokku redis:link {{cookiecutter.project_slug}}_redis {{cookiecutter.project_slug}}

# Configure persistent storage
mkdir -p  /var/lib/dokku/data/storage/{{cookiecutter.project_slug}}
chown -R 32767:32767 /var/lib/dokku/data/storage/{{cookiecutter.project_slug}}
dokku storage:mount {{cookiecutter.project_slug}} /var/lib/dokku/data/storage/{{cookiecutter.project_slug}}:/app/storage

# Configure environment variables
dokku config:set --no-restart {{cookiecutter.project_slug}} \
  DJANGO_SETTINGS_MODULE={{cookiecutter.project_slug}}.settings.production \
  DJANGO_SECRET_KEY=... \
  MAILGUN_API_KEY=...
```

### Configure Dokku locally and deploy
```
# Download Dokku locally
git clone git@github.com:dokku/dokku.git ~/.dokku

# add the following to either your
# .bashrc, .bash_profile, or .profile file
alias dokku='$HOME/.dokku/contrib/dokku_client.sh'

# Deploy
git remote add dokku dokku@{{cookiecutter.domain_name}}:{{cookiecutter.project_slug}}
git push dokku master
```
