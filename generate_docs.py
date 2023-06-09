import os
import pkgutil
import subprocess
import shutil

SRC_DIR = 'src'

def generate_documentation(module_name):
    # Remove 'src/' prefix from module_name
    module_name = module_name.replace('src/', '')
    output_file = os.path.join('docs', f'{module_name}.md')
    with open(output_file, 'w') as f:
        subprocess.run(['pydoc-markdown', '-I', SRC_DIR, '-m', module_name, '--render-toc'], stdout=f)
    # Return the filename of the generated documentation for use in the index
    return output_file

def main():
    docs_dir = os.path.join(os.getcwd(), 'docs')
    # If docs directory exists, remove it and all its contents
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    # Recreate docs directory
    os.makedirs(docs_dir, exist_ok=True)
    index_file = os.path.join('docs', 'index.md')

    with open(index_file, 'w') as index:
        for finder, name, ispkg in pkgutil.iter_modules([SRC_DIR]):
            if name == '__init__':
                continue
            output_file = generate_documentation(name)
            # Write a link to the generated documentation in the index file
            index.write(f'- [{name}]({output_file})\n')

if __name__ == '__main__':
    main()
