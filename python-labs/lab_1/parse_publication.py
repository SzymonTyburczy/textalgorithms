import re
from typing import Optional


def parse_publication(reference: str) -> Optional[dict]:
    """
    Parse academic publication reference and extract structured information.

    Expected reference format:
    Lastname, I., Lastname2, I2. (Year). Title. Journal, Volume(Issue), StartPage-EndPage.

    Example:
    Kowalski, J., Nowak, A. (2023). Analiza algorytmów tekstowych. Journal of Computer Science, 45(2), 123-145.

    Args:
        reference (str): Publication reference string

    Returns:
        Optional[dict]: A dictionary containing parsed publication data or None if the reference doesn't match expected format
    """
    # TODO: Implement regex patterns to match different parts of the reference
    # You need to create patterns for:
    # 1. Authors and year pattern
    # 2. Title and journal pattern
    # 3. Volume, issue, and pages pattern
    authors_year_pattern = r"((?:[A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż]+,\s*[A-Z]\.\s*(?:,\s*)?)+)\s*\((\d{4})\)\."

    title_journal_pattern = r"(.*?)\.\s+(.*)"
    volume_issue_pages_pattern = r"(\d+)(?:\((\d+)\))?, (\d+)-(\d+)"

    # TODO: Combine the patterns
    full_pattern = r"^" + authors_year_pattern + r"\s+" + title_journal_pattern + r",\s+" + volume_issue_pages_pattern + r"\.$"

    # TODO: Use re.match to try to match the full pattern against the reference
    # If there's no match, return None
    m = re.match(full_pattern, reference)
    if not m:
        return None

    # TODO: Extract information using regex
    # Each author should be parsed into a dictionary with 'last_name' and 'initial' keys
    authors_str = m.group(1)
    year = m.group(2)
    title = m.group(3)
    journal = m.group(4)
    volume = m.group(5)
    issue = m.group(6)
    start_page = m.group(7)
    end_page = m.group(8)
    authors_list = []

    # TODO: Create a pattern to match individual authors
    author_pattern = r"([A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż]+),\s*([A-Z])\."

    # TODO: Use re.finditer to find all authors and add them to authors_list
    for author_match in re.finditer(author_pattern, authors_str):
        last_name = author_match.group(1)
        initial = author_match.group(2)
        authors_list.append({'last_name': last_name, 'initial': initial})

    # TODO: Create and return the final result dictionary with all the parsed information
    # It should include authors, year, title, journal, volume, issue, and pages

    result = {
        "authors": authors_list,
        "year": int(year),
        "title": title.strip(),
        "journal": journal.strip(),
        "volume": int(volume),
        "issue": int(issue) if issue is not None else None,
        "pages": {'start': int(start_page), 'end': int(end_page)}
    }

    return result

