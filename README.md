# DisplayMain: Unattended Web Display Application

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setting Up the Development Environment](#setting-up-the-development-environment)
- [Running the Application](#running-the-application)
  - [Docker Compose](#docker-compose)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview
DisplayMain is an unattended web display application designed to run on a dedicated PC and display information on a large screen. It is powered by FastAPI and can be used to showcase customized content to viewers who pass by the display.

## Project Structure
The project has the following structure:


## Getting Started

### Prerequisites
Ensure the following prerequisites are installed on the development machine:
- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

### Setting Up the Development Environment
1. Clone the project repository to your local machine:

   `git clone <repository-url>`

### Running the Application

1. Build the Docker image for the FastAPI application:

`docker-compose build`

2. Start the containers:

`docker-compose up`

The FastAPI dev server should now be running, and you can access it by opening a web browser and navigating to http://localhost:8000. You should see the "Hello world" message.


## Troubleshooting

If you encounter any issues or errors while setting up or running the application, please refer to the Troubleshooting section in the README or seek assistance from the project contributors.

