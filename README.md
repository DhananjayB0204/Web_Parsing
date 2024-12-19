# Web_Parsing
Data Skill Assessment - Parsing project


**REQUIREMENT ANALYSIS**

**Introduction**

Welcome to the Web Scraper project documentation! This project demonstrates how to leverage Django, MongoDB, and BeautifulSoup to build a robust web scraping application. The main purpose of this project is to read HTML content from a JSON file, extract various elements such as paragraphs, mobile numbers, email addresses, LinkedIn URLs, Twitter handles, and image URLs, and then store this extracted data in a MongoDB collection. One of the key features of this project is its ability to handle duplicate data, ensuring that each piece of information is unique within the database.

#### Key Features

1.  **Automated Data Extraction**: This project automates the extraction of specific data elements from HTML content, saving time and reducing manual effort.
    
2.  **Duplicate Data Handling**: It includes mechanisms to avoid inserting duplicate data into the MongoDB collection, ensuring data integrity and cleanliness.
    
3.  **Scalability**: Built with Django, the project can be easily scaled and extended to include more features or handle larger datasets.
    
4.  **Ease of Use**: With a simple HTTP endpoint, users can trigger the data extraction and storage process, making it accessible even to those with limited technical knowledge.

#### Technologies Used

-   **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design. It takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.
    
-   **MongoDB**: A NoSQL database known for its high performance, high availability, and easy scalability. It is ideal for handling large volumes of unstructured data.
    
-   **BeautifulSoup**: A Python library for parsing HTML and XML documents. It creates parse trees from page source code that can be used to extract data from HTML.
    
-   **Python**: The programming language used to develop the entire project. Python is known for its readability, simplicity, and vast ecosystem of libraries and frameworks.

Great! Let's go through the installation process step-by-step. This will ensure you have all the necessary components installed to get your project up and running smoothly.

Great! Let's go through the installation process step-by-step. This will ensure you have all the necessary components installed to get your project up and running smoothly.

### Installation

