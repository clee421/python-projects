import urllib.request
import urllib.error


def fetch_url(url: str) -> str:
    """
    Fetch the raw HTML content from a given URL.
    
    Args:
        url: The URL to fetch
        
    Returns:
        The HTML content as a string
        
    Raises:
        urllib.error.URLError: If the URL cannot be fetched
        urllib.error.HTTPError: If an HTTP error occurs
    """
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        raise urllib.error.HTTPError(
            url, e.code, f"HTTP Error {e.code}: {e.reason}", e.hdrs, e.fp
        )
    except urllib.error.URLError as e:
        raise urllib.error.URLError(f"URL Error: {e.reason}")
    except UnicodeDecodeError:
        # Try with different encoding if UTF-8 fails
        with urllib.request.urlopen(url) as response:
            return response.read().decode('latin-1')
