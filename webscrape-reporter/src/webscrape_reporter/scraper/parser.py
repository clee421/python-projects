from html.parser import HTMLParser


class LinkExtractor(HTMLParser):
    """HTML parser that extracts href attributes from anchor tags."""
    
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        """Handle start tags and extract href from anchor tags."""
        if tag == "a":
            for attr_name, attr_value in attrs:
                if attr_name == "href" and attr_value:
                    self.links.append(attr_value)


def parse_html(html: str) -> list[str]:
    """
    Parse HTML content and extract all href links.
    
    Args:
        html: The HTML content as a string
        
    Returns:
        A list of href link strings found in the HTML
    """
    parser = LinkExtractor()
    parser.feed(html)
    return parser.links
