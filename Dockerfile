FROM python:3.9.1-buster

MAINTAINER Courtel Eliot <eliot.courtel@wanadoo.fr>
WORKDIR /home/project

COPY ./ ./
RUN for file in `ls -d */requirements.txt`; do \
      pip3 install --upgrade -r $file; \
    done

ENTRYPOINT for file in `ls -d */*.py` ; do \
              python3 $file `echo $file | cut -d'/' -f1`/data.json; \
           done
