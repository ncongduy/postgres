## Introduction
This repo helps to run postgres at local via docker. There are 2 postgres containers (raw database and clean database).

## Prerequisite
- docker installation

## How to run
- change mount path in Makefile
- run postgres container: `make run-postgres`
- raw postgres database is running on port 6000 locally (localhost:6000)
- clean postgres database is running on port 7000 locally (localhost:7000)  
- stop postgres container: `make stop-postgres`
