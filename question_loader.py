def load_qa(file_path):
    qa_list = []
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.read().split("\n\n")
        for item in lines:
            parts = item.split("\n", 1)
            if len(parts) == 2:
                question, answer = parts
                qa_list.append({
                    "question": question.strip(),
                    "answer": answer.strip()
                })
    return qa_list