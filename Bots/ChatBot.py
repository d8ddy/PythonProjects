from difflib import get_close_matches


def trained_file(file_path: str) -> dict:
    chat_data = {}
    try:
        with open(file_path, 'r') as file:
            data_by_line: str = file.read().split('\n')
            lines: list[str] = []
            for line in data_by_line:
                l = line.split('\t')
                l = tuple(l)
                print(l)
                lines.append(l)
            for key, val in lines:
                chat_data[key] = val
            # print(chat_data)
    except Exception as e:
        print(f'Error: {e}')
    return chat_data


def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(
        user_question, questions, n=1, cutoff=0.40)
    if matches:
        return matches[0]


def chat_bot(knowledge: dict):
    while True:
        user_input: str = input('You: ')
        best_match: str | None = get_best_match(user_input, knowledge)

        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print('Bot: I do not understand :(')

        if user_input.lower() == 'EXIT':
            break


if __name__ == '__main__':
    trained_file('Bots/dialogs.txt')
    # chat_bot(knowledge=trained_file('Bots/dialogs.txt'))
