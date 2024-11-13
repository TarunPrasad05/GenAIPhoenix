from genai import getGenAiResponse

def getResponse(subIssue):
    return getGenAiResponse(subIssue)

def getMockResponsee(subIssue):
    match subIssue:
        case "Credit card company won't increase or decrease your credit limit":
            return "Contact your credit card company's customer service to formally request a credit limit change and provide any necessary documentation to support your request."
        case "Can't use card to make purchases":
            return "Contact your credit card company's customer service to check for any holds, restrictions, or issues with your account and resolve them promptly."
        case "Problem with direct deposit":
            return "Verify your account and routing numbers with your employer or the depositing entity, and contact your bank's customer service to ensure there are no issues with your account receiving direct deposits."
        case "Trouble using the card to spend money in a store or online":
            return "Contact your card issuer to check for account restrictions or blocks."
        case "Trouble getting information about the card":
            return "Contact your card issuer's customer service for detailed information about your card."
        case "Trouble using the card to pay a bill":
            return "Verify card details and account balance, and contact customer service for assistance."
        case "Problem using the card to withdraw money from an ATM":
            return "Check your account balance and ensure your card is activated; contact customer service for further assistance."
        case "Account sold or transferred to another company":
            return "Contact the new company managing your account for details and next steps."
        case "Problem with a check written from your prepaid card account":
            return "Contact your prepaid card issuer's customer service for assistance with the check issue."
        case "Trouble using the card to send money to another person":
            return "Ensure you have sufficient funds and correct recipient details; contact your card issuer for further assistance."
        case "Problem adding money":
            return "Verify your funding source and ensure it's correctly linked; contact customer support for troubleshooting."
        case _:
            return "Please try again"
