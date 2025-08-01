import os
import streamlit as st 
from dotenv  import load_dotenv
load_dotenv()

import google.generativeai as genai

from PIL import Image #pillow image used to load,save and manipulate image 

st.set_page_config(page_title='Defect Detection', page_icon='🕵',layout='wide')

st.title('Ai assistant for :green[Structural defect and analysis]')
st.subheader(':blue[prototype for automated structural defect analysis]',divider=True)

with st.expander('about the application:'):
    st.markdown(f''' This prototype is used to detect the structural defects
                and analyse the defects using ai powered systems.
                - **Defect Detection** : Automatically detects the structural defects in the given image
                - **Recommendations** : Provide solution and recommendations based on defects
                - **Report Generation** : create a detailed report for the documentation
                ''')
    
key= os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

st.subheader('upload image here')
input_image= st.file_uploader('upload image here',type=['png','jpg','jpeg'])

if input_image:
    img= Image.open(input_image)
    st.image(img, caption='uploaded image')
    
prompt= f''' 
    1. By looking at the image label what are the things visible. 
    2. what is visible scenario as per image.is there any person or any animals?
    3. provide details to the image as per its perpestive. 
    4. if image has an event specify what kind of event?.
    5. is this image an positive or negative scenario.
    6. is this image clear or it is broken or damaged.
    7. is this image clearly visible.
    8. is the defects shown in image
    9. what is the probability in percentage is image having defects 
    10.what are possibilites for teh defects to happen again 
    '''
    
model = genai.GenerativeModel('gemini-2.0-flash')

def generative_results(prompt,input_image):
    result = model.generate_content(f''' Using the given prompt {prompt} analyze
                                    the given image {img} and generative the results based
                                    on the prompt ''')
    
    return result.text

submit = st.button('Analyze the defect')

if submit:
    with st.spinner('Analyzing...... '):
        response = generative_results(prompt,img) 
        
        st.markdown('## :green[Result]')
        st.write(response)