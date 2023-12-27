```python
class Feedback:
    def __init__(self):
        self.feedback_data = []

    def collect(self, code, user_feedback):
        """Collect user feedback on the generated code."""
        feedback_entry = {
            "code": code,
            "feedback": user_feedback
        }
        self.feedback_data.append(feedback_entry)

    def get_all_feedback(self):
        """Return all collected feedback."""
        return self.feedback_data

    def get_positive_feedback(self):
        """Return all positive feedback."""
        return [entry for entry in self.feedback_data if entry["feedback"].lower() == "positive"]

    def get_negative_feedback(self):
        """Return all negative feedback."""
        return [entry for entry in self.feedback_data if entry["feedback"].lower() == "negative"]

    def get_feedback_on_code(self, code):
        """Return all feedback on a specific piece of code."""
        return [entry for entry in self.feedback_data if entry["code"] == code]
```
