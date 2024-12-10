from openai import OpenAI
import os
from datetime import date

# Load API key from environment variables
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Set 'OPENAI_API_KEY' as an environment variable.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)


class Journal:
    """
    Represents a single journal entry
    """
    def __init__(self, date, mood, gratitude, room_for_growth, thoughts):
        self.date = date
        self.mood = mood
        self.gratitude = gratitude
        self.room_for_growth = room_for_growth
        self.thoughts = thoughts

    def format_entry(self):
        """
        Format the journal entry for saving to a file
        """
        return (
            f"Date: {self.date}\n"
            f"Mood: {self.mood}\n\n"
            f"What went well:\n{self.gratitude}\n\n"
            f"What could have gone better:\n{self.room_for_growth}\n\n"
            f"Thoughts:\n{self.thoughts}\n"
            f"{'-' * 40}\n"
        )


def get_ai_feedback(entry):
    """
    Sends the journal entry to the OpenAI API for analysis and feedback.
    """
    messages = [
        {"role": "system", "content": "You are a wise life coach who gives practical advice."},
        {"role": "user", "content": (
            f"Here's my journal entry for today:\n\n"
            f"Date: {entry.date}\n"
            f"Mood: {entry.mood}\n"
            f"What went well:\n{entry.gratitude}\n"
            f"What could have gone better:\n{entry.room_for_growth}\n"
            f"Thoughts:\n{entry.thoughts}\n\n"
            f"Please provide positive, constructive feedback."
        )}
    ]

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return completion.choices[0].message.content.strip()


def save_entry_to_file(entry, feedback):
    """
    Saves a journal entry to a new file with optional AI feedback.
    """
    timestamp = date.today().strftime("%Y-%m-%d")
    filename = f"journal_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write(entry.format_entry())
        if feedback:
            file.write("\nAI Feedback:\n")
            file.write(feedback)

    print(f"Your journal entry has been saved to {filename}.")


def main():
    """
    Main program function to collect and process a single journal entry.
    """
    print("Welcome to the Journal App!")
    today = date.today().strftime("%Y-%m-%d")
    print("\nLet's reflect on your day:")

    # Collect journal entry details
    mood = input("How are you doing today? (e.g., great, good, meh, bad): ").strip()
    gratitude = input("What are you grateful for today?: ").strip()
    room_for_growth = input("What could have gone better today?: ").strip()
    thoughts = input("What's on your mind?: ").strip()

    # Create the journal entry
    entry = Journal(today, mood, gratitude, room_for_growth, thoughts)

    # Get AI feedback if requested
    feedback_choice = input("Would you like to get AI feedback on your journal entry? (yes/no): ").strip().lower()
    feedback = None
    if feedback_choice == "yes":
        feedback = get_ai_feedback(entry)
        print("\nAI Feedback on your journal entry:")
        print(feedback)
    else:
        print("Skipping AI Feedback.")

    # Save the entry to a file
    save_entry_to_file(entry, feedback)

    print("\nThank you for journaling! Goodbye!")


if __name__ == "__main__":
    main()
