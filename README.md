# DDD-flask-mongodb-docker
Example to production APP with docker
# AlexDDD - Scalable and Optimized Flask Application with MongoDB and Docker: A Domain-Driven Design Example

## Introduction

This project is an example of a Flask application that uses a MongoDB database and is deployed with Docker. The main goal is to demonstrate a scalable and optimal architecture, following the best practices of Domain-Driven Design (DDD). It includes a basic authentication system using JWT and a CRUD for users as an example application. The project is designed to be easily deployable in different environments (dev, prod, test) using Docker.

Flask was chosen over other alternatives such as FastAPI because it allows for more flexibility and customization in handling requests. MongoDB was chosen as the database due to its ability to handle large volumes of data and its scalability.

Please note that this project is just an example and should not be used for small projects. Additionally, it is important to take into account security needs and adapt the JWT authentication system accordingly. Additionally, it is important to mention that this project is my personal vision of applying DDD to development.

## Requirements

The following are the requirements to deploy and run the application:

- Docker: to run the application and its dependencies in containers.
- Docker Compose: to manage the application's containers and their configuration.
It is important to have the latest version of these tools installed on your system to ensure compatibility with the application.

You should also configure the following environment variables in the .env file before deploying the application:
```
APP_USERNAME=alexddd
APP_PASSWORD=pass

WEB_HOST=alexddd_prod_api

JWT_ACCESS_TOKEN_EXPIRES= 900
JWT_REFRESH_TOKEN_EXPIRES= 1800 
JWT_SECRET_KEY='Your long secret key'

APP_USER_ADMIN = 'alejandropina'
APP_USER_EMAIL= 'alexddd@alejandropina.com'
APP_PASS= 'alejandropina'

MONGODB_HOST=alexddd_prod_mongodb
MONGODB_EXTERNAL_PORT=27019
MONGODB_LOCAL_PORT=27017
MONGODB_USERNAME=alexddd
MONGODB_PASSWORD=alexddd
MONGODB_DATABASE=app_alexddd
MONGODB_TIMEOUT=500

DEV_WEB_HOST=alexddd_dev_api
DEV_MONGODB_HOST=alexddd_dev_mongodb
DEV_MONGODB_EXTERNAL_PORT=27018
DEV_MONGODB_LOCAL_PORT=27017
DEV_MONGODB_USERNAME=alexddd
DEV_MONGODB_PASSWORD=alexddd
DEV_MONGODB_DATABASE=dev_alexddd
DEV_MONGODB_TIMEOUT=500

TEST_WEB_HOST=alexddd_test_api
TEST_MONGODB_HOST=alexddd_test_mongodb
TEST_MONGODB_EXTERNAL_PORT=27019
TEST_MONGODB_LOCAL_PORT=27017
TEST_MONGODB_USERNAME=alexddd
TEST_MONGODB_PASSWORD=alexddd
TEST_MONGODB_DATABASE=test_alexddd
TEST_MONGODB_TIMEOUT=500
```
## Deployment

To deploy the application, you need to have Docker and Docker Compose installed on your system.

- To deploy the application in a development environment, use the following command:
```
docker-compose -f docker-compose.dev.yml up
```
- To deploy the application in a testing environment, use the following command:
```
docker-compose -f docker-compose.test.yml up
```
- To deploy the application in a production environment, use the following command:
```
docker-compose -f docker-compose.prod.yml up
```
The files docker-compose.dev.yml, docker-compose.test.yml and docker-compose.prod.yml contain the necessary configuration to deploy the application in each of the aforementioned environments. It is important to note that it is necessary to configure the environment variables in the .env file before deploying the application.

Once the container is started, the application will be available on the port specified in the .env file or in the Docker configuration file.

