from pathlib import Path
import argparse
import shutil



def parse_args():
    parser = argparse.ArgumentParser(description="Копіювання файлів з сортуванням за розширеннями")
    parser.add_argument("--source", type=Path, required=True, help="Шлях до вихідної дерикторії")
    parser.add_argument("--dest", type=Path, default=Path('dist'), help="Шлях до директорії призначення")
    return parser.parse_args()



def copy_files(src, dst):
    try: 
        for item in src.iterdir():
            print(item)
            if item.is_dir():
                print(f'Піддиректорія {item}')
                copy_files(item, dst / item.name)
                # Рекурсивний виклик  для піддеректорії
            else:
                print(f"Фйл {item}")
                dest_path = dst / item.suffix.strip(".")  # Директорія за розширенням
                dest_path.mkdir(parents=True, exist_ok=True)
                shutil.copy(item, dest_path / item.name)
                # Копіювання файлу
    except Exception as e:
        print(f"Помилка при клпіюванні файлів: {e}")

def main():
    args = parse_args()
    print(args.source, args.dest)
    args.dest.mkdir(parents=True, exist_ok=True) #Створюємо директорію призначення, якщо вона не існує 
    copy_files(args.source, args.dest)


if __name__ == "__main__":
    main()

# python3 copy_files.py --source test --dest test_dest1
