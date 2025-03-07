# CodeSelect

<div align="center">

![CodeSelect Logo](https://img.shields.io/badge/CodeSelect-1.0.0-blue)

**Easily select and share code with AI assistants**

</div>

CodeSelect is a lightweight tool that helps developers share code with AI assistants like Claude or ChatGPT. It provides a simple interface to select files from a project and exports them in an AI-friendly format with intelligent context about project structure and relationships between files.

## 🚀 Quick Install

```bash
# One-line installation
curl -sSL https://raw.githubusercontent.com/mikeolteanu/codeselect/refs/heads/main/install.sh | bash
```

## ✨ Features

- **Visual File Selection**: Interactive UI to easily select files with checkboxes
- **Intelligent Code Analysis**: Automatically detects imports and relationships between files
- **Multi-language Support**: Works with Python, C/C++, JavaScript, Java, Go, Ruby, PHP, Rust, Swift and more
- **Zero Dependencies**: Works with standard Python libraries only
- **Non-admin Installation**: No special privileges required
- **Clipboard Integration**: Automatically copies output to clipboard
- **AI-optimized Format**: Structures output to help AI assistants understand project context

## 🛠️ Usage

```bash
# Navigate to your project directory
cd ~/projects/myproject

# Run CodeSelect
codeselect

# Export specific directory with custom filename
codeselect /path/to/project -o output.txt

# Help and options
codeselect --help
```

## 🖥️ Interface Controls

- **↑/↓**: Navigate between files
- **Space**: Toggle selection of file/directory
- **←/→**: Collapse/expand directories
- **A**: Select all files
- **N**: Deselect all files
- **B**: Toggle clipboard copy
- **D** or **Enter**: Complete selection and export
- **X** or **Esc**: Exit without saving

## 📄 Output Formats

CodeSelect offers four output formats:

- **LLM** (default): Optimized for language models with context about file relationships
- **Markdown**: GitHub-compatible markdown with syntax highlighting
- **TXT**: Plain text format for maximum compatibility
- **Aider**: Just filenames separated by spaces (for use with aider and similar tools)

```bash
# Generate GitHub-compatible markdown
codeselect --format md

# Generate AI-optimized format
codeselect --format llm

# Generate space-separated filenames for aider
codeselect --format aider
```

## ⚙️ Advanced Options

```
usage: codeselect [-h] [-o OUTPUT] [--format {txt,md,llm}] [--skip-selection] [--yes-clipboard] [--version] [directory]

CodeSelect v1.0.0 - Select files to share with AI assistants

positional arguments:
  directory             Directory to scan (default: current directory)

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file path (default: based on directory name)
  --format {txt,md,llm}
                        Output format (default: llm - optimized for LLMs)
  --skip-selection      Skip the selection interface and include all files
  --yes-clipboard       Enable automatic copy to clipboard (disabled by default)
  --version             Show version information
```

### Configuration

CodeSelect has built-in default settings that can be overridden using command-line arguments. The configuration settings are embedded directly in the script for easy customization.

You can modify the default settings by editing the configuration section at the top of the `codeselect.py` file:

```python
# Default directory to scan
DEFAULT_DIRECTORY = "."

# Default output format (txt, md, llm)
DEFAULT_FORMAT = "llm"

# Default output filename (None = auto-generate)
DEFAULT_OUTPUT = None

# Skip the selection interface
SKIP_SELECTION = False

# Enable automatic copy to clipboard
COPY_TO_CLIPBOARD = False

# Default ignore patterns
DEFAULT_IGNORE_PATTERNS = [
    '.git', '__pycache__', '*.pyc', '.DS_Store', 
    '.idea', '.vscode', 'node_modules', 'venv',
    '.env', '*.log', '*.sh'
]
```

## 🔍 How It Works

1. **Scan**: CodeSelect scans your project directory structure
2. **Select**: Interactive interface lets you choose which files to include
3. **Analyze**: Automatically detects dependencies between files
4. **Generate**: Creates a specially formatted output optimized for AI assistants
5. **Copy**: Optionally copies result to clipboard for easy pasting (when enabled)

## 💻 Development

CodeSelect was developed in just 30 minutes with the help of Claude, Anthropic's AI assistant. It demonstrates how AI can help create useful developer tools through iterative improvements.

Contributions are welcome! Please feel free to submit a Pull Request.

## 🗑️ Uninstallation

To remove CodeSelect from your system:

```bash
# One-line uninstallation
curl -sSL https://raw.githubusercontent.com/mikeolteanu/codeselect/main/uninstall.sh | bash
