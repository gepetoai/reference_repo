#reference repository for AWS ECR-> ECS deployment

#alembic commands 
docker compose run --rm web alembic revision --autogenerate -m "description" 

docker compose run --rm web alembic upgrade head



# Setup Instructions

### Create Virtual Environment
To create a virtual environment, run the following command:



### Activate Environment
Activate the virtual environment using the appropriate command for your operating system:

- **Windows:**
  ```bash
  source ./env/Scripts/activate
  ```

- **macOS/Linux:**
  ```bash
  source ./env/bin/activate
  ```
