# dockerfile from https://defiant-tarsal-f6e.notion.site/ae3885d33a304523bd1a99a4a191210d
FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

EXPOSE 8000

RUN    apt-get -y update
RUN    apt-get -y install vim
RUN    apt-get -y install python3.9-dev python3-venv python3-pip
RUN    apt-get -y install postgresql postgresql-contrib libpq-dev


RUN useradd -b /home -m -s /bin/bash django
RUN usermod -a -G www-data django
RUN mkdir -p /var/www/django
RUN mkdir -p /var/www/django/run
RUN mkdir -p /var/www/django/logs
RUN mkdir -p /var/www/django/ini

RUN python3 -m venv /var/www/django/venv
RUN chown -R django:www-data /var/www/django
RUN chmod -R g+w /var/www/django

ADD ./piro_docker /var/www/django/code

RUN /var/www/django/venv/bin/pip3 install wheel
RUN /var/www/django/venv/bin/pip3 install -U uwsgi
ADD ./uwsgi.service /etc/systemd/system/uwsgi.service
ADD ./uwsgi.ini /var/www/django/ini/uwsgi.ini

ADD ./requirements.txt /var/www/django/requirements.txt
RUN /var/www/django/venv/bin/pip3 install -r /var/www/django/requirements.txt


CMD ["bash", "-c", "source /var/www/django/venv/bin/activate && uwsgi --ini /var/www/django/ini/uwsgi.ini"]