text = input('Input: ')


def get_domains(text: str) -> list[str]:
    emails = text.split(',')
    
    domains = []
    for email in emails:
        idx = email.find('@')
        if idx != -1:
            domain = email[idx:]
            domains.append(domain)

    return domains


domains = get_domains(text=text)
print(domains)
