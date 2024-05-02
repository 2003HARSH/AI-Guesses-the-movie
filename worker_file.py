from langchain.llms import GooglePalm
from langchain.embeddings import GooglePalmEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS



def get_qa_chain(GOOGLEPALM_API_KEY):

    llm=GooglePalm(google_api_key=GOOGLEPALM_API_KEY,temperature=0)

    embeddings=GooglePalmEmbeddings(google_api_key=GOOGLEPALM_API_KEY)

    vectordb=FAISS.load_local('vectordb',embeddings)
    
    retriever=vectordb.as_retriever()

    prompt_template = """Given the following context and a question, give the movie title from the context.
    If the movie title is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    chain_type_kwargs = {"prompt": PROMPT}

    chain = RetrievalQA.from_chain_type(llm=llm,
                                          chain_type='stuff',
                                          retriever=retriever,
                                          return_source_documents=True,
                                          chain_type_kwargs={"prompt":PROMPT})
    
    return chain


    


