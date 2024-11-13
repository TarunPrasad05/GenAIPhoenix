def getResponse(subIssue):
    match subIssue:
        case "Credit card company won't increase or decrease your credit limit":
            return "Handling 'Credit card company won't increase or decrease your credit limit'"
        case "Can't use card to make purchases":
            return "Handling 'Can't use card to make purchases'"
        case "Problem with direct deposit":
            return "Handling 'Problem with direct deposit'"
        case "Trouble using the card to spend money in a store or online":
            return "Handling 'Trouble using the card to spend money in a store or online'"
        case "Trouble getting information about the card":
            return "Handling 'Trouble getting information about the card'"
        case "Trouble using the card to pay a bill":
            return "Handling 'Trouble using the card to pay a bill'"
        case "Problem using the card to withdraw money from an ATM":
            return "Handling 'Problem using the card to withdraw money from an ATM'"
        case "Account sold or transferred to another company":
            return "Handling 'Account sold or transferred to another company'"
        case "Problem with a check written from your prepaid card account":
            return "Handling 'Problem with a check written from your prepaid card account'"
        case "Trouble using the card to send money to another person":
            return "Handling 'Trouble using the card to send money to another person'"
        case "Problem adding money":
            return "Handling 'Problem adding money'"
        case _:
            return "Please try this"