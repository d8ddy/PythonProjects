from difflib import get_close_matches


def trained_file(file_path: str) -> dict:
    chat_data = {}
    try:
        with open(file_path) as file:
            for line in file:
                data = [line.rsplit(' ', 1)
                        for line in line.split('\n') if line]
                chat_data = {key: str(value) for key, value in data}
                print(chat_data)
    except Exception as e:
        print(f'Error: {e}')

    return chat_data


def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(
        user_question, questions, n=1, cutoff=0.6)
    if matches:
        return matches[0]


def chat_bot(knowledge: dict):
    user_input: str = input('You: ')
    best_match: str | None = get_best_match(user_input, knowledge)
    while True:
        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print('Bot: I do not understand :(')


if __name__ == '__main__':
    trained_file('Bots/dialogs.txt')
    # chat_bot(knowledge=trained_file('Bots/dialogs.txt'))
