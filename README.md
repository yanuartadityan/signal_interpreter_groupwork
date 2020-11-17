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
5. Run all tests `pytest -v`.

# 3: TBD