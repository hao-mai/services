
## Welcome

This is my repo for all Django applications I will make in the future. It includes a swagger file to see all the endpoint users can interact with, such as:

* Create a RESTful API that allows developers to interact with data stored in a database. This app will provide various functionalities and features for devs with data already generated and/or new data to be created for an app called VirtualLibrary.
* Create a RESTful API that allows integrations to applications (Integrations API). TBD

## Enviroment

### Container

The project is run inside a container to house a development enviroment with all needed dependencies. I have decided to use a docker container because of
- Portability: run the same container on different machines or environments without worrying about differences in the underlying OS or system configuration.
- Isolation: the container runs in its own environment and does not interfere with other applications or services running on the host machine.
- Reproducibility: to define the entire application stack, including the database and other services, and spin up the entire stack.

services:
* The requirements.txt will install all the packages needed.
* DB is MySQL on port 3306

### Setup TBD

* how to clone repo
* how to build the Docker image for project
* how to run it
* how to test it

## Pre-commit

Installed from [pre-commit](https://pre-commit.com/).

To install the git hook (which will run only on changed files upon commit):

    pre-commit install

To manually run hooks only on files you've changed:

    pre-commit

To manually run hooks on the entire project:

    pre-commit run --all-files

## Running Tests

I choose [pytest](https://docs.pytest.org/en/6.2.x/getting-started.html) for all tests in my app(s).

To run all tests, simply run pytest with no arguments:

    pytest

## Model Fixtures

To provide initial data with migrations for Services app. This way, other who would like to test the CRUDs endpoints can generate the data.
* TBD


## Scheduled Tasks

Tasks are scheduled via a cron scheduler and then queued.
* TBD

## Swagger file

The `schema/` directory contained the swagger specificiation for our first API; virtual library. It can be used to automatically generate documentation and client libraries for the API, it can validate incoming requests and outgoing responses. Developers can access the schema by visiting `/library/schema` endpoint.
