import streamlit as st
import pandas as pd


# Function to calculate loan data
def loan_amount(principal, rate, term):
    # Calculate monthly interest rate
    monthly_rate = rate / 12
    # Calculate monthly payment using the formula assuming linear payments
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** (-term))
    # Initialize remaining principal and total amount
    remaining_principal = principal
    total_amount = 0

    # Initialize data frame
    data = pd.DataFrame()

    # Iterate over loan term and calculate some values for each month
    for month in range(1, term + 1):
        # Calculate interest amount
        interest_amount = remaining_principal * monthly_rate
        # Calculate principal amount
        principal_amount = monthly_payment - interest_amount
        # Update remaining principal and total amount
        remaining_principal = remaining_principal - principal_amount
        total_amount = total_amount + monthly_payment
        # Print the result
        data_one_iter = pd.DataFrame({
            'month': [month],
            'monthly_payment': [monthly_payment],
            'interest_amount': [interest_amount],
            'remaining_principal': [remaining_principal],
            'total_amount': [total_amount]})
        data = pd.concat([data, data_one_iter], ignore_index=True)
    data['interest_monthly_ratio'] = data['interest_amount'] / data['monthly_payment']
    
    return data, total_amount

st.title('Calculate Loan - Dashboard')

col1, col2, col3 = st.columns(3)

with col1:
    principal = st.number_input('Principal amount', min_value=0, value=100000, step=1)
with col2:  
    interes_rate = st.number_input('Interest rate', min_value=0.00, value=5.00, step=0.25)/100
with col3:
    term = st.number_input('Term (in years)', min_value=0, value=30, step=1)/12

data, total_amount = loan_amount(principal, interes_rate, term)


st.write('Monthly installment: ', round(data['monthly_payment'][0]))
st.write('Total amount payed at the end of the loan period: ', round(total_amount))

