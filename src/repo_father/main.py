import os
import re
import shutil
import sys


def copy_template_folder(template_folder, new_folder):
    if os.path.exists(new_folder):
        print(f"Folder '{new_folder}' already exists. Exiting.")
        sys.exit(1)

    # Copy the template folder to the new folder
    shutil.copytree(template_folder, new_folder)


def replace_placeholders_in_path(path, variables):
    for key, value in variables.items():
        escaped_key = re.escape(key)
        pattern = r"{{" + escaped_key + r"}}"

        path = re.sub(pattern, value, path)
    return path


def replace_placeholders(folder, variables):
    for dirpath, dirnames, _ in os.walk(folder, topdown=False):
        # Replace placeholders in directory names
        for dirname in dirnames:
            old_dirpath = os.path.join(dirpath, dirname)
            new_dirpath = replace_placeholders_in_path(old_dirpath, variables)

            if new_dirpath != old_dirpath:
                os.rename(old_dirpath, new_dirpath)

    for dirpath, _, filenames in os.walk(folder, topdown=False):
        # Replace placeholders in file content
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            new_filepath = replace_placeholders_in_path(filepath, variables)
            if new_filepath != filepath:
                os.rename(filepath, new_filepath)

            with open(new_filepath, "r") as f:
                content = f.read()

            for key, value in variables.items():
                content = content.replace("{{" + key + "}}", value)

            with open(new_filepath, "w") as f:
                f.write(content)


def get_placeholders(folder):
    placeholders = set()

    # Extract placeholders from file content and directory/file names
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)

            with open(filepath, "r") as f:
                content = f.read()
                placeholders.update(re.findall(r"\{\{(.*?)\}\}", content))

        placeholders.update(re.findall(r"\{\{(.*?)\}\}", " ".join(dirnames)))
        placeholders.update(re.findall(r"\{\{(.*?)\}\}", " ".join(filenames)))

    return placeholders


def get_templates_folder(templates_folder):
    return [
        name
        for name in os.listdir(templates_folder)
        if os.path.isdir(os.path.join(templates_folder, name))
    ]


def main():
    templates_folder = "templates"
    templates = get_templates_folder(templates_folder)

    for i, template in enumerate(templates, start=1):
        print(f"{i}. {template}")

    template_num = int(input("Enter the number of the template you want to use: ")) - 1
    template_folder = os.path.join(templates_folder, templates[template_num])

    new_folder = input("Enter the new directory name: ")

    # Get unique placeholders
    placeholders = get_placeholders(template_folder)

    # Add new_folder as variable
    variables = {"NAME": new_folder}

    # Ask user for value of each placeholder
    for placeholder in placeholders:
        if not variables.get(placeholder):
            variables[placeholder] = input(f"Enter the value for {placeholder}: ")

    copy_template_folder(template_folder, new_folder)
    replace_placeholders(new_folder, variables)
    print(f"Directory '{new_folder}' created and placeholders replaced.")


if __name__ == "__main__":
    main()
