# Wikipedia Search Application

# Overview

The Wikipedia Search Application is a simple and user-friendly web application built with Streamlit. It allows users to search for content on Wikipedia by entering a query. The application leverages the LangChain WikipediaLoader to fetch and display relevant articles from Wikipedia. Additionally, it supports query translation using the Google Translator API, enabling multilingual search functionality.

# Features

Multilingual Query Support: Users can input queries in any language, which are automatically translated to English for Wikipedia search.

Efficient Wikipedia Content Fetching: Uses the LangChain WikipediaLoader to fetch up to three relevant Wikipedia articles.

Streamlined Content Display: Combines content from multiple articles and displays it in a clean format.

Error Handling: Handles errors gracefully, including translation failures and Wikipedia search issues.

# Technologies Used

Streamlit: For building the web application interface.

LangChain: For loading and processing Wikipedia articles.

Deep Translator (Google Translator API): For automatic query translation.

# Installation

To run the project locally, follow these steps:



1.Clone the repository:

git clone https://github.com/KaanSezen1923/Wikipedia-Search.git 
cd wikipedia-search-app

2.Create and activate a virtual environment (optional):

python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

3.Install the required dependencies:

pip install -r requirements.txt

Usage

1.Run the Streamlit application:

streamlit run app.py

2.Open your browser and go to the provided URL (usually http://localhost:8501).

Enter a query in the text box and press Enter. The application will:

Translate the query to English (if necessary).

Fetch relevant Wikipedia content.

Display the combined content on the page.

# File Structure

.
|-- app.py                  # Main Streamlit application file
|-- requirements.txt        # List of dependencies

# Example

![Ekran görüntüsü 2025-01-24 221349](https://github.com/user-attachments/assets/a92e70b5-6e3d-43f6-9f7a-dd20d8092ebb)


<br></br>

![Ekran görüntüsü 2025-01-24 200719](https://github.com/user-attachments/assets/df5a6703-6e8c-4270-91d0-95568caf34f8)


<br></br>

![Ekran görüntüsü 2025-01-24 221448](https://github.com/user-attachments/assets/51748991-6452-45b1-af76-cb71ee344e48)








https://wikipedia-search-3791.streamlit.app access the project this link.




# Dependencies

The application requires the following Python libraries:

streamlit

langchain-community

deep-translator

You can find the complete list of dependencies in requirements.txt.

# Contributing

Contributions are welcome! To contribute:

Fork the repository.

Create a new branch for your feature or bug fix.

Commit your changes and push them to your fork.

Open a pull request.

# License

This project is licensed under the MIT License. See the LICENSE file for more details.

# Acknowledgments

Streamlit for providing an easy-to-use framework for building data-driven applications.

LangChain for the powerful tools to process and retrieve Wikipedia content.

Deep Translator for enabling multilingual support.

# Contact

For any questions or suggestions, feel free to open an issue or contact kaantruk1923@gmail.com.

Enjoy exploring Wikipedia effortlessly with the Wikipedia Search Application!
