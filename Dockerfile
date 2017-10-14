FROM centos:centos7

MAINTAINER Olumide Karim-Mohammed <kmoh19@gmail.com>

# Set env variables used in this Dockerfile (add a unique prefix, such as DOCKYARD)
# Local directory with project source
ENV DOCKYARD_SRC=code/simplesocial
# Directory in container for all project files
ENV DOCKYARD_SRVHOME=/srv
# Directory in container for project source files
ENV DOCKYARD_SRVPROJ=$DOCKYARD_SRVHOME/$DOCKYARD_SRC


RUN yum install -y epel-release

RUN yum update -y
RUN yum install -y yum-utils
RUN yum groupinstall -y "Development Tools"
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum install -y python36u python36u-pip python36u-devel python36u-setuptools git
RUN yum install -y wget
RUN yum install -y  postgresql-server postgresql-devel postgresql-contrib gcc nginx 
RUN yum install -y nginx supervisor
RUN yes | pip3.6 install gunicorn psycopg2
RUN yes | pip3.6 install uwsgi

# Create application subdirectories
WORKDIR $DOCKYARD_SRVHOME
RUN mkdir -m 777 media static logs

#read
VOLUME ["$DOCKYARD_SRVHOME/media/", "$DOCKYARD_SRVHOME/logs/"]
# Copy application source code to SRCDIR
COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ

RUN yum install -y libffi libffi-devel
RUN yum install -y patch

# Install Python dependencies
RUN yes | pip3.6 install -r $DOCKYARD_SRVPROJ/requirement.txt
# Port to expose
EXPOSE 8000
# Copy entrypoint script into the image
WORKDIR $DOCKYARD_SRVPROJ
COPY ./docker-entrypoint.sh /
COPY ./django_nginx.conf /etc/nginx/nginx.conf
#RUN cat /etc/nginx/sites-available/django_nginx.conf >> /etc/nginx/nginx.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
ENTRYPOINT ["/docker-entrypoint.sh"]

