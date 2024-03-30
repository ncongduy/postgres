# should change mount path below
MOUNT_PATH_RAW=/home/ncd/workspace/postgres/raw_data
MOUNT_PATH_CLEAN=/home/ncd/workspace/postgres/raw_data

run-postgres:
	docker run --name raw-database --rm  -e POSTGRES_PASSWORD=password -p 6000:5432 -d -v $(MOUNT_PATH_RAW):/var/lib/postgresql/data postgres
	docker run --name clean-database --rm  -e POSTGRES_PASSWORD=password -p 7000:5432 -d -v $(MOUNT_PATH_CLEAN):/var/lib/postgresql/data postgres

stop-postgres:
	docker stop $(shell docker ps -aq)
