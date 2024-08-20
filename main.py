from src.blocks import markdown_to_html_node
import os
import shutil

def copy_directory(path_from, path_to):
    if os.path.exists(path_from) and os.path.exists(path_to):
        shutil.rmtree(path_to)

    copy_directory_rec(path_from, path_to)

def copy_directory_rec(path_from, path_to):
    if not os.path.isdir(path_from):
        shutil.copy(path_from, path_to)
        return

    os.mkdir(path_to)
    contents = os.listdir(path_from)
    for content in contents:
        if os.path.isdir(os.path.join(path_from, content)):
            copy_directory_rec(os.path.join(path_from, content), os.path.join(path_to, content))
        else:
            copy_directory_rec(os.path.join(path_from, content), path_to)

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line.lstrip('# ').strip(' ')

    raise Exception("Title doesn't exist.")

def read_file(file_path):
    with open(file_path) as file:
        return file.read()


def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for from_path in os.listdir(dir_path_content):
        if not os.path.isdir(os.path.join(dir_path_content, from_path)):
            return generate_page(os.path.join(dir_path_content, from_path), template_path, os.path.join(dest_dir_path, from_path.replace('.md', '.html')))

        if not os.path.exists(os.path.join(dest_dir_path, from_path)):
            os.mkdir(os.path.join(dest_dir_path, from_path))
        generate_pages_recursive(os.path.join(dir_path_content, from_path), template_path, os.path.join(dest_dir_path, from_path))


def generate_page(from_path, template_path, dest_path):
    if not os.path.exists(from_path) and not os.path.exists(template_path):
        if os.path.exists(template_path):
            raise Exception("Markdown file doesn't exists")
        raise Exception("Template file required")

    markdown_content = read_file(from_path)
    template_content = read_file(template_path)

    title = extract_title(markdown_content)
    html_content = markdown_to_html_node(markdown_content).to_html()

    template_content = template_content.replace('{{ Title }}', title)
    template_content = template_content.replace('{{ Content }}', html_content)

    write_to_file(dest_path, template_content)


def main():
    copy_directory('./static', './public/static')
    data = generate_pages_recursive('./content/', './template.html', './public/')


main()