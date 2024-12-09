import os
import kagglehub
import ai
from PIL import Image
import numpy as np

# Download latest version
path = kagglehub.dataset_download("crawford/cat-dataset")

print("Path to dataset files:", path)

print("Zawartość folderu:", os.listdir(path))
act = 0 

# Krok 3: Dodaj obrazy do bazy danych
for breed_folder in os.listdir(path):
    breed_path = os.path.join(path, breed_folder)  # Ścieżka do folderu rasy
    if os.path.isdir(breed_path):  # Sprawdź, czy to folder
        print(f"Przetwarzanie folderu rasy: {breed_folder}")  # Logowanie rasy
        for filename in os.listdir(breed_path):
            if filename.endswith(('.jpg', '.png')) and act < 200:  # Sprawdź, czy to obraz
                img_path = os.path.join(breed_path, filename)
                act+=1
                with Image.open(img_path) as img:
                        img = img.convert('RGB')  # Konwersja do formatu RGB
                        obraz = np.array(img)  # Konwersja do tablicy NumPy
                        ai.add(obraz, 2) # Dodaj obraz do bazy danych

print("Obrazy zostały dodane do bazy danych.")
print("ilość obrazów: ",act)
