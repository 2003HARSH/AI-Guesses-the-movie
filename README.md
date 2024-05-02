# Movie Name Guessing using Plot with RAG

This project is a Retrieval-Augmented Generation (RAG) application that can guess a movie's name based on a given plot summary. The application is built using LangChain, Google Palm LLM, CSVLoader, RetrievalQA, Google Palm Embeddings, and FAISS, and it is deployed on Streamlit for a user-friendly interface.

## Features

- **Plot-based Movie Guessing**: Provide a plot summary, and the application will guess the corresponding movie title.
- **AI-Powered Retrieval**: The application uses advanced AI models and embedding techniques to find the most relevant matches quickly.
- **Interactive Streamlit Interface**: The application is deployed on Streamlit, offering a simple and interactive user experience.

## Technologies Used

- **LangChain**: A framework for building AI applications that combine large language models (LLMs) with custom data sources.
- **Google Palm LLM**: A powerful large language model that processes text and provides accurate interpretations.
- **CSVLoader**: Loads the movie database from CSV files.
- **RetrievalQA**: Retrieves relevant data from the loaded dataset for question-answering tasks.
- **Google Palm Embeddings**: Creates efficient embeddings for text data.
- **FAISS**: A library for fast similarity search and clustering of dense vectors.

## Getting Started

To run the application, you'll need to follow these steps:

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/2003HARSH/AI-Guesses-the-movie.git]
   cd [AI-Guesses-the-movie]
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Environment**
   Ensure you have the necessary environment variables configured, such as API keys for Google Palm LLM and any other services used.

4. **Start the Streamlit App**
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Enter a Plot Summary**
   Input the plot summary for a movie into the provided text box.

2. **Generate Movie Name**
   Click the "Guess Movie" button to get the predicted movie name based on the provided plot.

3. **Review Results**
   The application will return the most likely movie name and additional information, if available.

## Contributions

Contributions are welcome! If you have ideas for improvements or new features, feel free to submit a pull request or open an issue. Please ensure your code follows the project's coding standards and is well-documented.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

Thanks to the developers of LangChain, Google Palm, FAISS, and Streamlit for providing the tools and libraries that made this project possible.
