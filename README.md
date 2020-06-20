# Ubex test application
Simple REST CRUD for all models in project


### Get Started (with Docker)
- Run postgres on you machine
- Create postgres database
```
ubex_authapi
```
- Run docker on you machine
- Call command to run dev project in docker 
```bash
make run_dev_in_docker
```
- Open
```
http://127.0.0.1:8000/api/
```
---
### Get Started (without Docker)
- Run postgres on you machine
- Create postgres database
```
ubex_authapi
```
- Run docker on you machine
- Install python3.8 on you machine
- Call command to run dev project
```bash
make run_dev
```
- Open
```
http://127.0.0.1:8000/api/
```


### Env Variables
- DEBUG (default True, *since this project is not for launch in production, but ready to run*)
- DATABASE_URL (default postgres://postgres:postgres@127.0.0.1/ubex_authapi)
- SECRET_KEY (default 123456)
- ALLOWED_HOSTS (default ["localhost", "127.0.0.1"])