#### Prerequisites
Before you begin, make sure you have the following installed on your system:
- **Python 3.x**: You can download Python from [python.org](https://www.python.org/).
- **MongoDB**: You can download MongoDB from [mongodb.com](https://www.mongodb.com/try/download/community).

### Step-by-Step Setup

1. **Clone the Repository**
   First, you need to clone the repository where your project is stored. Replace `<repository-url>` with the actual URL of your repository.

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment**
   It's a good practice to use a virtual environment to manage dependencies for your project. Here’s how you can create and activate a virtual environment:

   ```sh
   python -m venv venv
   ```

   - On Windows:
     ```sh
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

3. **Install Dependencies**
   Now, you'll need to install all the dependencies required for your project. This can be done using the `requirements.txt` file.

   ```sh
   pip install -r requirements.txt
   ```

   Your `requirements.txt` file should contain the following (based on the packages used in your project):

   ```plaintext
   beautifulsoup4==4.9.3
   pymongo==3.11.4
   ```

4. **Configure MongoDB**
   Ensure that MongoDB is running on your local machine. You can start the MongoDB server by running the following command in a new terminal window:

   ```sh
   mongod
   ```

5. **Update MongoDB Connection in `views.py`**
   Open your `views.py` file and update the MongoDB connection details as needed:

   ```python
   client = MongoClient('mongodb://localhost:27017/')
   db = client['webscrapr']  # Your database name
   collection = db['your_collection_name']  # Your collection name
   ```

6. **Run the Django Development Server**
   Start the Django development server to test your project locally:

   ```sh
   python manage.py runserver
   ```

7. **Access the Parsing Functionality**
   Open your web browser and navigate to the following URL to trigger the data extraction and storage process:

   ```
   http://127.0.0.1:8000/parser_app/parse/
   ```

This will start the web scraping process, and the data will be stored in your MongoDB collection.

### Final Project Structure
Your project directory should look something like this:

```
myproject/
│
├── parser_app/
│   ├── views.py
│   └── ... (other files)
│
├── requirements.txt
└── manage.py
```

### Configuration

Once you have your project set up, it’s important to configure it correctly to ensure smooth operation. Here are the steps for configuring your Django and MongoDB integration.

#### Configure MongoDB Connection

1. **Open `views.py`**:
   - Navigate to your Django app directory and open the `views.py` file.

2. **Update MongoDB Connection Details**:
   - Ensure that your MongoDB client is correctly configured to connect to your MongoDB instance. Modify the connection string as needed.

```python
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Update this with your MongoDB connection string if needed
db = client['webscrapr']  # Your database name
collection = db['Web_scraped_data']  # Your collection name
```

3. **Database and Collection Names**:
   - Replace `'webscrapr'` with the actual name of your database.
   - Replace `'Web_scraped_data'` with the name of your collection where you want to store the scraped data.

#### JSON File Configuration

Ensure the JSON file (`pressranger_scraped_pub_pages.json`) is correctly placed in your project directory and encoded in UTF-8. This file should contain the HTML content you want to parse.

#### Django Settings

1. **Ensure Django Settings are Correct**:
   - Verify that your Django settings are correctly configured. This includes ensuring `INSTALLED_APPS`, `MIDDLEWARE`, `TEMPLATES`, and other necessary settings are properly set in your `settings.py` file.

2. **Static and Media Files**:
   - If your project includes static or media files, make sure to configure the `STATIC_URL`, `STATICFILES_DIRS`, `MEDIA_URL`, and `MEDIA_ROOT` settings in `settings.py`.

### Usage

With your project configured, you can now use it to scrape data and store it in MongoDB.

1. **Run the Django Development Server**:
   - Start the server to test your project locally.
   ```sh
   python manage.py runserver
   ```

2. **Access the Parsing Functionality**:
   - Open your web browser and navigate to the following URL to trigger the data extraction and storage process:
   ```
   http://127.0.0.1:8000/parser_app/parse/
   ```

   This will execute the `parse_and_store` function, processing your JSON file and inserting the extracted data into MongoDB.

3. **Check MongoDB**:
   - Use MongoDB Compass or the MongoDB shell to verify that the data has been inserted into your database and collection.

### Directory Structure

Here is an example of what your project directory structure should look like:

```
myproject/
│
├── parser_app/
│   ├── views.py
│   └── ... (other files)
│
├── requirements.txt
├── pressranger_scraped_pub_pages.json  # Your JSON file with HTML content
└── manage.py

```

### Code Overview

#### `views.py`
- **Function**: `parse_and_store`
  - **Description**: Reads the JSON file, extracts data, removes duplicates, and stores it in MongoDB.
  - **Key Operations**:
    - Parsing HTML with BeautifulSoup.
    - Extracting paragraphs, mobile numbers, email addresses, LinkedIn URLs, Twitter handles, and image URLs.
    - Removing duplicate entries within fields.
    - Checking for existing documents in MongoDB before insertion.### Code Overview

#### `views.py`

The `views.py` file contains the core logic for parsing and storing the data from the JSON file. Here's a breakdown of the key components:

1.  **Imports**:
    
    -   We import the necessary modules and libraries, including `BeautifulSoup` for HTML parsing, `json` for handling JSON data, `re` for regular expressions, `MongoClient` from `pymongo` for MongoDB interactions, and `HttpResponse` and `HttpResponseNotFound` from `django.http` for HTTP responses.
        
2.  **Function** `parse_and_store`:
    
    -   **Loading Data**: The JSON data is loaded from a file named `pressranger_scraped_pub_pages.json`.
        
    -   **Error Handling**: If the file is not found or there's an encoding issue, appropriate HTTP responses are returned.
        
    -   **Database Connection**: The MongoDB client is set up to connect to the `webscrapr` database and a specified collection.
        
    -   **Data Processing**: The function iterates over each document in the JSON data, parses the HTML content using BeautifulSoup, and extracts relevant information like paragraphs, mobile numbers, email addresses, LinkedIn URLs, Twitter handles, and image URLs. Duplicate values within each document are removed.
        
    -   **Duplication Check**: Before inserting a document, a check is performed to ensure it doesn't already exist in the collection based on the specified fields.
        
    -   **Data Insertion**: If no duplicates are found, the cleaned data is inserted into the MongoDB collection.
        
    -   **HTTP Response**: Returns a success response if all data is processed and inserted correctly.


