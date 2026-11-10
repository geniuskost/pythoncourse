from climate import Thermostat


def main() -> None:
    living_room = Thermostat("Вітальня", target_temp=22, current_temp=16, mode="heat")
    print(living_room.describe())
    steps = living_room.run_until_target()
    print(f"Нагрів за {steps} кроків")
    print(living_room.describe())

    print()
    bedroom = Thermostat("Спальня", target_temp=18, current_temp=27, mode="cool")
    print(bedroom.describe())
    bedroom.step()
    print(bedroom.describe())
    bedroom.target_temp = 20
    print(f"Нова ціль: {bedroom.target_temp}°C")
    bedroom.apply_ambient_drift(-3)
    print(bedroom.describe())

    print()
    print("Перевірка захисту:")
    attempts = [
        ("ціль 100°C", lambda: setattr(living_room, "target_temp", 100)),
        ("режим 'turbo'", lambda: setattr(living_room, "mode", "turbo")),
        ("пряма зміна current_temp", lambda: setattr(living_room, "current_temp", 99)),
        ("дрейф +100°C", lambda: living_room.apply_ambient_drift(100)),
        ("порожня назва", lambda: Thermostat("  ", 20, 20)),
        ("запуск у режимі off", lambda: Thermostat("Гараж", 15, 10).run_until_target()),
        ("heat для гарячої кімнати", lambda: Thermostat("Кухня", 20, 30, "heat").run_until_target()),
    ]
    for label, action in attempts:
        try:
            action()
        except (ValueError, AttributeError) as error:
            print(f"  {label}: {type(error).__name__}: {error}")
        else:
            print(f"  {label}: НЕ відхилено (помилка в коді!)")

    print()
    print("Прямий доступ до приватного атрибута:")
    try:
        print(living_room.__current_temp)
    except AttributeError as error:
        print(f"  AttributeError: {error}")


if __name__ == "__main__":
    main()
