# Main_Repository

Project done for the Data Science Project course (DATA 11004) at the University of Helsinki.
Building an interactive dashboard for indirect threats to biodiversity.
- [In depth description](https://github.com/Biodiversity-Literature-Dashboard/Main_Repository/blob/64-code-cleanupreorganizing/documentation/PROJECT_DESCRIPTION.md)
- [Architecture](https://github.com/Biodiversity-Literature-Dashboard/Main_Repository/blob/64-code-cleanupreorganizing/documentation/ARCHITECTURE.md)
- [Staging server]()
- [Changelog]()
- [Product backlog](https://github.com/orgs/Biodiversity-Literature-Dashboard/projects/2)
- [Sprint backlogs](https://github.com/orgs/Biodiversity-Literature-Dashboard/projects)
- [Coding conduct]()
- [Definition of done]()

## Setting up repository

1. Clone the repository:

```bash
git clone https://github.com/Biodiversity-Literature-Dashboard/Main_Repository.git
cd Main_Repository
```

2. Create a virtual environment:

Linux:

```bash
python3 -m venv venv
```
Windows:

```bash
python -m venv venv
```

3. open virtual environment:

Linux:
```bash
source venv/bin/activate
```
Windows:
```bash
venv\Scripts\activate
```
4. Install Python dependencies

```bash
pip install -r requirements.txt
```
## Running the program

(make sure you have opened the virtual environment, it should say venv in the corner)

```bash
invoke start
```

## Running tests

Make sure Chromedriver or Geckodriver (Firefox) is installed!!

[Chrome driver install guide (Ubuntu)](https://tecadmin.net/install-chromedriver-on-ubuntu/)
[General Chromedriver install guide](https://www.automationtestinghub.com/download-chrome-driver/)

[Install Geckodriver here](https://github.com/mozilla/geckodriver/releases)



(make sure you have opened the virtual environment, it should say venv in the corner)

1. Run tests (Chromedriver) on terminal:

```bash
invoke test
```

Run tests (Geckodriver) on terminal:

```bash
invoke test-geckodriver
```

2. Open test coverage report in terminal

```bash
invoke coverage-report
```




