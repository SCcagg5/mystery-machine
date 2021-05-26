FROM python:3.9.1-buster

MAINTAINER Courtel Eliot <eliot.courtel@wanadoo.fr>
WORKDIR /home/project

COPY ./ ./
RUN for file in `ls -d */requirements.txt`; do \
      pip3 install --upgrade -r $file; \
    done

ENTRYPOINT for folder in `ls -d */` ; do \
              cd $folder; \
              echo -n "\e[4m\e[96m$folder :\e[0m\e[39m  "; \
              python3.7 *.py `cat args` || echo "fail"; \
              echo ; \
              cd ../; \
           done
