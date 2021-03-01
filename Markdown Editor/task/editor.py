supported_formatters = [
    'plain',
    'bold',
    'italic',
    'header',
    'ordered-list',
    'unordered-list',
    'link',
    'inline-code',
    'new-line'
]

commands = ['!help', '!done']

all_text = ''


def format_plain_text(text):
    return text


def format_bold_text(text):
    return f'**{text}**'


def format_italic_text(text):
    return f'*{text}*'


def format_inline_code(text):
    return f'`{text}`'


def format_link_text(label, url):
    return f'[{label}]({url})'


def format_header_text(level, text):
    return f'{int(level) * "#"} {text}\n'


def format_line_break():
    return '\n'


def format_ordered_list(row_count):
    result = ''
    for i in range(int(row_count)):
        result += f"{i + 1}. {input(f'- Row #{i + 1}: ')}\n"
    return result


def format_unordered_list(row_count):
    result = ''
    for i in range(int(int(row_count))):
        result += f"* {input(f'- Row #{i + 1}: ')}\n"
    return result


while True:
    command = input('- Choose a formatter: ')
    if command == '!help':
        print("Available formatters:", ' '.join(supported_formatters))
        print("Available commands: ", ' '.join(commands))
    elif command == '!done':
        file = open("output.md", "w")
        file.write(all_text)
        file.close()
        exit()
    elif command not in supported_formatters:
        print('Unknown formatting type or command. Please try again')
    elif command == 'plain':
        all_text += format_plain_text(input("- Text: "))
        print(all_text)
    elif command == 'bold':
        all_text += format_bold_text(input("- Text: "))
        print(all_text)
    elif command == 'italic':
        all_text += format_italic_text(input("- Text: "))
        print(all_text)
    elif command == 'inline-code':
        all_text += format_inline_code(input("- Text: "))
        print(all_text)
    elif command == 'link':
        all_text += format_link_text(input("- Label: "), input("- URL: "))
        print(all_text)
    elif command == 'header':
        all_text += format_header_text(input("- Level: "), input("- Text: "))
        print(all_text)
    elif command == 'new-line':
        all_text += format_line_break()
        print(all_text)
    elif command == "unordered-list":
        number = -1
        while number < 0:
            print("The number of rows should be greater than zero")
            number = int(input("- Number of rows: "))
        else:
            all_text += format_unordered_list(number)
            print(all_text)

    elif command == "ordered-list":
        number = int(input("- Number of rows: "))
        number1 = -1
        while number1 < 0:
            print("The number of rows should be greater than zero")
            number1 = int(input("- Number of rows: "))
        else:
            all_text += format_ordered_list(number1)
            print(all_text)
