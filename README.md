# Test-Langchain

A Streamlit application that leverages Langchain for various tasks. This README provides setup and installation instructions to get the project running on your system.

---

## Prerequisites

Before setting up the project, ensure the following are installed:

1. **Python**  
   Install Python (version 3.8 or above). You can download it from [Python's official website](https://www.python.org/downloads/).

---

## Setting Up the Project

### Create and Activate a Virtual Environment

It is recommended to use a virtual environment to manage dependencies for this project.

##### **On Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

##### **On macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### **Install Required Dependencies:**

After activating the virtual environment, install all the dependencies listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```

#### **Set Up the .env File:**

Create a file named .env in the root directory of the project and add the following environment variables:

.env

```bash
OPENAI_API_KEY = "<your_openai_api_key>"
GOOGLE_API_KEY = "<your_google_api_key>"
GOOGLE_CSE_ID = "<your_google_cse_id>"
AZURE_API_KEY = "<your_azure_api_key>"
OPENAI_API_BASE = "<your_openai_api_base>"
OPENAI_DEPLOYMENT_NAME = "<your_openai_deployment_name>"
OPENAI_API_VERSION = "<your_openai_api_version>"
```

Replace the placeholders with your respective API keys.

#### **Running the Project:**

To start the project, run the following command in your terminal:

```bash
streamlit run main.py
```

This will launch the Streamlit application in your default web browser.
