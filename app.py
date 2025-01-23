import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_study import page_study_body
from app_pages.page_predicted import page_predicted_body
from app_pages.page_hypothesis import page_hypothesis_body
from app_pages.page_model import page_model_body

app = MultiPage(app_name="Ames-Price-Predictor")

# Add your app pages here using .add_page()
app.add_page("Project Summary", page_summary_body)
app.add_page("Housing Prices Study", page_study_body)
app.add_page("Predicted House Value", page_predicted_body)
app.add_page("Project Hypothesis", page_hypothesis_body)
app.add_page("Predictive Model", page_model_body)

app.run()
