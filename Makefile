TESTS = tests
VENV ?= .venv
CODE = scrapper app src

ifeq ($(OS), Windows_NT)
SOURCE := $(VENV)/Scripts
else
SOURCE := $(VENV)/bin
endif

.PHONY: help
help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: up
up:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

.PHONY: docker
docker:
	docker-compose up --build

.PHONY: parse_news_test
parse_news_test:
	export OUTPUT_PATH=test_parsed.json && scrapy runspider scrapper/spiders/news/parse_news.py -a path=test_dataset_test.csv

.PHONY: parse_news_train
parse_news_train:
	export OUTPUT_PATH=train_parsed.json && scrapy runspider scrapper/spiders/news/parse_news.py -a path=train_dataset_train.csv

.PHONY: venv
venv:
	# python -m venv $(VENV)
	$(SOURCE)/python -m pip install --upgrade pip
	$(SOURCE)/python -m pip install poetry
	$(SOURCE)/poetry install

.PHONY: test
test: ## Runs pytest
	$(SOURCE)/pytest -v tests

.PHONY: lint
lint: ## Lint code
	$(SOURCE)/flake8 --jobs 4 --statistics --show-source $(CODE)
	$(SOURCE)/pylint --rcfile=setup.cfg $(CODE)
	$(SOURCE)/mypy $(CODE)
	$(SOURCE)/black --line-length 80 --skip-string-normalization --check $(CODE)

.PHONY: format
format: ## Formats all files
	$(SOURCE)/isort $(CODE)
	$(SOURCE)/black --line-length 80 --skip-string-normalization $(CODE)
	$(SOURCE)/autoflake --recursive --in-place --remove-all-unused-imports $(CODE)
	$(SOURCE)/unify --in-place --recursive $(CODE)

.PHONY: ci
ci:	lint test ## Lint code then run tests
