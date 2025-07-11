from gradio_client import Client

def get_recommendation(summary):
    client = Client("Avalan16/mydemo", hf_token="YOUR_HF_TOKEN")
    result = client.predict(summary, api_name="/")
    return result
