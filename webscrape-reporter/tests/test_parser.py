import unittest
import sys
from pathlib import Path

# Add src to path to import the module
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from webscrape_reporter.scraper.parser import parse_html


class TestParser(unittest.TestCase):
    """Test cases for the HTML parser module."""

    def test_parse_html_basic(self):
        """Test parsing HTML with basic anchor tags."""
        html = """
        <html>
            <body>
                <a href="https://example.com">Example</a>
                <a href="https://github.com">GitHub</a>
                <a href="/relative/path">Relative Link</a>
            </body>
        </html>
        """
        links = parse_html(html)
        expected = ["https://example.com", "https://github.com", "/relative/path"]
        self.assertEqual(links, expected)

    def test_parse_html_empty(self):
        """Test parsing HTML with no links."""
        html = "<html><body><p>No links here</p></body></html>"
        links = parse_html(html)
        self.assertEqual(links, [])

    def test_parse_html_no_href(self):
        """Test parsing HTML with anchor tags but no href attributes."""
        html = """
        <html>
            <body>
                <a name="anchor1">Named Anchor</a>
                <a>No href</a>
            </body>
        </html>
        """
        links = parse_html(html)
        self.assertEqual(links, [])

    def test_parse_html_empty_href(self):
        """Test parsing HTML with empty href attributes."""
        html = """
        <html>
            <body>
                <a href="">Empty href</a>
                <a href="https://example.com">Valid href</a>
            </body>
        </html>
        """
        links = parse_html(html)
        self.assertEqual(links, ["https://example.com"])

    def test_parse_html_mixed_content(self):
        """Test parsing HTML with mixed content and multiple links."""
        html = """
        <!DOCTYPE html>
        <html>
            <head><title>Test Page</title></head>
            <body>
                <h1>Welcome</h1>
                <p>Visit <a href="https://python.org">Python</a> for more info.</p>
                <ul>
                    <li><a href="https://docs.python.org">Documentation</a></li>
                    <li><a href="https://pypi.org">PyPI</a></li>
                    <li><a href="#section1">Internal Link</a></li>
                </ul>
                <div>
                    <a href="mailto:test@example.com">Email</a>
                </div>
            </body>
        </html>
        """
        links = parse_html(html)
        expected = [
            "https://python.org",
            "https://docs.python.org", 
            "https://pypi.org",
            "#section1",
            "mailto:test@example.com"
        ]
        self.assertEqual(links, expected)


if __name__ == "__main__":
    unittest.main()