import streamlit as st
st.set_page_config(layout="wide")
import os
from streamlit_extras.add_vertical_space import add_vertical_space
from dataclasses import dataclass
from tools.excel_agent_old import excel_llm_agent
# Set the title for the Streamlit app
# Create a file uploader in the sidebar
from langchain.callbacks.base import BaseCallbackHandler
import pandas as pd
import openai
from tools.viz_plotly import get_primer,format_question,run_request
import warnings
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport
import plotly.graph_objects as go
import plotly.express as px


warnings.filterwarnings("ignore")

with st.sidebar:
    st.image("images\PwC.png")  
    # open_ai_api = st.text_input('Open AI API', 'Enter your open AI API key')
    # if not open_ai_api.startswith('sk-'):
    #             st.error("Please enter a valid OpenAI API key.")
    #             api_keys_entered = False

    report_on = st.toggle("Automated Report")
    chat_on = st.toggle("NLQ")
    visualize = st.toggle("Custom Visualization")


    
def main():


    st.title("Data Explorer")

    # c1,c2= st.columns(2)
    # with c1:
    #     uploaded_files_ex = st.file_uploader("Upload Excel files", accept_multiple_files=True)
    # with c2:
    #     uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)
    
    # c1= st.columns(1)
    # with c1:
    uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)
    # with c2:
    #     uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)

    
    dataframes = []  
    file_list  = []

    if uploaded_files is not None:
        for file in uploaded_files:
            file_list.append(file.name)
        for uploaded_file in uploaded_files:
            try:
                dataframe = pd.read_csv(uploaded_file)
                dataframes.append(dataframe)  # Append DataFrame to the list
            except Exception as e:
                dataframe = pd.read_csv(uploaded_file,encoding='latin1')
                dataframes.append(dataframe)

    # if uploaded_files_ex is not None:
    #     for file in uploaded_files_ex:
    #         file_list.append(file.name)

    #     for uploaded_file in uploaded_files_ex:
    #         st.write("filename:", uploaded_file.name)
    #         try:
    #             dataframe = pd.read_excel(uploaded_file)
    #             dataframes.append(dataframe)  # Append DataFrame to the list
    #         except Exception as e:
    #             st.write("error")
    
    if uploaded_files is not None:
        selected_files = st.multiselect("Select Tables", file_list)
        
        # if selected_files:
        #     for selected_file in selected_files:
        #         index = file_list.index(selected_file)
        #         st.write(f"Displaying dataframe for **{selected_file}**")
        #         st.dataframe(dataframes[index],use_container_width = True)



        # if report_on:
        #         for selected_file in selected_files:
        #             index = file_list.index(selected_file)
        #             st.header(f"Displaying report for **{selected_file}**")
        #             profile = ProfileReport(dataframes[index], title= f"EDA Report **{selected_file}**", explorative = True)
        #             st_profile_report(profile)
            
        
        if chat_on:
                prompt = st.chat_input("Chat with your Data")
                # system_prompt  = """
                # never give the user code as an answer, always run the scripts multiple times to provide an answer
                # to the user.
                #  For few question you only need to refrase or understand the question as follow:-
                #  - Question-Show me Sales Performance by country-> Rephrased Question : Show me actual sales, Budget, LE, by country 
               
                
                # Finally- if from the result you can draw insight that would be helpfull and while giving insight start with the keyword Remark-"""
                system_prompt ="""

                    1. Code Execution:
                    - Never provide code directly to the user.
                    - Always execute scripts multiple times to generate accurate and consistent results.
                    - Present only the final output or analysis to the user.

                    2. Question Interpretation:
                    - For certain questions, rephrase or expand the query to ensure comprehensive answers:
                        Example1: 
                        User: "Show me Sales Performance by country"
                        Interpreted as: "Show me actual sales, Budget, LE (Latest Estimate), by country"
                        Example 2:
                        User:"Show me market share percentage for DRL for Russia for each brand wise"
                        Interpreted as: -Filter data on the country = Russia
                                        - Group by Product and calculate total DRL Sales and Market Sales
                                        - Calculate the market share percentage for each product
                                        - Finally map each product with their brand name

                    3. Data Presentation:
                    - Present results in a clear, organized manner.
                    - Use tables, bullet points, or other formatting as appropriate to enhance readability.

                    4. Insights:
                    - After presenting the data, provide valuable insights when possible.
                    - Begin each insight with the keyword "Remark:"
                    - Focus on trends, anomalies, or noteworthy patterns in the data.

                    Remember to maintain a professional and helpful tone throughout the interaction.

                    """
                if prompt:

                    final_prompt = prompt + system_prompt
                    selected_dataframes = [dataframes[file_list.index(file)] for file in selected_files]
                    result  = excel_llm_agent(selected_dataframes,final_prompt,open_ai_api)
                    st.write(f'**{prompt}**')
                    with st.expander("View Intermediate Steps"):
                        result["intermediate_steps"]       
                    st.write(result["output"])

        if visualize:
                st.header("Natural Language Visualization")
                selected_file_1 = st.selectbox("Select a table",file_list)
                index = file_list.index(selected_file_1)
                st.write(f"Displaying dataframe for **{selected_file_1}**")
                st.dataframe(dataframes[index],use_container_width = True)
                data_viz = dataframes[index]
                question = st.text_area(":eyes: What would you like to visualise?",height=10)
                
                if question:                
                    primer1,primer2 = get_primer(data_viz,'data_viz') 
                    model_type = "gpt-4"
                    question_to_ask = format_question(primer1, primer2, question, model_type)   
                    answer=""                             
                    answer = run_request(question_to_ask,"gpt-4", key=open_ai_api,alt_key=" ")
                    with st.expander("View Code"):
                        st.code(answer, language="python", line_numbers=False)
                    
                    plot_area = st.empty()
                    
                    local_vars = {}
                    exec(answer, globals(), local_vars)

                    create_plotly_figure = local_vars['create_plotly_figure']

                    fig = create_plotly_figure(data_viz)                                 

                    plot_area.plotly_chart(fig, use_container_width=True)
               
                

               
    
                    
if __name__=="__main__":
    main()
