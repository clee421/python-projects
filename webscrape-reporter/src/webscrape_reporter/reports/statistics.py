from collections import Counter
from urllib.parse import urlparse


def summarize(links: list[str]) -> dict:
    """
    Generate statistics summary from a list of links.
    
    Args:
        links: List of link strings
        
    Returns:
        Dictionary containing:
        - total_links: Total number of links
        - unique_domains: Number of unique domains
        - top_domains: List of tuples with top 5 most common domains and their counts
    """
    # Filter out empty links and extract domains
    valid_links = [link for link in links if link and link.strip()]
    domains = []
    
    for link in valid_links:
        try:
            parsed = urlparse(link)
            if parsed.netloc:
                domains.append(parsed.netloc)
            elif link.startswith('/') or link.startswith('#'):
                # Relative links don't have domains
                continue
            else:
                # Handle cases where scheme might be missing
                parsed = urlparse(f"http://{link}")
                if parsed.netloc:
                    domains.append(parsed.netloc)
        except Exception:
            # Skip malformed URLs
            continue
    
    domain_counts = Counter(domains)
    
    return {
        "total_links": len(valid_links),
        "unique_domains": len(domain_counts),
        "top_domains": domain_counts.most_common(5),
    }
