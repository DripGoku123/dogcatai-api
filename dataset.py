import os
import kagglehub
import ai
from PIL import Image
import numpy as np
import kagglehub

# Krok 1: Pobierz zestaw danych
path = kagglehub.dataset_download("jessicali9530/stanford-dogs-dataset")
print("Path to dataset files:", path)
print("Zawartość folderu:", os.listdir(path))

# Krok 2: Ustal folder z obrazami
images_dir = os.path.join(path, 'images\Images')  # Ścieżka do folderu z obrazami
print("Zawartość folderu:", os.listdir(images_dir))
act = 0 
# Krok 3: Dodaj obrazy do bazy danych
for breed_folder in os.listdir(images_dir):
    breed_path = os.path.join(images_dir, breed_folder)  # Ścieżka do folderu rasy
    if os.path.isdir(breed_path):  # Sprawdź, czy to folder
        print(f"Przetwarzanie folderu rasy: {breed_folder}")  # Logowanie rasy
        for filename in os.listdir(breed_path):
            if filename.endswith(('.jpg', '.png')) and act < 200:  # Sprawdź, czy to obraz
                act+=1
                img_path = os.path.join(breed_path, filename)
                with Image.open(img_path) as img:
                        img = img.convert('RGB')  # Konwersja do formatu RGB
                        obraz = np.array(img)  # Konwersja do tablicy NumPy
                        ai.add(obraz, 1) # Dodaj obraz do bazy danych

print("Obrazy zostały dodane do bazy danych.")
print("ilość obrazów: ",act)
import dataset2

