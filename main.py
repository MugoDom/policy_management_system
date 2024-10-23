
import streamlit as st
from policyholder import Policyholder
from product import Product_Management
from payments import Payment

# Initialize session state for policyholders, products, and payments if they don't exist
if 'policyholders' not in st.session_state:
    st.session_state.policyholders = []
if 'products' not in st.session_state:
    st.session_state.products = []
if 'payments' not in st.session_state:
    st.session_state.payments = []

def manage_products():
    """Manage products."""
    st.subheader("Manage Products")
    
    product_id = st.text_input("Product ID")
    product_name = st.text_input("Product Name")
    product_price = st.number_input("Product Price", min_value=0.0)
    selected_policyholder_id = st.selectbox("Select Policyholder for this Product", [ph.policyholder_id for ph in st.session_state.policyholders])

    if st.button("Create Product"):
        new_product = Product_Management(product_id, product_name, product_price)
        st.session_state.products.append(new_product)

        # Find the selected policyholder and add the product to their list
        for ph in st.session_state.policyholders:
            if ph.policyholder_id == selected_policyholder_id:
                ph.add_product(new_product)
                st.success(f"Product {product_name} added to Policyholder {ph.fname} {ph.lname}'s account.")

def register_policyholder():
    """Register a new policyholder."""
    st.subheader("Register a Policyholder")
    policyholder_id = st.text_input("Policyholder ID")
    fname = st.text_input("First Name")
    lname = st.text_input("Last Name")
    address = st.text_input("Address")

    if st.button("Register"):
        new_policyholder = Policyholder(policyholder_id, fname, lname, address)
        st.session_state.policyholders.append(new_policyholder)
        st.success(f"Policyholder {fname} {lname} registered successfully.")

def view_policyholders():
    """View registered policyholders and manage their status."""
    st.subheader("Registered Policyholders")
    if st.session_state.policyholders:
        for ph in st.session_state.policyholders:
            st.write(f"ID: {ph.policyholder_id}, Name: {ph.fname} {ph.lname}, Status: {ph.status}")

        selected_id = st.selectbox("Select Policyholder ID to manage", [ph.policyholder_id for ph in st.session_state.policyholders])
        
        for ph in st.session_state.policyholders:
            if ph.policyholder_id == selected_id:
                st.write(f"**ID:** {ph.policyholder_id}")
                st.write(f"**Name:** {ph.fname} {ph.lname}")
                st.write(f"**Email:** {ph.email}")
                st.write(f"**Address:** {ph.address}")
                st.write(f"**Status:** {ph.status}")

                st.write("### Products")
                if ph.products:
                    for product in ph.products:
                        st.write(f"- {product.product_name} (Price: {product.product_price})")
                else:
                    st.write("No products linked.")

                st.write("### Payments")
                if ph.payments:
                    for payment in ph.payments:
                        st.write(f"- Payment ID: {payment.payment_id}, Amount: {payment.payment_amount}, Status: {payment.status}")
                else:
                    st.write("No payments linked.")
                
                if ph.status == 'Active':
                    if st.button("Suspend Policyholder"):
                        ph.suspend()
                        st.success(f"Policyholder {ph.fname} {ph.lname} has been suspended.")
                else:
                    if st.button("Reactivate Policyholder"):
                        ph.reactivate()
                        st.success(f"Policyholder {ph.fname} {ph.lname} has been reactivated.")
    else:
        st.write("No policyholders registered yet.")

def manage_products():
    """Manage products."""
    st.subheader("Manage Products")
    
    product_id = st.text_input("Product ID")
    product_name = st.text_input("Product Name")
    product_price = st.number_input("Product Price", min_value=0.0)

    if st.button("Create Product"):
        new_product = Product_Management(product_id, product_name, product_price)
        st.session_state.products.append(new_product)
        st.success(f"Product {product_name} created successfully.")

    if st.session_state.products:
        st.write("Existing Products:")
        for product in st.session_state.products:
            st.write(f"ID: {product.product_id}, Name: {product.product_name}, Price: {product.product_price}, Status: {product.status}")
        
        selected_product_id = st.selectbox("Select Product ID to manage", [p.product_id for p in st.session_state.products])
        
        for product in st.session_state.products:
            if product.product_id == selected_product_id:
                if st.button("Update Product"):
                    new_name = st.text_input("New Product Name", value=product.product_name)
                    new_price = st.number_input("New Product Price", min_value=0.0, value=product.product_price)
                    product.update_product(new_name, new_price)
                    st.success(f"Product {selected_product_id} updated.")
                if st.button("Remove Product"):
                    product.remove_product()
                    st.success(f"Product {selected_product_id} removed.")

def create_payment():
    """Create a new payment for a policyholder."""
    st.subheader("Create a Payment")
    payment_id = st.text_input("Payment ID")
    payment_amount = st.number_input("Payment Amount", min_value=0.0)
    selected_policyholder_id = st.selectbox("Select Policyholder for Payment", [ph.policyholder_id for ph in st.session_state.policyholders])
    
    if st.button("Create Payment"):
        new_payment = Payment(payment_id, payment_amount)
        new_payment.process_payment()
        st.session_state.payments.append(new_payment)

        # Find the selected policyholder and add the payment to their list
        for ph in st.session_state.policyholders:
            if ph.policyholder_id == selected_policyholder_id:
                ph.add_payment(new_payment)
                st.success(f"Payment of {payment_amount} added to Policyholder {ph.fname} {ph.lname}.")


def payment_management():
    """View unpaid payments, send reminders, and apply penalties."""
    st.subheader("Manage Payments")
    
    if st.session_state.payments:
        st.write("Payments:")
        for payment in st.session_state.payments:
            st.write(f"ID: {payment.payment_id}, Amount: {payment.payment_amount}, Status: {payment.status}")
        
        selected_payment_id = st.selectbox("Select Payment ID", [p.payment_id for p in st.session_state.payments])
        selected_penalty_amount = st.number_input("Penalty Amount", min_value=0.0, step=0.01)

        for payment in st.session_state.payments:
            if payment.payment_id == selected_payment_id:
                if st.button("Send Reminder"):
                    reminder_message = payment.reminder()
                    st.info(reminder_message)
                
                if st.button("Apply Penalty"):
                    penalty_message = payment.penalty(selected_penalty_amount)
                    st.warning(penalty_message)
    else:
        st.write("No payments available.")

def main():
    st.title("Yaspi Insurance Management System")

    menu = ["Register Policyholder", "View Policyholders", "Manage Products", "Create Payment", "Manage Payments"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Register Policyholder":
        register_policyholder()
    elif choice == "View Policyholders":
        view_policyholders()
    elif choice == "Manage Products":
        manage_products()
    elif choice == "Create Payment":
        create_payment()
    elif choice == "Manage Payments":
        payment_management()

if __name__ == "__main__":
    main()
