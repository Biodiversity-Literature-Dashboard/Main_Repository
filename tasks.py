from invoke import task
from subprocess import call
from sys import platform

@task
def start(ctx):
    ctx.run("python3 app.py", pty=True)

@task
def test(ctx):
    """Runs coverage tests using Chromedriver"""
    ctx.run("coverage run --branch -m pytest", pty=True)

@task
def test_geckodriver(ctx):
    """Run tests using Geckodriver/Firefox"""
    ctx.run("coverage run --branch -m pytest --webdriver Firefox", pty=True)


@task
def coverage_report(ctx):
    """Returns coverage report"""
    ctx.run("coverage html", pty=True)
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))