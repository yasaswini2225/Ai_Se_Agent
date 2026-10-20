# Example: List comprehension and dictionary mapping
languages = ["Python", "JavaScript", "Rust"]
lengths = {lang: len(lang) for lang in languages}
print(lengths) # {'Python': 6, 'JavaScript': 10, 'Rust': 4}