# main.py

import streamlit as st
from policyholder import Policyholder
from payments import Payment

# Initialize session state for policyholders and payments if they don't exist
if 'policyholders' not in st.session_state:
    st.session_state.policyholders = []
if 'payments' not in st.session_state:
    st.session_state.payments = []

def register_policyholder():
    """Register a new policyholder."""
    st.subheader("Register a Policyholder")
    policyholder_id = st.text_input("Policyholder ID")
    fname = st.text_input("First Name")
    lname = st.text_input("Last Name")
    address = st.text_input("Address")

    if st.button("Register"):
        new_policyholder = Policyholder(policyholder_id, fname, lname, address)
        new_policyholder.register()
        st.session_state.policyholders.append(new_policyholder)  # Add to session state
        st.success(f"Policyholder {fname} {lname} registered successfully.")

def view_policyholders():
    """View registered policyholders."""
    st.subheader("Registered Policyholders")
    if st.session_state.policyholders:  # Check if there are any policyholders
        for ph in st.session_state.policyholders:
            st.write(f"ID: {ph.policyholder_id}, Name: {ph.fname} {ph.lname}")

        selected_id = st.selectbox("Select Policyholder ID to view details", [ph.policyholder_id for ph in st.session_state.policyholders])
        
        # Display the selected policyholder details
        for ph in st.session_state.policyholders:
            if ph.policyholder_id == selected_id:
                st.write(f"**ID:** {ph.policyholder_id}")
                st.write(f"**Name:** {ph.fname} {ph.lname}")
                st.write(f"**Email:** {ph.email}")
                st.write(f"**Address:** {ph.address}")
                st.write(f"**Status:** {ph.status}")
    else:
        st.write("No policyholders registered yet.")

def create_payment():
    """Create a new payment."""
    st.subheader("Create a Payment")
    payment_id = st.text_input("Payment ID")
    payment_amount = st.number_input("Payment Amount", min_value=0.0)
    
    if st.button("Create Payment"):
        new_payment = Payment(payment_id, payment_amount)
        new_payment.process_payment()
        st.session_state.payments.append(new_payment)  # Add to session state
        st.success(f"Payment ID: {payment_id} created successfully.")

def main():
    st.title("Yaspi Insurance Policy Management System")

    menu = ["Register Policyholder", "View Policyholders", "Create Payment"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Register Policyholder":
        register_policyholder()
    elif choice == "View Policyholders":
        view_policyholders()
    elif choice == "Create Payment":
        create_payment()

if __name__ == "__main__":
    main()

