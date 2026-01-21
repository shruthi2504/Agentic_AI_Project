from orchestrator import run_orchestrator

while True:
    user_input = input("Caregiver: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    response = run_orchestrator(user_input)
    print("\nAssistant:", response)
