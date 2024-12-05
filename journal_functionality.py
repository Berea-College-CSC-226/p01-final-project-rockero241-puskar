import os
from datetime import date
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Fetch the key from .env

# Validate API key
if not OPENAI_API_KEY:
    raise ValueError("API key not found. Make sure it is set in the .env file.")

openai.api_key = OPENAI_API_KEY  # Set the OpenAI API key

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
        :return:
        """
        return (
            f"Date: {self.date}\n"
            f"Mood: {self.mood}\n\n"
            f"What went well:\n{self.gratitude}\n\n"
            f"What could have gone better:\n{self.room_for_growth}\n\n"
            f"Thoughts:\n{self.thoughts}\n"
            f"{'-' * 40}\n"
        )

class JournalApp:
    """
    Controls the main program flow for the journal application.
    """

    def __init__(self):
        self.entries = []

    def run(self):
        """
        Main program loop.
        """
        print("Welcome to the Journal App!")
        while True:
            # To display the menu
            print("\nMenu:")
            print("1. Write a new journal entry")
            print("2. Exit")

            # Getting the user's choice
            choice = input("Choose an option (1 or 2): ").strip()

            if choice == "1":
                # Create and save a new journal entry
                entry = self.create_entry()


                feedback_choice = int(input("Would you like to get AI feedback on your journal entry?\n(1 = Yes, 0 = No): "))
                feedback = None
                while (feedback_choice != 1) and (feedback_choice != 0):
                    feedback_choice = int(input("Would you like to get AI feedback on your journal entry?\n(1 = Yes, 0 = No): "))
                if feedback_choice == 1:
                    feedback = self.get_ai_feedback(entry)
                    print("\nAI Feedback on your journal entry:")
                    print(feedback)
                else:
                    print("Skipping AI Feedback")

                self.save_entry_to_file(entry, feedback)
            elif choice == "2":
                # Exit the program
                print("Goodbye! Have a great time")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def create_entry(self):
        """
        Collects user input to create a new journal entry.
        """
        # Get the current date
        today = date.today().strftime("%Y-%m-%d")
        print("\nLet's reflect on your day:")
        mood = input("How are you doing today? (great, good, meh, bad): ").strip()
        gratitude = input("What are you grateful for today?: ").strip()
        room_for_growth = input("What could have gone better today?: ").strip()
        thoughts = input("What's on your mind?: ").strip()

        # Create a Journal object to represent the entry
        entry = Journal(today, mood, gratitude, room_for_growth, thoughts)
        self.entries.append(entry)
        print("Your journal entry has been created!")
        return entry

    def get_ai_feedback(self, entry):
        """
        Sends the journal entry to the OpenAI API for analysis and feedback.
        """
        try:
            # Construct the prompt as a list of messages
            messages = [
                {"role": "system",
                 "content": "You are a helpful assistant that provides constructive feedback on journal entries."},
                {"role": "user", "content": (
                    f"Analyze the following journal entry and provide feedback:\n\n"
                    f"Date: {entry.date}\n"
                    f"Mood: {entry.mood}\n"
                    f"What went well:\n{entry.gratitude}\n"
                    f"What could have gone better:\n{entry.room_for_growth}\n"
                    f"Thoughts:\n{entry.thoughts}\n\n"
                    f"Provide positive, constructive feedback and suggest improvements."
                )}
            ]

            # Call the OpenAI ChatCompletion API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
                messages=messages,
                max_tokens=150,
                temperature=0.7
            )

            # Return the AI feedback from the response
            return response['choices'][0]['message']['content'].strip()

        except Exception as e:
            # Catch and return any errors
            return f"Error during AI API call: {e}"


    def save_entry_to_file(self, entry, feedback):
        """
        Saves a journal entry to a new file with a unique timestamp.
        """
        # Use the current date and time for a unique filename
        timestamp = date.today().strftime("%Y-%m-%d")
        filename = f"journal_{timestamp}.txt"

        # Writing the formatted entry to the file
        with open(filename, "w") as file:
            file.write(entry.format_entry())
            if feedback:
                file.write("\nAI Feedback:\n")
                file.write(feedback)

        print(f"Your journal entry has been saved to {filename}.")

if __name__ == "__main__":
    app = JournalApp()
    app.run()