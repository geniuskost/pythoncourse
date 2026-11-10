import json
import random
import urllib.error
import urllib.request
from typing import Protocol, runtime_checkable

OPEN_METEO_URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=46.48&longitude=30.73&current=temperature_2m"
)


@runtime_checkable
class TemperatureSensor(Protocol):
    def read_temperature(self) -> float: ...

    def get_sensor_id(self) -> str: ...


class WeatherAPISensor:
    def __init__(self, timeout: float = 10.0) -> None:
        self._timeout = timeout

    def read_temperature(self) -> float:
        try:
            with urllib.request.urlopen(OPEN_METEO_URL, timeout=self._timeout) as response:
                data = json.load(response)
            return float(data["current"]["temperature_2m"])
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, KeyError, ValueError) as error:
            raise RuntimeError(f"Не вдалося отримати погоду: {error}") from error

    def get_sensor_id(self) -> str:
        return "WAS26-Odesa"


class SimulatedSensor:
    def __init__(self, base: float, deviation: float) -> None:
        self._base = base
        self._deviation = deviation

    def read_temperature(self) -> float:
        return self._base + random.uniform(-self._deviation, self._deviation)

    def get_sensor_id(self) -> str:
        return f"SIM-{self._base}"


class FakeAlways25:
    def read_temperature(self) -> float:
        return 25.0

    def get_sensor_id(self) -> str:
        return "Fake-25"


class BrokenSensor:
    def read_temperature(self) -> float:
        raise RuntimeError("Датчик зламаний!")

    def get_sensor_id(self) -> str:
        return "BROKEN-999"


class RealDHT22:
    def read_temperature(self) -> float:
        return 22.5

    def get_sensor_id(self) -> str:
        return "DHT22-001"


def monitor_room(sensors: list[TemperatureSensor]) -> None:
    for sensor in sensors:
        sensor_id = sensor.get_sensor_id()
        try:
            temperature = sensor.read_temperature()
        except Exception as error:
            print(f"[{sensor_id}] ПОМИЛКА: {error}")
        else:
            print(f"[{sensor_id}] Температура: {temperature:.1f} °C")


def main() -> None:
    sensors = [
        WeatherAPISensor(),
        SimulatedSensor(base=21.5, deviation=3.0),
        FakeAlways25(),
        BrokenSensor(),
    ]
    monitor_room(sensors)

    print()
    print(isinstance(RealDHT22(), TemperatureSensor))
    print(isinstance({"temp": 22}, TemperatureSensor))


if __name__ == "__main__":
    main()
