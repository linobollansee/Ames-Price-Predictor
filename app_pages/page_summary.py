import streamlit as st


def page_summary_body():
    """
    This function generates the content for a summary page
    """
    st.info(
        f"Our client has acquired four residential properties in Ames, Iowa, "
        f"through inheritance and engaged our services to maximize their "
        f"market value. To accomplish this, we implemented advanced Machine "
        f"Learning methodologies and regression analysis to deliver accurate "
        f"and reliable pricing estimates for the properties."
        )
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* **Inheritance**: The process by which a person receives assets, "
        f"such as property or money, from someone who has passed away. In "
        f"this case, Lydia receives houses from her great-grandfather.\n"
        f"* **Appraisals**: The act of estimating the value of a property or "
        f"asset, typically carried out by a professional.\n"
        f"* **Maximise**: To increase something to its highest possible "
        f"level. In this context, it means getting the highest possible sales "
        f"price for the properties.\n"
        f"* **Data Practitioner**: A professional who works with data, often "
        f"performing tasks like data analysis, modeling, and visualization. "
        f"In this case, it refers to someone skilled in using data to predict "
        f"property values.\n"
        f"* **Predicting**: Estimating or forecasting the value or outcome of "
        f"something based on existing data or trends.\n"
        f"* **Attributes**: Characteristics or features of an object, like a "
        f"house. For example, attributes might include square footage, "
        f"quality, or number of bedrooms.\n"
        f"* **Correlate**: To establish a relationship or connection between "
        f"two or more variables. For example, the client wants to see how "
        f"certain attributes of a house (e.g., square footage, quality, or "
        f"number of bedrooms) correlate with its sale price.\n"
        f"* **Data Visualisations**: Graphical representations of data, such "
        f"as charts or graphs, used to illustrate trends, patterns, or "
        f"relationships in the data.\n"
        f"* **Dashboard**: A user interface that displays key information, "
        f"often through visualizations like graphs, charts, or tables, in a "
        f"clear and interactive way."
        )
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/linobollansee/Ames-Price-Predictor/blob/main/README.md).")
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how the house "
        f"attributes correlate with the sale price. Therefore, the client "
        f"expects data visualisations of the correlated variables against the "
        f"sale price to show that.\n"
        f"* 2 - The client is interested in predicting the house sales price "
        f"from her four inherited houses, and any other house in Ames, Iowa."
        )
