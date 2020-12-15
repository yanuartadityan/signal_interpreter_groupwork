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
    cmd = f"pycodestyle signal_interpreter_client/ signal_interpreter_server/ --max-line-length=120"
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
    cmd = f"pytest signal_interpreter_server/tests/unit --cov signal_interpreter_server/ --cov-config=.coveragerc --verbose"
    subprocess.call(cmd, shell=True)

@task
def integration_test(_):
    """
    integration-test check
    """
    cmd = f"pytest signal_interpreter_server/tests/integration  --verbose"
    subprocess.call(cmd, shell=True)
