{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # portopal.py\
import streamlit as st\
import openai\
import os\
\
openai.api_key = st.secrets["OPENAI_API_KEY"]\
\
st.title("PortoPal: Moving to Portugal Made Simple")\
st.write("Ask me anything about relocating from the U.S. to Portugal!")\
\
# Capture user input\
user_input = st.text_input("What do you need help with?")\
\
# Make API call\
if user_input:\
    with st.spinner("Thinking..."):\
        response = openai.ChatCompletion.create(\
            model="gpt-3.5-turbo",\
            messages=[\
                \{"role": "system", "content": "You are a friendly relocation assistant that helps Americans move to Portugal."\},\
                \{"role": "user", "content": user_input\}\
            ]\
        )\
        st.success(response['choices'][0]['message']['content'])}