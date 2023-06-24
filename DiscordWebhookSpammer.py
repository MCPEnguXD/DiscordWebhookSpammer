import tkinter as tk
import requests
import json

def send_message_to_discord_webhook(webhook_url, message, num_times):
    data = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    for _ in range(num_times):
        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
        if response.status_code != 204:
            print(f"Failed to send message. Error: {response.text}")
        else:
            print("Message sent successfully!")

def send_message():
    webhook_url = url_entry.get()
    message = message_entry.get()
    num_times = int(num_entry.get())
    send_message_to_discord_webhook(webhook_url, message, num_times)

# Create the main window
window = tk.Tk()
window.title("Discord Webhook Sender")

# Create URL label and entry
url_label = tk.Label(window, text="Webhook URL:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Create message label and entry
message_label = tk.Label(window, text="Message:")
message_label.pack()
message_entry = tk.Entry(window, width=50)
message_entry.pack()

# Create number of times label and entry
num_label = tk.Label(window, text="Number of times:")
num_label.pack()
num_entry = tk.Entry(window, width=10)
num_entry.pack()

# Create send button
send_button = tk.Button(window, text="Send Message", command=send_message)
send_button.pack()

# Start the GUI event loop
window.mainloop()
