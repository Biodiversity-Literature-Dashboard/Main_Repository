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

3. Open virtual environment:

Linux:

```bash
source venv/bin/activate
```

Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

4. Install Python dependencies

```bash
pip install -r requirements.txt
```

## Setting up SQLite database and data cleaning

Go to the `set_up_and_data_exploration` folder. First, check that the notebook is using the Excel file of your choice and run `data_exploration_excel.ipynb` to inspect the data.

After this, carefully go through and run `set_up.ipynb` to set up the SQLite database for your data. Make sure you are converting the correct file.

Additional CSV setup scripts are located in the `set_up_csv` folder.

## Running the program

(make sure you have opened the virtual environment, it should say venv in the corner)

```bash
invoke start
```

On Windows, if `invoke` is not recognized, use:

```bash
python -m invoke start
```

## Running tests

Make sure Chromedriver or Geckodriver (Firefox) is installed!!

[Chrome driver install guide (Ubuntu)](https://tecadmin.net/install-chromedriver-on-ubuntu/)
[General Chromedriver install guide](https://www.automationtestinghub.com/download-chrome-driver/)

[Install Geckodriver here](https://github.com/mozilla/geckodriver/releases)



(make sure you have opened the virtual environment, it should say venv in the corner)

On Windows, if `invoke` is not recognized, replace `invoke` with `python -m invoke` in the commands below.

1. Run non-ui tests on terminal:

```bash
invoke test
```

Run UI tests (Chromedriver) on terminal (headless):

```bash
invoke chromedriver
```

Run UI tests (Chromedriver) on terminal (browser):

```bash
invoke chromedriver-browser
```

Run UI tests (Geckodriver) on terminal (headless):

```bash
invoke geckodriver
```
Run UI tests (Geckodriver) on terminal (browser):

```bash
invoke geckodriver-browser
```

2. Open test coverage report in terminal

```bash
invoke coverage-report
```




 