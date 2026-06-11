# Development Utils

`dev-utils` is a collection of development utilities for personal and shared use.

## Utilities

### 1. Clean Browser Bookmarks (`clean_browser_bookmarks.py`)

A tool to remove leading asterisks from browser-exported HTML bookmark files.

#### Usage (CLI)

```bash
python3 clean_browser_bookmarks.py bookmarks.html -o cleaned.html
```

### 2. PDF Page Counter (`Makefile`)

A utility to list and sort PDF files in the current directory by page count in descending order. (Requires macOS `mdls`).

#### Usage

```bash
make count-pages
```

## Development

### Prerequisites

- Python 3.10+
- `ruff`, `mypy`, `pytest`
- macOS (for `make count-pages`)

### Running Checks Locally

```bash
# Linting
ruff check .

# Type checking
mypy .

# Testing
PYTHONPATH=. pytest
```

### Makefile Commands

Additional utility commands are available via `Makefile`:

- `make count-pages`: Lists all PDFs in the current directory sorted by page count.

### CI/CD

This project uses GitHub Actions for Continuous Integration. Every push or pull request triggers linting, type checking, and unit tests across multiple Python versions (3.10, 3.11, 3.12).
