import streamlit as st
from worker_file import get_qa_chain

GOOGLEPALM_API_KEY=st.secrets['auth_token']
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_PROJECT']='ai-guesses-the-movie'
LANGCHAIN_API-KEY=st.secrets['langchain_key']

st.set_page_config(page_icon='🎬',
                   page_title="AI guesses the movie",                  
)

st.header('Can You Beat the Movie-Knowing Machine?')
st.write('Give a plot of any Bollywood movie🎦🍿 and it will guess which movie it is 😊')

plot=st.text_area(label='Plot:')

if st.button('Guess'):
    if plot:
        try:
            chain=get_qa_chain(GOOGLEPALM_API_KEY)
            response=chain(plot)
            st.header('Movie Name :')
            st.header(response['result'])
        except Exception as e:
            st.header('Sorry! I don\'t know 🥺')
            
