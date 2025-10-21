import os
import subprocess

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
RESULTS_FILE = os.path.join(WORKSPACE, 'results.txt')

def run_script(script_path):
    try:
        result = subprocess.run(
            ['python', script_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout.strip() if result.returncode == 0 else f'Error: {result.stderr.strip()}'
    except Exception as e:
        return f'Exception: {e}'

def main():
    with open(RESULTS_FILE, 'w', encoding='utf-8') as out:
        for folder in sorted(os.listdir(WORKSPACE)):
            folder_path = os.path.join(WORKSPACE, folder)
            if os.path.isdir(folder_path) and folder.startswith('task'):
                out.write(f'{folder}\n')
                for file in sorted(os.listdir(folder_path)):
                    if file.startswith('solution') and file.endswith('.py'):
                        script_path = os.path.join(folder_path, file)
                        result = run_script(script_path)
                        out.write(f'{file} : {result}\n')
                out.write('\n')

if __name__ == '__main__':
    main()
