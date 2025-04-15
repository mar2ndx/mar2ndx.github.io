import os
import re
import datetime
from collections import OrderedDict


def sanitize_filename(filename):
    """
    Sanitize filename to contain only alphanumeric chars and dashes.
    """
    # Remove file extension first
    base, ext = os.path.splitext(filename)
    # Replace non-alphanumeric chars (except dashes) with dash
    sanitized = re.sub(r'[^a-zA-Z0-9-]', '-', base)
    # Replace multiple dashes with single dash
    sanitized = re.sub(r'-+', '-', sanitized)
    # Add extension back
    return sanitized + ext


def process_markdown_files(folder_path):
    """
    Processes Markdown files in the given folder, ensuring the frontmatter
    has the required fields in the correct order and renames files to use
    proper formatting.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(".md") or filename.endswith(".markdown"):
            filepath = os.path.join(folder_path, filename)
            
            # Rename file if needed
            new_filename = sanitize_filename(filename)
            if new_filename != filename:
                new_filepath = os.path.join(folder_path, new_filename)
                os.rename(filepath, new_filepath)
                filepath = new_filepath
                print(f"Renamed: {filename} -> {new_filename}")
            
            process_markdown_file(filepath)


def process_markdown_file(filepath):
    """
    Processes a single Markdown file to update its frontmatter.

    Args:
        filepath (str): The path to the Markdown file.
    """

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract existing frontmatter if it exists
        frontmatter_match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
        existing_frontmatter = frontmatter_match.group(1) if frontmatter_match else None

        # Parse existing frontmatter (or create a new one)
        metadata = {}
        if existing_frontmatter:
            lines = existing_frontmatter.splitlines()
            for line in lines:
                if ":" in line:
                    key, value = line.split(":", 1)
                    key = key.strip()
                    value = value.strip()
                    # if key == "tags":
                    #     try:
                    #         metadata[key] = eval(value)
                    #     except:
                    #         metadata[key] = []
                    # else:
                    metadata[key] = value

        # Set default values if fields are missing
        if "title" not in metadata:
            metadata["title"] = "Untitled"
        if "category" not in metadata:
            metadata["category"] = "unknown"
        if "tags" not in metadata:
            metadata["tags"] = []
        if "comments" not in metadata:
            metadata["comments"] = "true"

        # If date not in metadata, try to extract from filename first, then fall back to file time
        if "date" not in metadata:
            filename = os.path.basename(filepath)
            date_match = re.match(r'(\d{4})-(\d{2})-(\d{2})', filename)
            
            if date_match:
                year, month, day = date_match.groups()
                try:
                    parsed_date = datetime.datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
                    metadata["date"] = parsed_date.strftime("%Y-%m-%d %H:%M")
                except ValueError:
                    # If date parsing fails, fall back to file creation time
                    stat = os.stat(filepath)
                    try:
                        creation_time = datetime.datetime.fromtimestamp(stat.st_birthtime)
                    except AttributeError:
                        creation_time = datetime.datetime.fromtimestamp(stat.st_ctime)
                    metadata["date"] = creation_time.strftime("%Y-%m-%d %H:%M")
            else:
                # No date in filename, use file creation time
                stat = os.stat(filepath)
                try:
                    creation_time = datetime.datetime.fromtimestamp(stat.st_birthtime)
                except AttributeError:
                    creation_time = datetime.datetime.fromtimestamp(stat.st_ctime)
                metadata["date"] = creation_time.strftime("%Y-%m-%d %H:%M")

        # Create new frontmatter with ordered fields
        ordered_fields = ["title", "category", "tags", "comments", "date"]
        new_frontmatter = "---\n"
        for field in ordered_fields:
            new_frontmatter += f"{field}: {metadata[field]}\n"
        new_frontmatter += "---\n"

        # Replace the old frontmatter (or add it if it didn't exist)
        if frontmatter_match:
            new_content = re.sub(r"^---\n(.*?)\n---", new_frontmatter, content, flags=re.DOTALL)
        else:
            new_content = new_frontmatter + content

        # Write the updated content back to the file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"Processed: {filepath}")

    except Exception as e:
        print(f"Error processing {filepath}: {e}")


# Example Usage:
if __name__ == "__main__":
    folder_path = "."  # Replace with the actual path to your Markdown folder
    process_markdown_files(folder_path)