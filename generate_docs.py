import os
import pkgutil
import subprocess

SRC_DIR = 'src'

def generate_documentation(module_name):
    output_file = os.path.join('docs', f'{module_name}.md')
    with open(output_file, 'w') as f:
        subprocess.run(['pydoc-markdown', '-I', SRC_DIR, '-m', module_name, '--render-toc'], stdout=f)

def main():
    os.makedirs('docs', exist_ok=True)

    for finder, name, ispkg in pkgutil.iter_modules([SRC_DIR]):
        if name == '__init__':
            continue
        generate_documentation(name)

if __name__ == '__main__':
    main()
