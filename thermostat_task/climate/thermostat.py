MIN_TARGET = 5.0
MAX_TARGET = 35.0
MIN_ROOM = -20.0
MAX_ROOM = 50.0
MODES = ("heat", "cool", "off")
STEP_DEGREES = 1.5


class Thermostat:
    def __init__(self, name: str, target_temp: float, current_temp: float, mode: str = "off"):
        self.__name = self.__validate_name(name)
        self.__target_temp = self.__validate_target(target_temp)
        self.__current_temp = self.__validate_room(current_temp)
        self.__mode = self.__validate_mode(mode)

    @staticmethod
    def __validate_name(name: str) -> str:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Назва термостата не може бути порожньою")
        return name.strip()

    @staticmethod
    def __validate_target(value: float) -> float:
        if not MIN_TARGET <= value <= MAX_TARGET:
            raise ValueError(
                f"Цільова температура {value}°C поза діапазоном "
                f"[{MIN_TARGET}; {MAX_TARGET}]"
            )
        return float(value)

    @staticmethod
    def __validate_room(value: float) -> float:
        if not MIN_ROOM <= value <= MAX_ROOM:
            raise ValueError(
                f"Температура в кімнаті {value}°C поза діапазоном "
                f"[{MIN_ROOM}; {MAX_ROOM}]"
            )
        return float(value)

    @staticmethod
    def __validate_mode(mode: str) -> str:
        if mode not in MODES:
            raise ValueError(f"Невідомий режим '{mode}'. Дозволені: {', '.join(MODES)}")
        return mode

    @property
    def name(self) -> str:
        return self.__name

    @property
    def target_temp(self) -> float:
        return self.__target_temp

    @target_temp.setter
    def target_temp(self, value: float) -> None:
        self.__target_temp = self.__validate_target(value)

    @property
    def current_temp(self) -> float:
        return self.__current_temp

    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, value: str) -> None:
        self.__mode = self.__validate_mode(value)

    def is_at_target(self) -> bool:
        return self.__current_temp == self.__target_temp

    def step(self) -> float:
        if self.__mode == "heat" and self.__current_temp < self.__target_temp:
            self.__current_temp = min(self.__target_temp, self.__current_temp + STEP_DEGREES)
        elif self.__mode == "cool" and self.__current_temp > self.__target_temp:
            self.__current_temp = max(self.__target_temp, self.__current_temp - STEP_DEGREES)
        return self.__current_temp

    def run_until_target(self, max_steps: int = 100) -> int:
        if self.__mode == "off":
            raise ValueError("Термостат вимкнений: оберіть режим 'heat' або 'cool'")
        if max_steps <= 0:
            raise ValueError("max_steps має бути додатним")
        if self.__mode == "heat" and self.__current_temp > self.__target_temp:
            raise ValueError("Режим 'heat' не може охолодити кімнату до цілі")
        if self.__mode == "cool" and self.__current_temp < self.__target_temp:
            raise ValueError("Режим 'cool' не може нагріти кімнату до цілі")

        steps = 0
        while not self.is_at_target() and steps < max_steps:
            self.step()
            steps += 1
        return steps

    def apply_ambient_drift(self, delta: float) -> float:
        self.__current_temp = self.__validate_room(self.__current_temp + delta)
        return self.__current_temp

    def describe(self) -> str:
        state = "на цілі" if self.is_at_target() else "не на цілі"
        return (
            f"Термостат '{self.__name}': режим={self.__mode}, "
            f"зараз={self.__current_temp:.1f}°C, ціль={self.__target_temp:.1f}°C ({state})"
        )
