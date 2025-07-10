qa_pairs = {
    "what is portopal?": "PortoPal is a relocation assistant for Americans moving to Portugal.",
    "how do i get a visa?": "Start with the Portuguese consulate website and gather your income documents.",
    "what's the cost of living?": "It depends on the city, but Lisbon and Porto are the most expensive."
}

def chatbot():
    print("Ask me anything about moving to Portugal! Type 'exit' to quit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            break
        response = qa_pairs.get(user_input, "Sorry, I don't know that yet.")
        print("Bot:", response)

chatbot()
