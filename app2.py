import os
from minio import Minio
from minio.error import S3Error


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

    # проверка файлов по указанной дате
    objects2 = client.list_objects(bucket_name, recursive=True)
    for o in objects2:
        date = client.stat_object(bucket_name, o.object_name).last_modified
        if find_time == date.strftime('%Y-%m-%d')[:10]:
            name_file = o.object_name
            if name_file.endswith('.csv'):
                print(name_file)
                print(date)
                cut_date_load_file = date.strftime('%Y-%m-%d')[:10]
                cut_date_from_name_file = name_file[-14:-4]

                if cut_date_load_file != cut_date_from_name_file:
                    print('Даты не соответсвуют')
                else:
                    print('Даты соответсвуют')
            else:
                print(name_file, ' - не .csv')
                print(date)
            print('\n')
        else:
            print('Таких файлов нет по указанной дате')
            break
    # проверка на существование во всех папках


if __name__ == "__main__":
    main()
