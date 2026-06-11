import argparse
import os
import re
import sys


def clean_browser_bookmarks(input_filename, output_filename):
    """
    Reads a browser-exported HTML bookmark file and removes leading
    asterisks from bookmark names.

    How to Run (from Terminal):
        python3 clean_browser_bookmarks.py bookmarks.html -o cleaned.html

    Python API Usage:
        from clean_browser_bookmarks import clean_browser_bookmarks
        clean_browser_bookmarks('input.html', 'output.html')

    Args:
        input_filename (str): The path to the source HTML file.
        output_filename (str): The path to save the processed HTML file.
    """
    if not os.path.exists(input_filename):
        print(f"Error: The file '{input_filename}' was not found.")
        sys.exit(1)

    try:
        # Use utf-8 to preserve all character sets (important for URLs and metadata)
        with open(input_filename, "r", encoding="utf-8") as f:
            content = f.read()

        # Regex: Captures the anchor tag, ignores whitespace, and matches leading asterisks
        pattern = r"(<A [^>]*>)\s*\*+"
        cleaned_content = re.sub(pattern, r"\1", content)

        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(cleaned_content)

        print(f"Success! Cleaned bookmarks saved to: {os.path.abspath(output_filename)}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="CLI tool to remove leading asterisks from browser bookmark HTML files.")

    parser.add_argument("input", help="Path to the original exported bookmarks HTML file.")

    parser.add_argument(
        "-o",
        "--output",
        default="bookmarks_cleaned.html",
        help="Path to save the cleaned file (default: bookmarks_cleaned.html).",
    )

    args = parser.parse_args()
    clean_browser_bookmarks(args.input, args.output)


if __name__ == "__main__":
    main()
