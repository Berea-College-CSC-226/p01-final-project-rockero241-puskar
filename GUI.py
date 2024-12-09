import tkinter as tk
import openai

# Set your OpenAI API key
openai.api_key = "your-api-key-here"  # Replace with your actual key


def get_response():
    # Get the text the user typed in
    user_prompt = prompt_entry.get()

    try:
        # Call the OpenAI API with the user's prompt
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_prompt}],
            max_tokens=100
        )

        # Get the response content
        result = response['choices'][0]['message']['content']

        # Show the response in the text box
        response_box.config(state=tk.NORMAL)  # Allow editing to update text
        response_box.delete(1.0, tk.END)  # Clear the box first
        response_box.insert(tk.END, result)  # Add the result
        response_box.config(state=tk.DISABLED)  # Make it read-only again
    except Exception as e:
        # If there's an error, display it
        response_box.config(state=tk.NORMAL)
        response_box.delete(1.0, tk.END)
        response_box.insert(tk.END, f"Error: {e}")
        response_box.config(state=tk.DISABLED)


# Create the main window
root = tk.Tk()
root.title("OpenAI Chat")

# Create a label for the prompt
prompt_label = tk.Label(root, text="Enter your prompt:")
prompt_label.pack(pady=5)

# Create an entry box for the user to type their prompt
prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack(pady=5)

# Create a button to get the response
submit_button = tk.Button(root, text="Get Response", command=get_response)
submit_button.pack(pady=5)

# Create a text box to show the response
response_box = tk.Text(root, height=10, width=50, state=tk.DISABLED, wrap=tk.WORD)
response_box.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
