from models_loader import load_phi3, load_llama, load_mistral
from agents.question_understanding import build_question_understanding_agent
from agents.advice import build_advice_agent
from agents.search import build_search_agent

phi3 = load_phi3()
llama = load_llama()
mistral = load_mistral()

question_agent = build_question_understanding_agent(phi3)
advice_agent = build_advice_agent(llama)
search_agent = build_search_agent(mistral)

def run_orchestrator(user_input):
    intent = question_agent.run(user_input)

    if "resource" in intent.lower():
        return search_agent.run(user_input)

    return advice_agent.run(user_input)
