import zipfile
import os
from bs4 import BeautifulSoup

def format_html(input_file, output_file, indent_spaces):
    try:
        with open(input_file, 'r', encoding = 'utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        formatted_html = soup.prettify()

        lines          = formatted_html.split('\n')
        indented_lines = []
        current_indent = 0

        # prettify() 怎么不能用了？

        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith('</'):
                current_indent = max(0, current_indent - indent_spaces)
            indented_lines.append(' ' * current_indent + stripped_line)
            if (    stripped_line. startswith('<') and
                not stripped_line.  endswith('/>') and
                not stripped_line.startswith('</')):
                current_indent += indent_spaces

        formatted_html = '\n'.join(indented_lines)

        with open(output_file, 'w', encoding = 'utf-8') as f:
            f.write(formatted_html)
            
        print(f"HTML file '{input_file}' has been successfully formatted and saved as '{output_file}'。")

    except FileNotFoundError:
        print(f"Error: No such file @'{input_file}'。")
    except Exception as e:
        print(f"Error: @{e}")

def html_files_process(folder_path, indent_spaces):
    for filename in os.listdir(folder_path):
        if filename.endswith('.html'):
            file_path = os.path.join(folder_path, filename)
            zip_path = os.path.join(folder_path, filename + '.zip')

            with zipfile.ZipFile(zip_path, 'w') as zipf:
                zipf.write(file_path, filename)

            with zipfile.ZipFile(zip_path, 'r') as zipf:
                zipf.extractall(folder_path)

            format_html(file_path, file_path, indent_spaces)


folder_path = '.'
indent_spaces = 2

html_files_process(folder_path, indent_spaces)