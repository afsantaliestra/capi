.DEFAULT_GOAL := compose

compose:
	@echo "\e[44mLaunching docker for development\e[0m"
	cd ci/development; docker-compose --progress plain -f docker-compose.yml up -d

install:
	@echo "\e[44mInstalling poetry deps\e[0m"
	poetry install

run: install
	@echo "\e[44mLaunching docker for development\e[0m"
	poetry run python src

build: check_format ln lint ln test

format: black ln isort

black:
	@echo "\e[44mBlack formatter\e[0m"
	@poetry run black --line-length=99 src/
	@poetry run black --line-length=99 tests/

isort:
	@echo "\e[44mIsort formatter\e[0m"
	@poetry run isort --settings-path dev_configs/.isort.cfg src/
	@poetry run isort --settings-path dev_configs/.isort.cfg tests/

check_format: check_black ln check_isort

check_black:
	@echo "\e[44m(Check) Black formatter\e[0m"
	@poetry run black --check --line-length=99 src/
	@poetry run black --check --line-length=99 tests/

check_isort:
	@echo "\e[44m(Check) Isort formatter\e[0m"
	@poetry run isort --check --settings-path dev_configs/.isort.cfg src/
	@poetry run isort --check --settings-path dev_configs/.isort.cfg tests/

lint: pylint ln bandit ln flake8

pylint:
	@echo "\e[44mPylint linter\e[0m"
	@echo "src folder"
	@poetry run pylint --rcfile=dev_configs/.pylintrc src/
	@echo "tests folder"
	@poetry run pylint --rcfile=dev_configs/.pylintrc tests/

bandit:
	@echo "\e[44mBandit linter\e[0m"
	@poetry run bandit -c dev_configs/.bandit . -r 

flake8:
	@echo "\e[44mFlake8 linter\e[0m"
	@poetry run flake8 --config dev_configs/.flake8 .

test:
	@echo "\e[44mUnitTest with Pytest\e[0m"
	@poetry run pytest

ln:
	@echo ""
