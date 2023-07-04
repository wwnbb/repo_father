# Repo Father


Repo Father is a command-line tool designed to automate the process of repository creation based on template files. It reads from a template folder, prompts the user to select a template, then asks for input for each placeholder in the selected template.


Placeholders are defined as `{{PLACEHOLDER_NAME}}` within the template files. After receiving user input, the tool replaces these placeholders with the user-defined values.
Installation


Before you can use Repo Father, you need to install it on your system. Here are the steps to do so:

```bash
git clone https://github.com/your-username/repo_creator.git
cd repo_creator
pip install -r requirements.txt
```


#### Usage


To use Repo Creator, follow the below steps:

    Run the script with the command:


#### Template Creation

To add your own templates, follow these steps:

* Create a new directory in the /templates folder.
* Add your files and remember to use {{PLACEHOLDER_NAME}} for areas that require user input.

For example, to create a readme file with a custom project name and description, you could create a README.md file like this:

```markdown

# {{PROJECT_NAME}}

{{PROJECT_DESCRIPTION}}
```

## Licensing

The code in this project is licensed under:

GNU LESSER GENERAL PUBLIC LICENSE
Version 2.1, February 1999
