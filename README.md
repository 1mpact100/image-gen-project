# image-gen-project

Простой Python-скрипт для генерации изображения через Hugging Face Inference API.
В проекте используется модель `black-forest-labs/FLUX.1-schnell`.

## Что делает программа

Скрипт `index.py`:

- получает токен Hugging Face из переменной окружения `HF_TOKEN`;
- создает клиент `InferenceClient`;
- отправляет текстовый запрос в модель `black-forest-labs/FLUX.1-schnell`;
- сохраняет результат в файл `generated_image.png`.

## Установка

Создайте и активируйте виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

## Настройка токена

Создайте токен доступа в Hugging Face и передайте его программе через переменную окружения:

```bash
export HF_TOKEN="ваш_токен_hugging_face"
```

Не добавляйте токен напрямую в `index.py` и не пушьте его в Git.

## Запуск

Запустите программу из корня проекта:

```bash
python index.py
```

После успешного выполнения рядом с `index.py` появится файл:

```text
generated_image.png
```

В консоли будет выведено сообщение:

```text
Изображение успешно сохранено как 'generated_image.png'.
```
