import re

def extract_legal_citations(text):
    citations = set()

    # IPC Sections (e.g., Section 420 IPC or Section 302 of the Indian Penal Code)
    ipc_matches = re.findall(r'Section\s+\d+\s+(?:IPC|of the Indian Penal Code)', text, re.IGNORECASE)
    citations.update(ipc_matches)

    # CrPC Sections (e.g., Section 161 CrPC)
    crpc_matches = re.findall(r'Section\s+\d+\s+(?:CrPC|of the Criminal Procedure Code)', text, re.IGNORECASE)
    citations.update(crpc_matches)

    # Articles (e.g., Article 21, Article 14)
    article_matches = re.findall(r'Article\s+\d+', text, re.IGNORECASE)
    citations.update(article_matches)

    # Other Acts (e.g., The Companies Act, 2013)
    act_matches = re.findall(r'The\s+[A-Z][\w\s]+?Act(?:,\s*\d{4})?', text)
    citations.update(act_matches)

    # Case laws (e.g., AIR 1962 SC 123, (2009) 8 SCC 1)
    case_matches = re.findall(r'(?:AIR\s+\d{4}\s+SC\s+\d+|\(\d{4}\)\s+\d+\s+SCC\s+\d+)', text)
    citations.update(case_matches)

    return sorted(citations)
