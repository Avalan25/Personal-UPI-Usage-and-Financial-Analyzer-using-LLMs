from huggingface_hub import InferenceClient

client = InferenceClient("tiiuae/falcon-7b-instruct", token="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")

prompt = """
You are a finance advisor. Here is the user's spending data:
- Food: ₹12,000/month
- Rent: ₹18,000/month
- Entertainment: ₹4,000/month
- Savings: ₹3,000/month

Give practical, personalized advice.
"""

response = client.text_generation(prompt, max_new_tokens=200)
print(response)
