# Intermediate Python S/W Development 

Organized by VCC & Veldi Kompetens AB

# 1: Virtual Environment, Setting-Up Flask Server and Git

One of the easiest option to setup *virtual environment* IMO is Python 3's own *venv* built-in package. The simple command to create your new environment is to call `python -m venv [PATH_TO_VENV]`. If you want to bundle *venv*'s environment in the project, you can point your working directory as the PATH, e.g., `python -m venv ./vcc_venv/`. Next you can activate the *vcc_venv* virtual environment by running *activate* script under *./vcc_venv/Scripts/activate*.

This course uses *pipenv* package, therefore you must install the package first by calling `python -m pip install pipenv`. 

Personally, as long as you know what package to use, it's good to put it in *requirements.txt* file. Later on when you invoke `pipenv shell` on your working directory with *requirements.txt* file, *pipenv* will set up Pipfile with all packages copied from the *requirements.txt* file. For *venv*, you can install all packages in *requirements.txt* by invoking `python -m pip install -r requirements.txt`.

Note: This repository has *.gitignore* which contains both *Pipfile* and *Pipfile.lock*, that means when you clone it out, you won't see any Pipfile. You must run pipenv command in the previous paragraph to do so.

# 2: Unittest, Mocking and Patching

To run:

1. Run `git clone https://github.com/yanuartadityan/signal_interpreter_groupwork.git --recursive`. Codes for each *server* and *client* are in two different repositories, and linked through Git submodules. Therefore `--recursive` will also clone both server and client submodules with main repository.
2. After a while using *pipenv*, I feel like using *venv* is easier. From terminal, go to the root directory of the directory and create *venv*'s environment by running `python3 -m venv .venv/`. This will save the virtual environment named `venv` locally.
3. Activate the virtual environment by running `.venv/bin/activate` or if Git-Bash is used, `source .venv/bin/activate`. To deactivate just run `deactivate`.
4. Install all the dependancies, `python3 -m pip install -r requirements.txt`.
5. Add the current project directory to PYTHONPATH environment variable. This can done by `export PYTHONPATH=$PYTHONPATH:$(pwd)`
6. Run all tests `pytest -v`.

Next to run with coverage:
1. Install `pytest-cov` package (already added in the requirements.txt).
2. Now pytest will support `--cov` arguments. To run with coverage, run `<signal_interpreter_groupwork>$ pytest --verbose --cov-config=.coveragerc --cov .`

Some notes on the Git stuffs:
1. When adding another repository as modules, they are automatically detached from their HEAD:master branch. This allows us to focus on our own development repo as usually we don't contribute much on the submodules.
2. For this project, instead, collaborators are actively working with the submodules (*signal_interpreter_server* and *signal_interpreter_client*). Then, for collaborators to start working, first is you must create a branch in each submodule directory, e.g., `git branch exercise_3` then followed by `git checkout exercise_3`. 
3. When the work is done, stage and commit, then merge the changes in *exercise_3* to the main branch. To merge, perform `git checkout main`, followed by `git merge exercise_3`. Then you can push to the Github repository.

# 3: Even More on Unittest, Pylint & Pycodestyle, Parametrizing Unittest

To run:

1. If you already have the repository, perform clean submodule updates `git pull` followed by `git submodule update --init --recursive`. 
2. Install even more modules in *pip* by calling `python -m pip install -r requirements.txt`.
3. Run pycodestyle by invoking `invoke style`, run pylint by invoking `invoke lint` and run unit test by invoking `invoke unit-test`.

