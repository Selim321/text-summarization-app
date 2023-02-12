# text-summarization-app
A basic text summarization web app using Streamlit and FastAPI.

<img width="1440" alt="Screenshot 2023-02-11 at 11 24 49 PM" src="https://user-images.githubusercontent.com/97094237/218284131-efd3736d-69a6-44f7-b4e8-607decc47e4a.png">

# Description 
## app.py
1. Defines a FastAPI endpint that accepts a POST request containing some text to summarize.
2. The endpoint function extracts the text from the request body, and uses a *Hugging Face* summarization piepline to summarize the text.
3. The summarized text is returned as a prediction response to the client.

## Client.py
1. Creates the UI using Streamlit and takes as input the text to summarize.
2. Defines an endpoint and sends a POST request with the text passed as a parameter.
3. Shows the summarized text.

# How to use
````
$ git clone 

````
