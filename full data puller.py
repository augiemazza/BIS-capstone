import requests
import os
import json
import openai

# FMP API key
fmp_api_key = 'c0039cbd7daccd381cced70fe663c88c'

# OpenAI API key
openai.api_key = 'sk-tCswlzQdqh22Iz3hMCTRAJBjEHVdjaI2YkGR_cOJmJT3BlbkFJJfQIj7CoGhMrUeQeHMZYv53RPU-T1zMjZ27gUd2fQA'

# Directory where the files should be saved
save_directory = '/Users/augiemazza/Dropbox/BIS'

# Ensure the save directory exists
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# List of companies and their tickers
companies = {
    'alcon': 'ALC',
    'bausch_lomb': 'BLCO',
    'coopervision': 'COO',
    'rxsight': 'RXST'
}


### CASH FLOW STATEMENTS ###

# Function to fetch the most recent cash flow statement for a company
def fetch_cash_flow(company_ticker, api_key):
    url = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{company_ticker}?apikey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        cash_flow_data = response.json()
        if cash_flow_data:
            return cash_flow_data[0]  # Return the most recent cash flow statement
        else:
            print(f"No cash flow data found for {company_ticker}.")
            return None
    else:
        print(f"Error fetching data for {company_ticker}: {response.status_code}")
        return None

# Save combined cash flow statements
def save_combined_cash_flows(cash_flows, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(cash_flows, file, indent=4)
    print(f"Combined cash flow statements saved to {file_path}")

# Fetch and save cash flow data
def update_cash_flow_statements():
    combined_cash_flows = {}
    for company_name, company_ticker in companies.items():
        cash_flow = fetch_cash_flow(company_ticker, fmp_api_key)
        if cash_flow:
            combined_cash_flows[company_name] = cash_flow
    combined_cash_flow_path = os.path.join(save_directory, "combined_cash_flows.json")
    save_combined_cash_flows(combined_cash_flows, combined_cash_flow_path)


### BALANCE SHEETS ###

# Function to fetch the most recent balance sheet for a company
def fetch_balance_sheet(company_ticker, api_key):
    url = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company_ticker}?apikey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        balance_sheet_data = response.json()
        if balance_sheet_data:
            return balance_sheet_data[0]  # Return the most recent balance sheet
        else:
            print(f"No balance sheet data found for {company_ticker}.")
            return None
    else:
        print(f"Error fetching data for {company_ticker}: {response.status_code}")
        return None

# Save combined balance sheets
def save_combined_balance_sheets(balance_sheets, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(balance_sheets, file, indent=4)
    print(f"Combined balance sheets saved to {file_path}")

# Fetch and save balance sheet data
def update_balance_sheets():
    combined_balance_sheets = {}
    for company_name, company_ticker in companies.items():
        balance_sheet = fetch_balance_sheet(company_ticker, fmp_api_key)
        if balance_sheet:
            combined_balance_sheets[company_name] = balance_sheet
    combined_balance_sheet_path = os.path.join(save_directory, "combined_balance_sheets.json")
    save_combined_balance_sheets(combined_balance_sheets, combined_balance_sheet_path)


### INCOME STATEMENTS ###

# Function to fetch the most recent income statement for a company
def fetch_income_statement(company_ticker, api_key):
    url = f"https://financialmodelingprep.com/api/v3/income-statement/{company_ticker}?apikey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        income_statement_data = response.json()
        if income_statement_data:
            return income_statement_data[0]  # Return the most recent income statement
        else:
            print(f"No income statement data found for {company_ticker}.")
            return None
    else:
        print(f"Error fetching data for {company_ticker}: {response.status_code}")
        return None

# Save combined income statements
def save_combined_income_statements(income_statements, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(income_statements, file, indent=4)
    print(f"Combined income statements saved to {file_path}")

# Fetch and save income statement data
def update_income_statements():
    combined_income_statements = {}
    for company_name, company_ticker in companies.items():
        income_statement = fetch_income_statement(company_ticker, fmp_api_key)
        if income_statement:
            combined_income_statements[company_name] = income_statement
    combined_file_path = os.path.join(save_directory, "combined_income_statements.json")
    save_combined_income_statements(combined_income_statements, combined_file_path)


### EARNINGS CALL TRANSCRIPTS ###

# Fetch the earnings call transcript and save the combined file
def update_earnings_call_transcripts():
    combined_transcript_path = os.path.join(save_directory, 'combined_transcripts.txt')
    
    # Placeholder: Your logic for fetching and combining earnings call transcripts goes here
    
    print(f"Transcripts saved to {combined_transcript_path}")


### MASTER SCRIPT ###

# Function to run all updates
def run_master_update():
    print("Updating Cash Flow Statements...")
    update_cash_flow_statements()

    print("Updating Balance Sheets...")
    update_balance_sheets()

    print("Updating Income Statements...")
    update_income_statements()

    print("Updating Earnings Call Transcripts...")
    update_earnings_call_transcripts()

    print("All updates completed!")


# Call the master update function
if __name__ == "__main__":
    run_master_update()
