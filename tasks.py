from invoke import task
from subprocess import call
from sys import platform

USE_PTY = platform != "win32"

@task
def start(ctx):
    if platform == 'linux':
        ctx.run("python3 app.py", pty=USE_PTY)
    else:
        ctx.run("python app.py", pty=USE_PTY)


@task
def test(ctx):
    """Runs non-UI tests only"""
    ctx.run("coverage run --branch -m pytest tests --ignore=tests/ui", pty=USE_PTY)

@task
def geckodriver(ctx):
    """Runs UI tests using Geckodriver/Firefox in headless mode"""
    ctx.run("coverage run --branch -m pytest tests/ui --webdriver Firefox --headless", pty=True)

@task
def chromedriver(ctx):
    """Runs UI tests using Chromedriver/Chrome in headless mode"""
    ctx.run("coverage run --branch -m pytest tests/ui --webdriver Chrome --headless", pty=True)

@task
def geckodriver_browser(ctx):
    """Runs UI tests using Geckodriver/Firefox"""
    ctx.run("coverage run --branch -m pytest tests/ui --webdriver Firefox", pty=True)

@task
def chromedriver_browser(ctx):
    """Runs UI tests using Chromedriver/Chrome"""
    ctx.run("coverage run --branch -m pytest tests/ui --webdriver Chrome", pty=True)

@task
def coverage_report(ctx):
    """Returns coverage report"""
    ctx.run("coverage html", pty=USE_PTY)
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))
