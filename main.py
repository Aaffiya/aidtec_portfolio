import streamlit as st
import requests

# Define your GitHub repository URL and image directory
github_repo_url = "https://raw.githubusercontent.com/yourusername/your-repo/master/"
image_directory = "images/"

# Create a dictionary with image filenames and descriptions
image_info = {
    "logo.jpg": "Logo Design - This is a description of the logo design.",
    "banner.jpg": "Banner Design - This is a description of the banner design.",
    "food_menu.jpg": "Food Menu - This is a description of the food menu.",
    "book_cover.jpg": "Book Cover Design - This is a description of the book cover design.",
}

st.title("Portfolio Website")

# Create a slider to navigate through images
selected_image = st.selectbox("Select an Image", list(image_info.keys()))

# Display the selected image
st.image(github_repo_url + image_directory + selected_image, use_column_width=True)

# Retrieve image description from the dictionary
image_description = image_info[selected_image]

# Display the image description
st.write(f"**Description:** {image_description}")

# You can add more animations or interactivity as needed using Streamlit components
