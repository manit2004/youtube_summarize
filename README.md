# Youtube Summarizer

Welcome to **Youtube Summarizer**, which helps you to summarize youtube videos in a single click just by enterting the video url. You can access the webapp [here](https://summarizeyt.streamlit.app/).

## Getting Started

### Prerequisites

- Python 3.11
- Streamlit

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/manit2004/youtube_summarize.git
    cd youtube_summarize
    ```
2. Create and activate a Python virtual environment:
    - **Windows**:
        ```powershell
        python -m venv venv
        .\venv\Scripts\activate
        ```
    - **Linux**:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set the environment variable `GROQ_API_KEY` in the .env file present in your root directory with your own GROQ API key which you can get for free from [here](https://console.groq.com/keys):


## Usage

1. Open the webapp in your browser:
    ```bash
    streamlit run app.py
    ```
2. Enter the youtube video url in the text box and click on generate summary.

## Project Structure

- `app.py`: The main file that runs the Streamlit webapp.
- `requirements.txt`: List of Python libraries required to run the app.

## Contributing

We welcome contributions! If you have suggestions or improvements, please create a pull request or open an issue.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://www.streamlit.io/) for providing an amazing platform to build the webapp.
- All contributors and users for their valuable feedback and support.
