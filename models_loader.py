from llms import load_llm

def load_phi3():
    return load_llm(
        "models/phi3/phi-3-mini-4k-instruct-q4_k_m.gguf",
        temperature=0.0
    )

def load_llama():
    return load_llm(
        "models/llama/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf",
        temperature=0.6
    )

def load_mistral():
    return load_llm(
        "models/mistral/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
        temperature=0.2
    )

def load_qwen():
    return load_llm(
        "models/qwen/qwen2.5-7b-instruct-q4_k_m-00001-of-00002.gguf",
        temperature=0.2
    )
