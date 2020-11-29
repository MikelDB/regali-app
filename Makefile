SHELL=/bin/bash

.DEFAULT_GOAL := help


help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

up: ## Spin up the project
	docker-compose up -d

down: ## Bring down the environment
	docker-compose down

in: ## Enter docker api machine
	docker-compose exec api bash

pylint: ## Pylint code
	docker-compose exec api pylint --load-plugins pylint_flask_sqlalchemy app

unittest: ## Unittest code
	docker-compose exec api python -m unittest discover -s tests/unit/ 