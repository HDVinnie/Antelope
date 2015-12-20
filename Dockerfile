FROM python:3.5.1-onbuild
ENV DJANGO_CONFIGURATION Docker
CMD ["gunicorn", "-c", "gunicorn_conf.py", "--chdir", "antelope", "antelope.wsgi:application", "--reload"]
