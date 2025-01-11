import streamlit as st
import pandas as pd
import os

# File paths for the CSV files
MENU_DB_PATH = 'menu_data.csv'
ORDER_DB_PATH = 'orders_data.csv'

# Initialize the CSV files if they don't exist
def init_csv_files():
    if not os.path.exists(MENU_DB_PATH):
        pd.DataFrame(columns=['Dish Name', 'Price']).to_csv(MENU_DB_PATH, index=False)
    
    if not os.path.exists(ORDER_DB_PATH):
        pd.DataFrame(columns=['Order ID', 'Username', 'Dish Name', 'Quantity', 'Order Status']).to_csv(ORDER_DB_PATH, index=False)

# Function to add a new menu item
def add_menu_item(dish_name, price):
    menu = pd.read_csv(MENU_DB_PATH)
    new_item = pd.DataFrame({'Dish Name': [dish_name], 'Price': [price]})
    menu = pd.concat([menu, new_item], ignore_index=True)
    menu.to_csv(MENU_DB_PATH, index=False)

# Function to place a new order
def place_order(username, dish_name, quantity):
    orders = pd.read_csv(ORDER_DB_PATH)
    order_id = len(orders) + 1
    order_status = "Pending"  # New order status
    new_order = pd.DataFrame({'Order ID': [order_id], 'Username': [username], 'Dish Name': [dish_name], 'Quantity': [quantity], 'Order Status': [order_status]})
    orders = pd.concat([orders, new_order], ignore_index=True)
    orders.to_csv(ORDER_DB_PATH, index=False)
    return order_id, dish_name, quantity, order_status

# Function to view user's orders
def view_orders(username):
    orders = pd.read_csv(ORDER_DB_PATH)
    user_orders = orders[orders['Username'] == username]
    if not user_orders.empty:
        st.write(user_orders)
    else:
        st.write("No orders found.")

# Function to manage the restaurant system
def restaurant_management(username):
    init_csv_files()

    st.title(f"Restaurant Management System - Welcome {username}")
    
    # Load the menu and display it
    menu = pd.read_csv(MENU_DB_PATH)
    menu_dishes = menu['Dish Name'].tolist()

    # Menu Management Section
    st.subheader("Menu Management")
    st.write(menu)

    with st.form(key='menu_form'):
        dish_name = st.text_input("Dish Name")
        price = st.number_input("Price", min_value=0.01, step=0.01)
        submit_menu = st.form_submit_button("Add Dish")
        
        if submit_menu and dish_name and price:
            add_menu_item(dish_name, price)
            st.success(f"Dish '{dish_name}' added to the menu.")
            # Reload the menu to show the newly added dish
            menu = pd.read_csv(MENU_DB_PATH)
            menu_dishes = menu['Dish Name'].tolist()

    # Order Management Section
    st.subheader("Place an Order")
    if menu_dishes:
        dish_to_order = st.selectbox("Select a Dish", menu_dishes)
        quantity = st.number_input("Quantity", min_value=1, step=1)
    
        if st.button("Place Order"):
            order_id, dish_name, quantity, order_status = place_order(username, dish_to_order, quantity)
            st.success(f"Order placed successfully: {quantity}x {dish_name}")
            st.write(f"Order ID: {order_id}, Dish: {dish_name}, Quantity: {quantity}, Status: {order_status}")

            # Redirect to Order Confirmation Page (optional)
            st.subheader("Order Confirmation")
            st.write(f"Your order has been placed. Here are your order details:")
            st.write(f"Order ID: {order_id}")
            st.write(f"Dish: {dish_name}")
            st.write(f"Quantity: {quantity}")
            st.write(f"Order Status: {order_status}")

            # Display all orders
            st.subheader("View Your Orders")
            view_orders(username)
    else:
        st.warning("No dishes available in the menu. Please add some dishes first.")

    # View Orders Section
    st.subheader("View Your Orders")
    view_orders(username)
if 'username' in st.session_state:
    restaurant_management(st.session_state.username)
else:
    st.warning("Please log in first to access the restaurant management system.")
