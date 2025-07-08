from api.vulnerability_db import query_vulnerability
from utils.notifications import create_trello_task, send_email

def handle_user_input(user_input):
    if "CVE" in user_input:
        cve_id = user_input.split(" ")[-1]
        details = query_vulnerability(cve_id)
        card_id = create_trello_task(details)
        send_email(details, card_id)