# coding=utf-8
""" Configuration of nox test automation tool. """

import nox


@nox.session(python=['3.8'])
def lint(session):
    """Run static analysis."""
    session.run("pipenv", "install", "--dev", external=True)
    session.run("flake8", "xutilities/", "tests/")


@nox.session(python=['3.8'])
def tests(session):
    """Run tests for all supported versions of Python."""
    session.run("pipenv", "install", "--dev", external=True)
    session.run("pytest", "tests/")