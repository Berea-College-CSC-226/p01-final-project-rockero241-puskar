import os, date
from datetime

class Journal:
    """
    Represents a single journal entry
    """
    def __init__(self, date, mood, grattitude, room_for_growth, thoughts):
        self.date = date
        self.mood = mood
        self.grattitude = grattitude
        self.room_for_growth = room_for_growth
        self.thoughts = thoughts

    def format_entry(self):
        """
        Format the journal entry for saving to a file
        :return:
        """
        return {
            f"Date: {self.date}\n"
            f"Mood: {self.mood}\n\n"
            f"What went well:\n{self.what_went_well}\n\n"
            f"What could have gone better:\n{self.what_could_be_better}\n\n"
            f"Thoughts:\n{self.thoughts}\n"
            f"{'-' * 40}\n"
        }





































class Write:






















































































def main():
    pass

main()