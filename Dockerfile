FROM registry.access.redhat.com/ubi8/ubi

COPY . .

RUN yum -y install python3 python3-pip && pip3 install flask

CMD /usr/bin/python3 app.py
