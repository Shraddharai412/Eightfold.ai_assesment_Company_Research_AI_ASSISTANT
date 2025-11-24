# ui/theme.py
import streamlit as st

def inject_theme():
    st.markdown("""
    <style>

    /*  GLOBAL BACKGROUND */
    body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #eef2f3, #dfe9f3);
    }

    /*  HEADER  */
    .assistant-title {
        font-size: 38px;
        font-weight: 800;
        color: #1F2937;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 5px;
        animation: fadeIn 1s ease-in-out;
    }

    /* INPUT BOX */
    input[type="text"] {
        background: white !important;
        color: #1F2937 !important;
        border-radius: 12px !important;
        border: 1px solid #d1d5db !important;
        padding: 14px !important;
        font-size: 16px !important;
    }

    /*  BUTTON  */
    button[kind="primary"] {
        background: #2563eb !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 10px 24px !important;
        font-size: 16px !important;
        border: none !important;
    }
    button[kind="primary"]:hover {
        background: #1d4ed8 !important;
    }

    /*  CHAT BUBBLES  */
    .user-bubble {
        background: #dbeafe;
        color: #1e3a8a;
        padding: 12px;
        border-radius: 16px;
        max-width: 80%;
        margin-left: auto;
        margin-bottom: 8px;
        animation: fadeInUp 0.4s ease-out;
    }
                

    .ai-bubble {
        background: white;
        color: #111827;
        padding: 12px;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
        max-width: 80%;
        margin-right: auto;
        margin-bottom: 8px;
        animation: fadeInUp 0.4s ease-out;
    }

    /*  SIDEBAR */
    [data-testid="stSidebar"] {
        background: #0f172a;
        padding: 20px;
    }

    .sidebar-card {
        background: rgba(255,255,255,0.05);
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 14px;
        color: #e2e8f0;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .sidebar-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 10px;
        color: #f8fafc;
    }
                

    /*  ANIMATIONS  */
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    @keyframes fadeInUp {
        from {opacity: 0; transform: translateY(12px);}
        to {opacity: 1; transform: translateY(0);}
    }
                
    

    </style>
    """, unsafe_allow_html=True)
