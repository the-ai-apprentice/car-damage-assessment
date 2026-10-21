import streamlit as st

def apply_custom_css():
    custom_css = """
    <style>
        /* Fix the white strip at the top (Streamlit's default header) */
        header[data-testid="stHeader"] {
            background-color: transparent !important;
        }

        /* Hide the sidebar collapse/expand button (Targets both old and new Streamlit versions) */
        [data-testid="collapsedControl"],
        [data-testid="stSidebarCollapseButton"] {
            display: none !important;
        }
        
        /* Global Text Color Fix for Dark Theme */
        .stApp, .stApp p, .stApp span, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6, .stApp label {
            color: #E2E8F0 !important;
        }

        /* Main app background color */
        .stApp {
            background-color: #111823 !important;
        }

        /* Sidebar background color & text */
        [data-testid="stSidebar"] {
            background-color: #1E2837 !important;
            border-right: 1px solid #2d3748 !important;
        }
        
        [data-testid="stSidebar"] * {
            color: #E2E8F0 !important;
        }

        /* File Uploader styling - fixing the white box */
        [data-testid="stFileUploader"] section {
            background-color: #1A2230 !important;
            color: #E2E8F0 !important;
        }
        
        [data-testid="stFileUploadDropzone"] {
            background-color: #1A2230 !important;
            border: 1px dashed #4B5563 !important;
            border-radius: 8px !important;
        }
        
        [data-testid="stFileUploadDropzone"]:hover {
            border-color: #00d2ff !important;
        }
        
        /* Ensure uploader text is visible */
        [data-testid="stFileUploadDropzone"] div, [data-testid="stFileUploadDropzone"] span {
            color: #A0AEC0 !important;
        }

        /* Base styling for Metric containers - Reduced padding to shrink the box */
        div[data-testid="stMetric"] {
            background-color: #111823 !important;
            padding: 8px 12px !important; /* Reduced padding */
            border-radius: 12px !important;
            min-height: 60px !important; /* Reduced min-height */
        }

        /* Left Column (Predicted Class) - Blue glowing border */
        div[data-testid="stHorizontalBlock"] > div:nth-child(1) div[data-testid="stMetric"] {
            border: 2px solid #00a8ff !important;
            box-shadow: 0 0 12px rgba(0, 168, 255, 0.15) !important;
        }

        /* Right Column (Damage Condition) - Green glowing border */
        div[data-testid="stHorizontalBlock"] > div:nth-child(2) div[data-testid="stMetric"] {
            border: 2px solid #00E676 !important;
            box-shadow: 0 0 12px rgba(0, 230, 118, 0.15) !important;
        }

        /* Formatting the Metric Label */
        [data-testid="stMetricLabel"] * {
            color: #A0AEC0 !important;
            font-size: 11px !important; /* Reduced font size */
            font-weight: 500 !important;
            padding-bottom: 0px !important; /* Reduced padding */
        }
        
        /* Formatting the Metric Value */
        [data-testid="stMetricValue"] div {
            color: #FFFFFF !important;
            font-size: 20px !important; /* Reduced font size */
            font-weight: 700 !important;
            line-height: 1.1 !important;
        }       
        
        /* Style the progress bar to match the new color theme */
        [data-testid="stProgressBar"] div[role="progressbar"] > div {
            background-color: #00E676 !important; /* Replace #00a8ff with your desired hex color */
        }
        
        /* Sidebar bottom card styling (Model details) */
        .sidebar-card {
            background-color: #111823 !important;
            padding: 15px !important;
            border-radius: 8px !important;
            border: 1px solid #2d3748 !important;
            margin-top: 20px !important;
            color: #E2E8F0 !important;
        }
        /* Enable absolute positioning context for the sidebar */
        [data-testid="stSidebar"] {
            position: relative !important;
        }
        
        /* Pin Sidebar bottom card styling to the bottom */
        .sidebar-card {
            background-color: #111823 !important;
            padding: 15px !important;
            border-radius: 8px !important;
            border: 1px solid #2d3748 !important;
            margin-top: 300px !important; /* Pushes the card down naturally */
            color: #E2E8F0 !important;
        }

        /* Round the corners of the uploaded image to match design */
        [data-testid="stImage"] img {
            border-radius: 12px;
        }
        /* Reduce the top padding of the main layout container */
        .block-container {
            padding-top: 0rem !important;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)