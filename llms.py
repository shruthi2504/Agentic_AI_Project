from langchain_community.llms import LlamaCpp

def load_llm(model_path, temperature, n_ctx=4096):
    return LlamaCpp(
        model_path=model_path,
        n_ctx=n_ctx,
        temperature=temperature,
        max_tokens=512,
        n_threads=8,
        verbose=False
    )
