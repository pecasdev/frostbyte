from src.monad import create_person


def main():
    result = create_person()
    value = result.unwrap()
    print(f"A person was created: {value}")


if __name__ == "__main__":
    main()
    print("hello!")
