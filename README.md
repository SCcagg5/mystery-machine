### global testing using docker
Launch using:
  ```bash
  docker-compose up -d
  sleep 3
  docker logs mystery-machine
  ```

### Without docker

From inside each exercice folder 
  ```bash 
  python3.7 *.py `cat args`
  ```
