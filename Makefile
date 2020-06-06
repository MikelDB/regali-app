SHELL=/bin/bash

.DEFAULT_GOAL := help


help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

up: ## Spin up the project
	docker-compose up -d
	docker-compose exec api bash

down: ## Bring down the environment
	docker-compose down
	docker stop $(docker ps -aq)
