import string
import os


class Colors:
    WHITE = "\033[37m"
    GREEN = "\033[32m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"


messages = {
    'welcome': f'{Colors.CYAN}-== Bem vindo ao Word Counter! ==-',
    'sentence': f'{Colors.WHITE}Digite sua frase: {Colors.YELLOW}',
    'sentence_or_bye': f'{Colors.WHITE}Digite outra frase ou digite "{Colors.CYAN}sair{Colors.WHITE}": {Colors.YELLOW}',
    'invalid_sentence': f'{Colors.WHITE}Por favor, insira uma frase {Colors.GREEN}válida{Colors.WHITE}.',
    'result': f'{Colors.WHITE}Quantidade de palavras:{Colors.GREEN}',
    'exit': f'{Colors.CYAN}- Saindo do programa. Até logo!'
}


def start():
    clear_screen()
    print(messages['welcome'])
    
    while True:
        sentence = get_input(messages['sentence'])
        if check_exit(sentence, messages['exit']):
            return

        word_count = count_words(sentence)
        print(messages['result'], word_count, '\n')

        while True:
            sentence_or_bye = get_input(messages['sentence_or_bye'])
            if check_exit(sentence_or_bye, messages['exit']):
                return

            word_count = count_words(sentence_or_bye)
            print(messages['result'], word_count, '\n')


def count_words(entry):
    punctuation = string.punctuation
    for char in punctuation:
        entry = entry.replace(char, ' ')
    entry = entry.strip()
    words = entry.split()
    return len(words)


def check_exit(entry, msg=None):
    if entry.lower() in ['sair', 'close', 'exit']:
        if msg:
            print(msg)
        return True
    return False


def invalid_sentence(entry, msg):
    if not entry.strip():
        print(msg)
        return True
    return False


def get_input(msg):
    while True:
        __input__ = input(msg)
        if invalid_sentence(__input__, messages['invalid_sentence']):
            continue
        return __input__
        

def clear_screen():
    system = os.name
    if system == 'nt':  # windows
        os.system('cls')
    else:
        os.system('clear')


start()
