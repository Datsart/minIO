import os

# Определяем структуру директорий и файлов
structure = {
    "deals": {
        "Краснодарский край": ["2024-05-26.cs", "file_n.csv"],  # не csv
        "Ленинградская область": ["file_n.csv"],  # тут нет
        "Московская область": ["2024-05-26.csv", "file_n.csv"],
        "Омская область": ["2024-05-26.csv", "file_n.csv"],
        "Калужская область": ["2024-05-26.csv", "file_n.csv"],
    },
    "full_objects": {
        "Краснодарский край": ["2024-05-26.csv", "file_n.csv"],
        "Ленинградская область": ["2024-05-26.csv", "file_n.csv"],
        "Московская область": ["2024-05-26.csv", "file_n.csv"],
        "Омская область": ["2024-05-26.csv", "file_n.csv"],
        "Калужская область": ["2024-05-26.csv", "file_n.csv"],
    },
    "analytics": {
        "Краснодарский край": ["file_n.csv"],  # тут нет
        "Ленинградская область": ["2024-05-26.csv", "file_n.csv"],
        "Московская область": ["2024-05-26.csv", "file_n.csv"],
        "Омская область": ["2024-05-26.csv", "file_n.csv"],
        "Калужская область": ["2024-05-26.csv", "file_n.csv"],
    },
    "prices": {
        "Краснодарский край": ["2024-05-26.csv", "file_n.csv"],
        "Ленинградская область": ["2024-05-26.csv", "file_n.csv"],
        "Московская область": ["2024-05-26.csv", "file_n.csv"],
        "Омская область": ["2024-05-26.csv", "file_n.csv"],
        "Калужская область": ["2024-05-26.csv", "file_n.csv"],
    }
}


# Функция для создания структуры директорий и файлов
def create_structure(base_path, structure):
    for folder, subfolders in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

        for subfolder, files in subfolders.items():
            subfolder_path = os.path.join(folder_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)

            for file in files:
                file_path = os.path.join(subfolder_path, file)
                with open(file_path, 'w') as f:
                    pass  # Создаем пустой файл


# Путь к базовой директории (например, рабочая директория проекта в PyCharm)
base_path = "./test_dir"

# Создаем структуру директорий и файлов
create_structure(base_path, structure)
