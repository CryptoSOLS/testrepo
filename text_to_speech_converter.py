import pyttsx3
import os

def text_to_speech(text, output_path, speed=200):
    try:
        # Инициализация движка
        engine = pyttsx3.init()
        
        # Настройка скорости речи (по умолчанию около 200)
        engine.setProperty('rate', speed)
        
        # Сохранение в файл
        engine.save_to_file(text, output_path)
        engine.runAndWait()  # Ожидаем завершения генерации
        
        print(f"Аудиофайл успешно сохранён: {output_path}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def main():
    print("Программа преобразования текста в речь. Введите текст на русском или /exit для выхода.")
    
    # Путь к рабочему столу
    desktop_path = r"C:\Users\dmitrii.chiniaev\Desktop"
    
    if not os.path.exists(desktop_path):
        print("Ошибка: указанный путь к рабочему столу не существует!")
        return
    
    while True:
        user_input = input("Введите текст: ").strip()
        
        if user_input.lower() == "/exit":
            print("Завершение программы...")
            break
        
        if not user_input:
            print("Вы ввели пустую строку. Попробуйте ещё раз.")
            continue
        
        # Формируем путь к файлу
        output_file = os.path.join(desktop_path, "output.mp3")
        
        # Вызываем функцию с настройками:
        # speed=200 - стандартная скорость (можно увеличить до 300-500 для ускорения)
        text_to_speech(user_input, output_file, speed=210)

if __name__ == "__main__":
    main()