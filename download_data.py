from datasets import load_dataset
import os

# Define save path
save_path = "C:/Users/SIVA RAM/PycharmProjects/PythonProject/ValorantAimbot/valorant_data"
os.makedirs(save_path, exist_ok=True)

# Load dataset
print("Downloading Valorant dataset...")
ds = load_dataset("keremberke/valorant-object-detection", "full")

# Save to disk
print("Saving to", save_path)
ds["train"].save_to_disk(save_path)
print("Download complete! Saved to", save_path)


for i in range(5):
    img = ds["train"][i]["image"]
    img.save(f"preview_{i}.jpg")
    print(f"Saved preview_{i}.jpg")