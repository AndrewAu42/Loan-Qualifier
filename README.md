# Loan Qualifier 

Due to the requested updates and changes to the business requirements, this is a business application that will facilitate with verifying individuals and data for a Loan Application. This is to be in line for a startup for a lending service, and will focus mainly  on large quantities of potential lenders. A csv file titled 'daily_rate_sheet' will provide the proper loan data with further questions to verify loan status, and returning information that relates to qualifying loans. 

---

## Technologies

Currently this requires use of Python 3.8, and the following packages:

```python
fire==0.3.1
questionary==1.5.2
pytest==5.4.2
```

These can be found and referenced to run the application in the requirements.txt file to run and reference. 

---

## Installation Guide

Please double check before running the application, you need to be sure to install the above mentioned technologies. 

Open python, and run the following lines in the command prompt:

```python
    pip install fire
    pip install questionary
    pip install pytest
```

or open python, and run the following line of code to pull the information directly from the requirements.txt file:

```python
    pip install -r (your path here)/requirements.txt
```
![Pulling Required Technologies from file](https://github.com/AndrewAu42/Loan-Qualifier/blob/main/images/pip_requirements_txt.png)

---

## Examples of Application

![Successful Loan:](https://github.com/AndrewAu42/Loan-Qualifier/blob/main/images/success_qualifying_loans.png)

![Unsuccessful Loan instance:](https://github.com/AndrewAu42/Loan-Qualifier/blob/main/images/failure_qualifying_loans.PNG)

---

## Usage

In order to run the application for loan qualifications, clone the repository from here: https://github.com/AndrewAu42/Loan-Qualifier.git

run **app.py** wit the follow code line in python:
```python
python app.py
```
![Running Application](https://github.com/AndrewAu42/Loan-Qualifier/blob/main/images/running_application.png)

---

## Contributors

Modified and updated by Andrew Au, with provided code from 2021 Rice FinTech Bootcamp. Hope this facilitates with the decision process for the end user.  

---

## License

MIT License


