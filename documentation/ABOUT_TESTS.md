# About tests
We have made sure that all tests run automatically on GitHub using CodeQL. To edit how automated tests run or what folders you want to be run, change the [.yml file found in the workflows folder](https://github.com/Biodiversity-Literature-Dashboard/Main_Repository/blob/main/.github/workflows/python-app.yml) 

All tests can be found in the tests folder. End-to-end tests have their seperate subfolder (tests/ui) and are run seperately from other tests.
All test commands can be found in README.md. 

The tests do not cover the whole program. 
To see which files and how much of the files has been covered run tests and open coverage report in browser:

```bash
invoke test
invoke coverage-report
```

Documentation to help writing tests:

[Pytest website](https://docs.pytest.org/en/stable/)

[Unittest website](https://docs.python.org/3/library/unittest.html)

[Pandas testing](https://pandas.pydata.org/docs/reference/testing.html)

Dash has some of its own testing fixtures for both pytest and Selenium that you can use:

[Dash testing](https://dash.plotly.com/testing)

## End-to-End/User Interface tests:

Installing Chromedriver is recommended over Geckodriver. One of the issues seems to be Geckodriver passing tests that do not pass on Cromedriver.

Remember to also check that tests run on both headless and browser mode! 

Dash's custom Browser APIs are rather limited, so using regural Selenium webdriver commands might be needed:

[Selenium webdriver website](https://www.selenium.dev/about/)

When using a dash_duo test function from the Dash testing documentation linked earlier, you can use regular Selenium commands by replacing driver with dash_duo.driver.

Use:

```python
driver = dash_duo.driver
```

instead of 

```python
driver = webdriver.Chrome()
```
