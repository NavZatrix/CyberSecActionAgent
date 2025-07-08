def create_trello_task(details):
    print(f"Trello card created: Investigate {details['cve_id']}")
    return "simulated_card_id"

def send_email(details, card_id):
    print(f"Email sent to security_team@example.com regarding {details['cve_id']}")