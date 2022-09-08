import requests
x, y = input("Введите первые координаты: "), input("Введите вторые коордианты: ")
while True:
    try:
        image = requests.get(f"https://static-maps.yandex.ru/1.x/?ll={y},{x}&spn=0.006,0.006&l=map")
        with open("image.png", "wb") as file:
            file.write(image.content)
        print("Изображение сохранено: image.png")
        print()
    except Exception:
        print("Неверные координаты!")
    finally:
        x, y = input("Введите первые координаты: "), input("Введите вторые коордианты: ")

# 47.409318, 47.252063