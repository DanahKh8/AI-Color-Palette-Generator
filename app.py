import streamlit as st
import numpy as np
import cv2
from sklearn.cluster import KMeans
from collections import Counter

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Color Palette Generator", page_icon="🎨")

# --- HEADER ---
st.title("AI Color Palette Generator")
st.write("Upload an image to extract its aesthetic color scheme using **Machine Learning**.")

# --- SIDEBAR CONFIG ---
with st.sidebar:
    st.header("Settings")
    number_of_colors = st.slider("Number of Colors", min_value=3, max_value=10, value=5)
    st.markdown("---")
    st.caption("Created by Danah | Creative Technologist")

# --- HELPER FUNCTIONS ---
def get_image(image_file):
    # Convert the uploaded file into an OpenCV image
    file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

# --- MAIN APP ---
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 1. Display Original Image
    image = get_image(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    # 2. Process with Loading Spinner
    with st.spinner("AI is extracting aesthetic colors..."):
        # Resize for speed (optional)
        modified_image = cv2.resize(image, (600, 400), interpolation=cv2.INTER_AREA)
        modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)

        # K-Means Clustering
        clf = KMeans(n_clusters=number_of_colors)
        labels = clf.fit_predict(modified_image)
        
        counts = Counter(labels)
        center_colors = clf.cluster_centers_

        # Order by frequency
        ordered_colors = [center_colors[i] for i in counts.keys()]
        hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]

    # 3. Display Results
    st.success("Palette Extracted!")
    
    # Create columns to display colors side-by-side
    cols = st.columns(number_of_colors)
    for i, col in enumerate(cols):
        with col:
            # Display color block and hex code
            st.color_picker(f"Color {i+1}", hex_colors[i], disabled=True, key=i)
            st.code(hex_colors[i], language="text")

else:
    st.info("Please upload an image to start!")