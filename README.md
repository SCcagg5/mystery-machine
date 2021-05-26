### global testing using docker
launch using:
  ```bash
  docker-compose up -d
  sleep 3
  docker logs mystery-machine
  ```

### Without docker

from inside each exercice folder 
  ```bash 
  python3.7 *.py `cat args`
  ```
