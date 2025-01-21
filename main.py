
import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Set up Streamlit app layout and styling
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="💼", layout="centered")

# Custom CSS for a vibrant and colorful UI
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #f6d365, #fda085); /* Warm gradient */
        color: #333;
    }
    .title {
        font-size: 3em;
        font-weight: bold;
        color: #FFFFFF; /* White text for contrast */
        text-align: center;
        margin-bottom: 20px;
        font-family: 'Verdana', sans-serif;
        animation: fadeInZoom 1.5s ease;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2); /* Subtle shadow */
    }
    .dropdown-label {
        font-weight: bold;
        font-size: 1.1em;
        color: #FFFFFF; /* White for dropdown labels */
        margin-top: 15px;
        display: block;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }
    .generate-button {
        width: 100%;
        background: linear-gradient(90deg, #6a11cb, #2575fc); /* Vibrant gradient */
        color: white;
        font-size: 1.4em;
        font-weight: bold;
        padding: 12px;
        border: none;
        border-radius: 15px;
        cursor: pointer;
        margin-top: 25px;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3); /* Hover effect shadow */
    }
    .generate-button:hover {
        background: linear-gradient(90deg, #2575fc, #6a11cb); /* Reversed gradient */
        transform: scale(1.05); /* Slightly larger on hover */
    }
    .generated-post {
        background: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 15px;
        margin-top: 30px;
        border: 2px solid #fda085; /* Matching accent color */
        font-size: 1.2em;
        color: #333;
        font-family: 'Courier New', Courier, monospace;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1); /* Soft shadow */
        animation: fadeInSlideUp 1s ease;
    }
    @keyframes fadeInZoom {
        from { opacity: 0; transform: scale(0.8); }
        to { opacity: 1; transform: scale(1); }
    }
    @keyframes fadeInSlideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Function
def main():
    # Display vibrant title
    st.markdown('<div class="title">🚀 LinkedIn Post Generator 📱</div>', unsafe_allow_html=True)

    # Initialize FewShotPosts for data
    fs = FewShotPosts()
    tags = fs.get_tags()

    # Dropdown for Topic (Tags)
    st.markdown('<label class="dropdown-label">🌟 Choose a Topic</label>', unsafe_allow_html=True)
    selected_tag = st.selectbox("", options=tags, key="tag")

    # Dropdown for Length
    st.markdown('<label class="dropdown-label">📏 Select Length</label>', unsafe_allow_html=True)
    selected_length = st.selectbox("", options=["Short", "Medium", "Long"], key="length")

    # Dropdown for Language
    st.markdown('<label class="dropdown-label">🌐 Choose Language</label>', unsafe_allow_html=True)
    selected_language = st.selectbox("", options=["English", "Hinglish"], key="language")

    # Dropdown for Tone
    st.markdown('<label class="dropdown-label">🎨 Select Tone</label>', unsafe_allow_html=True)
    selected_tone = st.selectbox("", options=["Casual", "Professional", "Friendly"], key="tone")

    # Generate Button
    if st.button("💡 Generate Post ✨", key="generate", use_container_width=True):
        with st.spinner("Generating your post... 🎉"):
            post = generate_post(selected_length, selected_language, selected_tag, selected_tone)
        st.markdown('<div class="generated-post">' + post + '</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

