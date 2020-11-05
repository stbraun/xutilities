# coding=utf-8
""" Configuration of nox test automation tool. """

import nox


@nox.session(python=['3.7', '3.8', '3.9'])
def tests(session):
    """Run tests for all supported versions of Python."""
    session.run("pipenv", "install", "--dev", external=True)
    session.run("flake8", "xutilities/", "tests/")
    session.run("pytest", "tests/")
