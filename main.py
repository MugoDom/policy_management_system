# We create a streamlit app for the User Interface
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
    """View registered policyholders and manage their status."""
    st.subheader("Registered Policyholders")
    if st.session_state.policyholders:  # Check if there are any policyholders
        for ph in st.session_state.policyholders:
            st.write(f"ID: {ph.policyholder_id}, Name: {ph.fname} {ph.lname}, Status: {ph.status}")

        selected_id = st.selectbox("Select Policyholder ID to manage", [ph.policyholder_id for ph in st.session_state.policyholders])
        
        # Display the selected policyholder details and manage status
        for ph in st.session_state.policyholders:
            if ph.policyholder_id == selected_id:
                st.write(f"**ID:** {ph.policyholder_id}")
                st.write(f"**Name:** {ph.fname} {ph.lname}")
                st.write(f"**Email:** {ph.email}")
                st.write(f"**Address:** {ph.address}")
                st.write(f"**Status:** {ph.status}")
                
                # Suspend or Reactivate buttons
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
    
    # Create Product
    st.write("Create New Product")
    product_id = st.text_input("Product ID")
    product_name = st.text_input("Product Name")
    product_price = st.number_input("Product Price", min_value=0.0)

    if st.button("Create Product"):
        new_product = Product_Management(product_id, product_name, product_price)
        st.session_state.products.append(new_product)  # Add to session state
        st.success(f"Product {product_name} created successfully.")

    # List and manage existing products
    if st.session_state.products:
        st.write("Existing Products:")
        for product in st.session_state.products:
            st.write(f"ID: {product.product_id}, Name: {product.product_name}, Price: {product.product_price}, Status: {product.status}")
        
        selected_product_id = st.selectbox("Select Product ID to manage", [p.product_id for p in st.session_state.products])
        
        # Update or Remove Product
        for product in st.session_state.products:
            if product.product_id == selected_product_id:
                if st.button("Update Product"):
                    new_name = st.text_input("New Product Name", value=product.product_name)
                    new_price = st.number_input("New Product Price", min_value=0.0, value=product.product_price)
                    product.update_product(new_name, new_price)
                    st.success(f"Product {selected_product_id} updated to {new_name} at price {new_price}.")
                if st.button("Remove Product"):
                    product.remove_product()
                    st.success(f"Product {selected_product_id} has been removed.")

def create_payment():
    """Create a new payment for a policyholder."""
    st.subheader("Create a Payment")
    payment_id = st.text_input("Payment ID")
    payment_amount = st.number_input("Payment Amount", min_value=0.0)
    selected_policyholder_id = st.selectbox("Select Policyholder for Payment", [ph.policyholder_id for ph in st.session_state.policyholders])
    
    if st.button("Create Payment"):
        new_payment = Payment(payment_id, payment_amount)
        new_payment.process_payment()
        st.session_state.payments.append(new_payment)  # Add to session state
        st.success(f"Payment ID: {payment_id} created successfully for {selected_policyholder_id}.")

def main():
    st.title("Insurance Policy Management System")

    menu = ["Register Policyholder", "View Policyholders", "Manage Products", "Create Payment"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Register Policyholder":
        register_policyholder()
    elif choice == "View Policyholders":
        view_policyholders()
    elif choice == "Manage Products":
        manage_products()
    elif choice == "Create Payment":
        create_payment()

if __name__ == "__main__":
    main()
