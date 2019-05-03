# Advisagator


[![Travis Build Status](https://travis-ci.com/GatorEducator/quizagator.svg?branch=master)](https://travis-ci.com/GatorEducator/advisagator)
<!-- [![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/gatoreducator/quizagator.svg?style=popout)](https://hub.docker.com/r/gatoreducator/quizagator) -->
[![codecov.io](http://codecov.io/github/GatorEducator/advisagator/coverage.svg?branch=master)](http://codecov.io/github/GatorEducator/advisagator?branch=master)
<!-- [![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat)](#contributors) -->
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)

## A planning Tool or communicate your 4 year plan with your advisers.

Advisagator allows you to download a 4 year plan template to be filled out by you
and then uploaded back up. The tool automatically adds your name to start of the
file name so that is easy for the adviser to recognize and manage the different plans
that are uploaded by several students.

This tool was made to aid communication between student and adviser and helps reduce
unnecessarily meeting in person and allows the professor to keep track of the student's
progress in each year.


## Pipenv

Advisagator uses a [Pipenv](https://project/pipenv/)-built virtual environment
to standardize the execution of the project. If you don't have pipenv we highly
recommend installing it using `pip`:

```
pip install pipenv
```

If for some reason this doesn't work for you, you can check out the [pipenv
github](https://github.com/pypa/pipenv).

## Commands

After cloning the repo for the first time, run

```
pipenv install --dev
```

to install the developer and default packages. To get a list of scripts for the
project, inspect the `[scripts]` tag in `Pipfile`:

```
cat Pipfile
```

Finally, to run the project locally in development mode:

```
pipenv run server
```

Or use the following to see all the options:

```
pipenv run python run.py --help
```

<!-- ## Docker

There is a docker image published to
[gatoreducator/quizagator](https://hub.docker.com/r/gatoreducator/quizagator).
There are two main parts of configuration: specifying a secret in the
`FLASK_SECRET_KEY` environment variable, and forwarding the desired outer port
to `80` inside the container. The following command does both:

```
docker run --name quizagator -p 5000:80 -e FLASK_SECRET_KEY=d2dbb3 gatoreducator/quizagator:0.0.1-dev
```

Additionally, developers can use `pipenv run create-image` and `pipenv run
image` to run a development container -- this is not to be deployed to
production. -->
