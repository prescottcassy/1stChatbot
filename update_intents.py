import os
import json

# Define folder path and file names
folder_path = "/home/cassy-cormier/chatbot_project/archive"
file_names = ["input_text.txt", "dialog.txt", "label_texts.txt"]

# Load existing intents.json
intents_file = "/home/cassy-cormier/chatbot_project/intents.json"
with open(intents_file, "r") as f:
    data = json.load(f)

# Iterate through specified files and add their content
for filename in file_names:
    file_path = os.path.join(folder_path, filename)

    if os.path.exists(file_path):  # Ensure file exists
        with open(file_path, "r") as f:
            lines = f.readlines()

        # Create structured intent
        new_intent = {
            "tag": filename.replace(".txt", ""),  # Use file name as intent tag
            "patterns": [line.strip() for line in lines if line.strip()],  # Extract lines
            "responses": [f"Generic response for {filename.replace('.txt', '')}"]
        }

        data["intents"].append(new_intent)
    else:
        print(f"Warning: {filename} not found in {folder_path}")

# Save updated `intents.json`
with open(intents_file, "w") as f:
    json.dump(data, f, indent=4)

print("Updated intents.json with all files successfully!")
