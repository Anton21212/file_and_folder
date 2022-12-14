# FILE AND FOLDER

Приложение для получения информации о папках и файлах

## Установка

1. Склонировать репозиторий с помощью команды:

```shell
git clone https://github.com/Anton21212/file_and_folder.git
```

2. Перейти в папку проекта.

## Запуск

```shell
sudo docker-compose -p "file_and_folder" --file "docker-compose.yml" up --build
```

## Использование

Для получения информации используется эндпоинт `http://127.0.0.1:82/api/meta`. Для обращения к нему
нужно выполнять `GET` запросы.

Успешным результатом работы API является возврат имени файле или директории, типа файла или директории и дата создания в
Unix формате.

Примеры ответов:

```json
{
    "data": [
        {
            "name": "1.txt",
            "type": "file",
            "time": 1666614330072
        },
        {
            "name": "2",
            "type": "folder",
            "time": 1666615444492
        }
    ]
}
```

## Автор

Васильев Антон Юрьевич

sortof00@mail.ru