import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from io import BytesIO


def render_header():
    col, _ = st.columns([1, 0.0001])   # keep header on right page only

    with col:
        st.markdown("<div style='text-align:center; margin-top:10px;'>", unsafe_allow_html=True)

        st.image("ui/assets/bot_avatar.png", width=140)

        st.markdown(
            """
            <h1 style="
                text-align:center;
                font-size: 36px;
                font-weight: 800;
                color: #000000;
                margin-top: 5px;
            ">
                AI Company Research Assistant
            </h1>
            """,
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)



def render_chat(messages):
    for sender, msg in messages:
        if sender == "user":
            st.markdown(f"<div class='user-bubble'>{msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='ai-bubble'>{msg}</div>", unsafe_allow_html=True)



# ------------------------------------------------------------------------
# 📄  PDF EXPORT FUNCTION  (NEW)
# ------------------------------------------------------------------------
def generate_pdf(plan: dict):
    """
    Convert account plan dictionary into a downloadable PDF.
    """

    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    title_style = styles["Heading1"]
    section_title_style = styles["Heading2"]
    body_style = styles["BodyText"]

    # PDF Title
    story.append(Paragraph("Account Plan", title_style))
    story.append(Spacer(1, 0.3 * inch))

    # Add all sections
    for section, content in plan.items():
        story.append(Paragraph(section.replace("_", " "), section_title_style))
        story.append(Spacer(1, 0.1 * inch))

        if not content:
            content = "No content available."

        story.append(Paragraph(content.replace("\n", "<br/>"), body_style))
        story.append(Spacer(1, 0.3 * inch))

    pdf.build(story)
    buffer.seek(0)
    return buffer


def render_pdf_download(plan):
    """
    Creates a Streamlit download button for exporting PDF.
    """
    if plan:
        pdf_bytes = generate_pdf(plan)
        st.download_button(
            label="📄 Download Account Plan (PDF)",
            data=pdf_bytes,
            file_name="Account_Plan.pdf",
            mime="application/pdf"
        )



# ------------------------------------------------------------------------
# SIDEBAR PLAN + PDF EXPORT BUTTON
# ------------------------------------------------------------------------
def render_sidebar_plan(plan):
    if not plan:
        st.markdown(
            "<div class='sidebar-card'><div class='sidebar-title'>Account Plan</div>No plan generated yet.</div>",
            unsafe_allow_html=True
        )
        return

    st.markdown("<div class='sidebar-title'> Account Plan</div>", unsafe_allow_html=True)

    # PDF Button Added Here
    render_pdf_download(plan)

    for section, content in plan.items():
        st.markdown(f"""
            <div class="sidebar-card">
                <div class="sidebar-title">{section.replace('_',' ')}</div>
                {content}
            </div>
        """, unsafe_allow_html=True)

