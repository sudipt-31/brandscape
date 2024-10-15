from huggingface_hub import InferenceClient
import json
repo_id = "google/gemma-2b"
llm_client = InferenceClient(
    model=repo_id,
    timeout=120,
)
def call_llm(inference_client: InferenceClient, prompt: str):
    response = inference_client.post(
        json={
            "inputs": prompt,
            "parameters": {"max_new_tokens": 1200},
            "task": "text-generation",
        },
    )
    return json.loads(response.decode())[0]["generated_text"]
response=call_llm(llm_client, "write a c program to swap two numbers")
print (response)

# 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