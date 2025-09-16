# Very small sentiment heuristic. Replace with a proper library for production.
def classify(text: str) -> str:
    t = text.lower()
    if any(w in t for w in ['excellent','great','thank','love','happy']):
        return 'positive'
    if any(w in t for w in ['terrible','bad','angry','hate','poor','urgent']):
        return 'negative'
    return 'neutral'
