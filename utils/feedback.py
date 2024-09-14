import difflib

def generate_feedback(user_input, expected_input):
    diff = difflib.ndiff(expected_input.split(), user_input.split())
    return "\n".join(diff)
