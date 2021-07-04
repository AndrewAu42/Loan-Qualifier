# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

def test_save_csv():
    qualify_loans = "test"
    csvoutput = Path("./tests/qualify_loans.csv")
    #location of path where the file test is to be run

    fileio.save_csv(
        csvoutput,
        qualify_loans,
        [
            #Headers for test file to be placed in CSV file
            "lender",
            "max_amount",
            "max_loan_value",
            "max_debt_to_income",
            "min_credit_score",
            "rate",
        ]
    )

    assert csvoutput.exists()
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84


##filter that pushes and verify's the data in the CSV
def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    bank_info_filtered = max_loan_size.filter_max_loan_size(loan,bank_data)
    bank_info_filtered = credit_score.filter_credit_score(
        current_credit_score,bank_info_filtered
    )
    bank_info_filtered = debt_to_income.filter_debt_to_income(
        monthly_debt_ratio,bank_info_filtered
    )
    bank_info_filtered = loan_to_value.filter_loan_to_value(
        loan_to_value_ratio,bank_info_filtered
    )

    assert len(bank_info_filtered) == 6