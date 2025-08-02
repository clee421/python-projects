import argparse
import sys
from webscrape_reporter.scraper.fetcher import fetch_url
from webscrape_reporter.scraper.parser import parse_html
from webscrape_reporter.reports.formatter import save_report
from webscrape_reporter.reports.statistics import summarize


def main():
    """Main CLI entrypoint for webscrape-reporter."""
    parser = argparse.ArgumentParser(
        description="Scrape a website and generate a report of all hyperlinks found."
    )
    parser.add_argument("url", help="Target URL to scrape")
    parser.add_argument(
        "--format", 
        choices=["json", "csv", "text"], 
        default="text",
        help="Output format for the report (default: text)"
    )
    parser.add_argument(
        "--output", 
        default="report",
        help="Output filename (without extension, default: report)"
    )
    
    args = parser.parse_args()
    
    try:
        print(f"Fetching URL: {args.url}")
        html = fetch_url(args.url)
        
        print("Parsing HTML for links...")
        links = parse_html(html)
        
        print("Generating statistics...")
        summary = summarize(links)
        
        # Print summary to console
        print("\nSummary:")
        print(f"total_links: {summary['total_links']}")
        print(f"unique_domains: {summary['unique_domains']}")
        print(f"top_domains: {summary['top_domains']}")
        
        print(f"\nLinks:")
        for link in links[:10]:  # Show first 10 links
            print(link)
        if len(links) > 10:
            print(f"... and {len(links) - 10} more links")
        
        print(f"\nSaving report in {args.format} format...")
        save_report(links, summary, output_format=args.format, filename=args.output)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
