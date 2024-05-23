import os
from minio import Minio
from minio.error import S3Error


def upload_files(client, bucket_name, source_folder):
    # Проходим по всем директориям и файлам в указанной папке
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)  # Полный путь к файлу
            object_name = os.path.relpath(file_path, source_folder)  # Относительный путь для объекта в бакете
            client.fput_object(bucket_name, object_name, file_path)  # Загрузка файла в бакет
            print(f"Загружен {file_path} как {object_name} в бакет {bucket_name}")


def main():
    # Создаем клиента для подключения к MinIO серверу с указанными ключами доступа
    client = Minio("play.min.io",
                   access_key="Q3AM3UQ867SPQQA43P2F",
                   secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
                   )

    # Папка для заугрузки
    source_folder = "./test_dir"

    # Название бакета
    bucket_name = "python-test-bucket"

    # Проверяем, существует ли бакет , если не тто создаем
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print(f"Бакет {bucket_name} создан")
    else:
        print(f"Бакет {bucket_name} уже существует")

    # Загружаем файлы в бакет
    # upload_files(client, bucket_name, source_folder)

    # ДАТА ПО КОТОРОЙ ИЩЕМ
    find_time = '2024-05-23'

    # Список всех объектов в бакете
    print('Все файлы:\n')
    print(f"Объекты в бакете '{bucket_name}':\n")
    objects = client.list_objects(bucket_name, recursive=True)
    for obj in objects:
        name_file = obj.object_name
        date = client.stat_object(bucket_name, name_file).last_modified
        if name_file.endswith('.csv'):
            print(name_file)
            print(date)
            cut_date_load_file = date.strftime('%Y-%m-%d')[:10]
            cut_date_from_name_file = name_file[-14:-4]
            if cut_date_load_file != cut_date_from_name_file:
                print('Даты не соответсвуют\n')
            else:
                print('Даты соответсвуют\n')
        else:
            print(name_file, ' - не .csv')
            print(date)


if __name__ == "__main__":
    main()
