import re
from collections import Counter


def analyze_text_file(filename: str) -> dict:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    except Exception as e:
        return {"error": f"Could not read file: {str(e)}"}

    # Common English stop words to filter out from frequency analysis
    stop_words = {
        "the",
        "a",
        "an",
        "and",
        "or",
        "but",
        "in",
        "on",
        "at",
        "to",
        "for",
        "with",
        "by",
        "about",
        "as",
        "into",
        "like",
        "through",
        "after",
        "over",
        "between",
        "out",
        "of",
        "is",
        "are",
        "was",
        "were",
        "be",
        "been",
        "being",
        "have",
        "has",
        "had",
        "do",
        "does",
        "did",
        "this",
        "that",
        "these",
        "those",
        "it",
        "its",
        "from",
        "there",
        "their",
    }

    # TODO: Implement word extraction using regex
    # Find all words in the content (lowercase for consistency)
    words = re.findall(r'\b\w+\b', content.lower())
    word_count = len(words)

    # TODO: Implement sentence splitting using regex
    # A sentence typically ends with ., !, or ? followed by a space
    # Be careful about abbreviations (e.g., "Dr.", "U.S.A.")
    sentences = re.split(r'(?<=[.!?])\s+', content.strip())
    sentence_count = len([s for s in sentences if s.strip()])

    # TODO: Implement email extraction using regex
    # Extract all valid email addresses from the content
    email_pattern = r'\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b'
    emails = re.findall(email_pattern, content)

    # TODO: Calculate word frequencies
    # Count occurrences of each word, excluding stop words and short words
    # Use the Counter class from collections
    filtered_words = [w for w in words if w not in stop_words and len(w) > 2]
    counter = Counter(filtered_words)
    # Get the 10 most common words as a dictionary
    frequent_words = dict(counter.most_common(10))

    # TODO: Implement date extraction with multiple formats
    # Detect dates in various formats: YYYY-MM-DD, DD.MM.YYYY, MM/DD/YYYY, etc.
    # Create multiple regex patterns for different date formats
    date_patterns = [
        r'\b\d{4}-\d{2}-\d{2}\b',  # e.g. 2023-09-15 (YYYY-MM-DD)
        r'\b\d{2}\.\d{2}\.\d{4}\b',  # e.g. 15.03.2023 (DD.MM.YYYY)
        r'\b\d{2}/\d{2}/\d{4}\b',  # e.g. 01/05/2022 (MM/DD/YYYY)
        r'\b\d{2}-\d{2}-\d{4}\b',  # e.g. 11-22-2023 (MM-DD-YYYY)
        r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b',
        # e.g. May 23, 1977
    ]
    dates = []
    for pattern in date_patterns:
        found_dates = re.findall(pattern, content)
        dates.extend(found_dates)
    # TODO: Analyze paragraphs
    # Split the content into paragraphs and count words in each
    # Paragraphs are typically separated by one or more blank lines
    paragraphs = re.split(r'\n\s*\n', content.strip())
    paragraph_sizes = {}
    for i, para in enumerate(paragraphs):
        # Count words in each paragraph
        para_words = re.findall(r'\b\w+\b', para)
        paragraph_sizes[f'Paragraph {i + 1}'] = len(para_words)

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "emails": emails,
        "frequent_words": frequent_words,
        "dates": dates,
        "paragraph_sizes": paragraph_sizes,
    }
