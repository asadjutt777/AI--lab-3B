def rule_based(score, documents_complete, interview_passed, fee_paid):
    if documents_complete and score >= 70 and interview_passed and fee_paid:
        return "Review"
    else:
        return "Hold"

def probability_based(probability): 
    return "Review" if probability >= 0.70 else "Hold"

print(rule_based(76, True, True, True))
print(rule_based(69, True, True, True))
print(rule_based(92, True, False, True))
print(rule_based(62, True, True, False))
print(probability_based(0.76))