import streamlit as st

def home():
    st.set_page_config(page_title="Sindhri Restaurant", layout="wide")

    st.title("Welcome to Sindhri Restaurant Sukkur")
   
    st.write("Sindhri Restaurant Sukkur offers the best dining experience in the heart of Sukkur. Our system allows you to manage the restaurant menu, place orders, and track customer orders efficiently.")
    st.write("Explore the system to manage your operations seamlessly.")
    
    # Add restaurant images
    st.image("https://i.ytimg.com/vi/VawqbvnQjs0/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAhXa-stiS_hyRcZnH44v0OGTjNvQ", caption="Sindhri Restaurant Sukkur", use_column_width=True)
    st.write("Use the sidebar to navigate through the system and manage your orders, menu, and more.")
    
    st.image("https://scontent.fkhi10-1.fna.fbcdn.net/v/t1.6435-9/96715368_1737278986395941_1027729195112857600_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=833d8c&_nc_ohc=g8icuG85O2oQ7kNvgHHQp3x&_nc_zt=23&_nc_ht=scontent.fkhi10-1.fna&_nc_gid=A_XwBWrKTSc4kboshKJMuP4&oh=00_AYBfHoKYzk_HicnXS0EGc5pilk-Axm0GGqVUGu9ni8gVfA&oe=67A95D64", caption="Sindhri Restaurant Sukkur", use_column_width=True)
   
    # Restaurant description text
    restaurant_description = """
    At **Sindhri Restaurant**, we pride ourselves on serving exquisite flavors from the heart of Sindh, bringing you a delightful culinary experience that celebrates the rich heritage of Pakistani cuisine. Our menu is carefully crafted to provide you with a perfect blend of traditional recipes and modern twists, ensuring every meal is a feast for the senses.

    **Signature Dishes:**
    - **Sindhri Biryani**: A mouth-watering, aromatic biryani prepared with the finest basmati rice, tender meat, and a rich mix of spices, topped with a fragrant blend of herbs.
    - **Karahi**: Our sizzling Karahi dishes, available in chicken, mutton, or beef, are cooked to perfection with fresh tomatoes, green chilies, and a special mix of Sindhi spices.
    - **Sindhri Seekh Kebabs**: Juicy and tender kebabs made from minced meat and marinated with a blend of spices, served with a side of naan or rice.
    - **Saag with Makki di Roti**: A traditional Sindhi dish made with fresh mustard greens, served with hot cornmeal flatbread.
    - **Sindhi Biryani**: A vibrant, flavorful biryani made with long-grain rice and a blend of fresh spices, bringing the unique taste of Sindh to your plate.

    **Specialty Drinks:**
    - **Fresh Mango Lassi**: A refreshing, sweet yogurt drink made with fresh mangoes, perfect to complement your meal.
    - **Rooh Afza**: A traditional, sweet, rose-flavored drink to cool you down on a hot day.

    **Desserts:**
    - **Sindhri Kulfi**: A rich, creamy, and delicious ice cream, perfect for ending your meal on a sweet note.
    - **Gulab Jamun**: Soft, melt-in-your-mouth dough balls soaked in sugar syrup, a sweet treat you’ll love.

    Our chefs are passionate about using only the finest ingredients, ensuring that each dish is prepared with the utmost care and authenticity. Whether you're here for a casual lunch, a family dinner, or a special occasion, Sindhri Restaurant promises a meal that you’ll savor and remember.

    **Experience the true taste of Sindh with every bite.**
    """

    # Display the restaurant description using markdown
    st.markdown(restaurant_description)

# Call the home function to display the content
home()
