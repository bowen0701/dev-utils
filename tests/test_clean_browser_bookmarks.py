import os
import tempfile

from clean_browser_bookmarks import clean_browser_bookmarks


def test_clean_browser_bookmarks():
    # Create a temporary input file
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".html") as temp_in:
        temp_in.write('<A HREF="http://example.com">***Bookmark 1</A>\n')
        temp_in.write('<A HREF="http://google.com"> **Bookmark 2</A>\n')
        temp_in.write('<A HREF="http://github.com">Bookmark 3</A>\n')
        input_path = temp_in.name

    output_path = input_path + "_cleaned.html"

    try:
        clean_browser_bookmarks(input_path, output_path)

        with open(output_path, "r", encoding="utf-8") as f:
            content = f.read()

        assert '<A HREF="http://example.com">Bookmark 1</A>' in content
        assert '<A HREF="http://google.com">Bookmark 2</A>' in content
        assert '<A HREF="http://github.com">Bookmark 3</A>' in content

    finally:
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)
