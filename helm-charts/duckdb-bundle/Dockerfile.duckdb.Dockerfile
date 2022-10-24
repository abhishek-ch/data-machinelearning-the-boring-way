FROM apache/superset:1.5.2

# Switching to root to install the required packages
USER root

# RUN apt-get update && apt-get install ca-certificates

COPY cacert.pem /usr/share/ca-certificates
RUN apt-get update && update-ca-certificates
# Example: installing the MySQL driver to connect to the metadata database
# if you prefer Postgres, you may want to use `psycopg2-binary` instead
RUN pip install psycopg2==2.9.4 && \
    pip install pyarrow==5.0.0 && \
    pip install awscli --upgrade --user && \
    pip install boto3 && \
    pip install pyhive[hive] && \
    pip install pyhive[presto] && \
    pip install duckdb-engine==0.6.4 && \
    pip install httpfs && \
    pip install markupsafe==2.0.1 && \
    pip install certifi

ADD ./config/superset_config.py /app/pythonpath/superset_config.py

EXPOSE 8088

# Switching back to using the `superset` user
USER root
RUN export PYTHONHTTPSVERIFY=0 

RUN update-ca-certificates --fresh
RUN export SSL_CERT_DIR=/etc/ssl/certs


RUN superset db upgrade
RUN export FLASK_APP=superset
# RUN superset fab create-admin

# Load some data to play with
RUN superset load_examples

# Create default roles and permissions
RUN superset init

# To start a development web server on port 8088, use -p to bind to another port
CMD superset run -p 8088 --with-threads --reload --debugger