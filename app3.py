from minio import Minio
from minio.error import S3Error


def main():
    # Создаем клиента для подключения к MinIO серверу с указанными ключами доступа
    client = Minio("play.min.io",
                   access_key="Q3AM3UQ867SPQQA43P2F",
                   secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
                   )

    # Название бакета
    bucket_name = "python-test-bucket"

    # Проверяем, существует ли бакет, если нет, то создаем
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print(f"Бакет {bucket_name} создан")
    else:
        print(f"Бакет {bucket_name} уже существует")

    # файл который мы будем искать
    find_file = '2024-02-16.csv'
    objects = client.list_objects(bucket_name, prefix='', recursive=True)
    list_error = []

    for obj in objects:
        first_part = obj.object_name[:obj.object_name.find('/')]  # названия первых папок без слеша
        second_part = obj.object_name[obj.object_name.index('/'):]  # названия вторых папок и файлов со слэшем
        second_dir_name = second_part[1:second_part.index('/', 1)]  # чисто назвагия 2ых папок
        file_path = f'{first_part}/{second_dir_name}/{find_file}'  # полное название искомого файла
        # print(file_path)
        try:
            client.stat_object(bucket_name, file_path)
        except S3Error as err:
            if err.code == "NoSuchKey":
                list_error.append(f'{file_path}_error')
            else:
                print("Произошла ошибка:", err)

    for i in list_error:
        print(i)


if __name__ == "__main__":
    main()
