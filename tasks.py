"""
tasks.py
"""
import subprocess
from invoke import task

@task
def style(_):
    """
    pycodestyle check
    """
    cmd = f"pycodestyle signal_interpreter_client/ signal_interpreter_server/"
    subprocess.call(cmd, shell=True)

@task
def lint(_):
    """
    pylint check
    """
    cmd = f"pylint signal_interpreter_client/ signal_interpreter_server/"
    subprocess.call(cmd, shell=True)

@task
def unit_test(_):
    """
    unit-test check
    """
    cmd = f"pytest . --cov . --cov-config=.coveragerc --verbose"
    subprocess.call(cmd, shell=True)

