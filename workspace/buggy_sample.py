# DevPulse AI - Deliberate Bug Test Case
# Click "Run Code", then click "Debug with AI" to see the agent fix this instantly!

def process_user_records(records):
    total_score = 0
    # BUG: Attempting to access key that doesn't exist for all records without checking
    # or dividing by zero if list is empty
    for user in records:
        print(f"Processing {user['name']}...")
        total_score += user["score"]
        
    avg = total_score / len(records)
    return avg

users = [
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 88},
    {"name": "Charlie"} # Missing 'score' key! Raises KeyError
]

print("Average Score:", process_user_records(users))
