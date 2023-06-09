import os
import pkgutil
import subprocess
import shutil
from typing import List, Tuple

SRC_DIR = 'src'

def generate_documentation(module_name: str) -> str:
    """
    Generate markdown documentation for a Python module.

    Args:
        module_name: Name of the module, assumed to be a string with 'src/' prefix.

    Returns:
        The filename of the generated markdown file.
    """
    # Remove 'src/' prefix from module_name
    module_name = module_name.replace('src/', '')
    output_file = os.path.join('docs', f'{module_name}.md')
    with open(output_file, 'w') as f:
        subprocess.run(['pydoc-markdown', '-I', SRC_DIR, '-m', module_name, '--render-toc'], stdout=f)
    return f'{module_name}.md'

def create_index(modules: List[Tuple[str, str]]) -> None:
    """
    Create an index file with links to module documentation.

    Args:
        modules: List of tuples, each containing a module name and the filename of its documentation.
    """
    index_file = os.path.join('docs', 'index.md')
    with open(index_file, 'w') as index:
        # Write preamble
        index.write("# Modules Documentation Index\n")
        index.write("This index contains links to documentation for each module in the project. "
                    "Click on a module name to view its documentation.\n\n")
        for module_name, output_file in modules:
            # Write a link to the generated documentation in the index file
            index.write(f'- [{module_name}]({output_file})\n')

def main() -> None:
    """
    Main function to generate documentation for modules and create an index.
    """
    docs_dir = os.path.join(os.getcwd(), 'docs')
    # If docs directory exists, remove it and all its contents
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    # Recreate docs directory
    os.makedirs(docs_dir, exist_ok=True)

    modules = []
    for finder, name, ispkg in pkgutil.iter_modules([SRC_DIR]):
        if name == '__init__':
            continue
        output_file = generate_documentation(name)
        modules.append((name, output_file))

    create_index(modules)

if __name__ == '__main__':
    main()
