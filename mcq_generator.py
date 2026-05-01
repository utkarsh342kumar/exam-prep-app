import random
from nlp_utils import extract_keywords, get_sentences, get_distractors

def generate_mcqs(text, difficulty="Medium"):
    keywords = extract_keywords(text)
    sentences = get_sentences(text)

    questions = []

    for _ in range(5):
        if not keywords or not sentences:
            break

        word = random.choice(keywords)
        sentence = random.choice(sentences)

        if word not in sentence:
            continue

        # Difficulty logic
        if difficulty == "Easy":
            question = sentence.replace(word, "_____")
        elif difficulty == "Medium":
            question = f"What fits in the blank: {sentence.replace(word, '_____')}?"
        else:
            question = f"Identify the correct term: {sentence.replace(word, '_____')}"

        distractors = get_distractors(word)

        if difficulty == "Easy":
            distractors = distractors[:2]
        elif difficulty == "Hard":
            distractors = distractors[:3]

        options = distractors + [word]
        random.shuffle(options)

        questions.append({
            "question": question,
            "options": options,
            "answer": word
        })

    return questions
