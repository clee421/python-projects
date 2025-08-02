import json
import csv
from pathlib import Path


def save_report(links: list[str], summary: dict, output_format: str = "text", filename: str = "report"):
    """
    Save the links and summary to a file in the specified format.
    
    Args:
        links: List of extracted links
        summary: Dictionary containing link statistics
        output_format: Output format - 'text', 'json', or 'csv'
        filename: Base filename (without extension)
    """
    output_path = Path(filename)
    
    if output_format.lower() == "json":
        output_file = output_path.with_suffix(".json")
        with open(output_file, "w") as f:
            json.dump({
                "summary": summary,
                "links": links
            }, f, indent=2)
        print(f"Report saved to {output_file}")
        
    elif output_format.lower() == "csv":
        output_file = output_path.with_suffix(".csv")
        with open(output_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["metric", "value"])
            writer.writerow(["total_links", summary["total_links"]])
            writer.writerow(["unique_domains", summary["unique_domains"]])
            writer.writerow(["", ""])
            writer.writerow(["top_domains", "count"])
            for domain, count in summary["top_domains"]:
                writer.writerow([domain, count])
            writer.writerow(["", ""])
            writer.writerow(["all_links", ""])
            for link in links:
                writer.writerow([link, ""])
        print(f"Report saved to {output_file}")
        
    else:  # Default to text format
        output_file = output_path.with_suffix(".txt")
        with open(output_file, "w") as f:
            f.write("Summary:\n")
            f.write(f"total_links: {summary['total_links']}\n")
            f.write(f"unique_domains: {summary['unique_domains']}\n")
            f.write(f"top_domains: {summary['top_domains']}\n")
            f.write("\nLinks:\n")
            for link in links:
                f.write(f"{link}\n")
        print(f"Report saved to {output_file}")
