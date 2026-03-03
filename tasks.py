from invoke import task
from subprocess import call
from sys import platform

@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)

@task
def test(ctx):
    """Runs coverage tests"""
    ctx.run("coverage run --branch -m pytest", pty=True)


@task
def coverage_report(ctx):
    """Returns coverage report"""
    ctx.run("coverage html", pty=True)
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))