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

    # Список всех объектов в бакете
    print('Все файлы:\n')
    print(f"Объекты в бакете '{bucket_name}':\n")
    objects = client.list_objects(bucket_name, recursive=True)
    list_error = []
    find_time = '2024-05-27'  # дата по которой ищем загрузки
    find_file = '2024-05-26.csv'  # файл который будем искать во всех папках

    counter = 0
    for obj in objects:
        name_file = obj.object_name
        date = client.stat_object(bucket_name, name_file).last_modified
        print(name_file)
        print(f'date_modification: {date}\n')
        cut_date_load_file = date.strftime('%Y-%m-%d')[:10]
        if name_file.endswith('.csv'):  # проверка на csv
            cut_date_from_name_file = name_file[-14:-4]
            if name_file.endswith('file_n.csv') == False:  # не берем файлы file_n.csv
                if cut_date_load_file != cut_date_from_name_file:  # проверка на дату загрузки и дату в имени
                    list_error.append(f'{name_file}_DateLoad_DateName_error')
        else:
            list_error.append(f'{name_file}_error_format')
        if find_time != cut_date_load_file and counter == 0:  # проверка на загрузку данных по указанной дате
            list_error.append('Данных нет по указанной дате')
        counter += 1
        # 0 1 2 3 - задание до сюда сделал

        # 4ое задание пошло отсюда
        first_part = obj.object_name[:obj.object_name.find('/')]  # названия первых папок без слеша
        second_part = obj.object_name[obj.object_name.index('/'):]  # названия вторых папок и файлов со слэшем
        second_dir_name = second_part[1:second_part.index('/', 1)]  # чисто назвагия 2ых папок
        file_path = f'{first_part}/{second_dir_name}/{find_file}'  # полное название искомого файла
        # print(file_path)
        try:
            client.stat_object(bucket_name, file_path)
        except S3Error as err:
            if err.code == "NoSuchKey" and f"{file_path}_not_find_in_all_dir" not in list_error:  # чтобы запись оишбок повторялась
                list_error.append(f'{file_path}_not_find_in_all_dir')
            else:
                print("Произошла ошибка:", err)
    print('\nОшибки:\n')
    for i in list_error:
        print(i)


if __name__ == "__main__":
    main()
