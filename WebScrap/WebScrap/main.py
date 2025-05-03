import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("🔍 GitHub Profile Image Finder")

# Input GitHub username
username = st.text_input("Enter GitHub username")

if username:
    url = f"https://github.com/{username}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find profile image
        profile_img_tag = soup.find('img', {'class': 'avatar-user'})

        if profile_img_tag:
            profile_image = profile_img_tag['src']
            
            # Check if the image URL is relative (GitHub uses relative URLs sometimes)
            if profile_image.startswith("//"):
                profile_image = "https:" + profile_image

            st.success("Profile Image Found!")
            st.image(profile_image, width=150)  # Displaying the image
            st.write(f"**Profile Image URL:** {profile_image}")
        else:
            st.error("❌ Profile image not found. GitHub HTML structure might have changed.")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
