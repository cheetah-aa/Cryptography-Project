import os
import sys

def generate_tree(startpath, output_file=None, ignore_dirs=None):
    if ignore_dirs is None:
        ignore_dirs = ['.git', '__pycache__', 'venv', 'node_modules', '.idea', '.vscode']
    
    if output_file:
        sys.stdout = open(output_file, 'w')
    
    for root, dirs, files in os.walk(startpath):
        # Filter out directories to ignore
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")
    
    if output_file:
        sys.stdout.close()
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    generate_tree('.', 'project_structure.txt')