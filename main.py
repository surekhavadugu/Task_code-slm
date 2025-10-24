from question_loader import load_qa
from data_manager import load_memory, store_in_memory
from gemini_api import get_gemini_answer
from sem import find_best_match  
import os

qa_file = os.path.join("data", "questions.txt")
qa_data = load_qa(qa_file)
memory = load_memory()

print("🤖 SLM with Semantic Matching is ready! Type 'exit' to stop.")

while True:
    question = input("You: ").strip().lower()
    if question == "exit":
        print(" Goodbye!")
        break

    # 1️⃣ Semantic match
    best_answer, score = find_best_match(question, qa_data)
    if best_answer:
        print(f"SLM (match {score:.2f}): {best_answer}")
        continue

    # 2️⃣ Memory check
    if question in memory:
        print(f"(From Memory): {memory[question]}")
        continue

    # 3️⃣ Gemini fallback
    print("Fetching from Gemini model...")
    answer = get_gemini_answer(question)
    store_in_memory(question, answer)
    memory[question] = answer
    print(f"Gemini: {answer}")