from dataclasses import dataclass


@dataclass
class BudylnykSadyst:
    brand: str
    alarm_time: str
    snooze_count: int
    patience: int

    def ring(self) -> None:
        print(f"[{self.brand}] Дзинь-дзинь! {self.alarm_time}! "
              f"Ви ж просили розбудити. Ось я і радий стараюся.")

    def snooze(self) -> None:
        self.snooze_count += 1
        self.patience = max(0, self.patience - 20)
        print(f"[{self.brand}] Відкладено вже {self.snooze_count} раз(и). "
              f"Терпіння: {self.patience}%. Я все пам'ятаю.")

    def complain(self) -> None:
        if self.patience > 60:
            mood = "Та я нічого, спіть собі... (насправді ні)."
        elif self.patience > 20:
            mood = "Знаєте, мені теж хочеться поспати. Але ж ні."
        else:
            mood = "ВСТАВАЙ! Я більше не ввічливий будильник!"
        print(f"[{self.brand}] {mood}")

    def threaten(self) -> None:
        if self.snooze_count == 0:
            print(f"[{self.brand}] Поки що ви молодець. Але я стежу.")
        else:
            print(f"[{self.brand}] Наступного разу дзвенітиму на "
                  f"{self.snooze_count + 1} децибел голосніше і з сусідом за стіною.")


def main() -> None:
    clocks = [
        BudylnykSadyst("Poljot", "06:30", 0, 100),
        BudylnykSadyst("Casio", "05:45", 2, 50),
        BudylnykSadyst("Mriya-3000", "04:00", 5, 10),
    ]

    for clock in clocks:
        print("=" * 60)
        print(clock)
        clock.ring()
        clock.snooze()
        clock.complain()
        clock.threaten()


if __name__ == "__main__":
    main()
