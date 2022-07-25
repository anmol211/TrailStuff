from abc import ABC, abstractmethod


# Product
class Desktop:
    def __init__(self):
        self.keyboard = None
        self.monitor = None

    def show_specs(self):
        print(f"{self.keyboard} and {self.monitor}")


# Builder
class DesktopBuilder(ABC):
    def __init__(self):
        self.desktop = Desktop()

    @abstractmethod
    def build_keyboard(self):
        pass

    @abstractmethod
    def build_monitor(self):
        pass

    @abstractmethod
    def get_desktop(self):
        pass


# Concrete Builder 1
class DellDesktopBuilder(DesktopBuilder):

    def build_monitor(self):
        self.desktop.monitor = "DELL Monitor"

    def build_keyboard(self):
        self.desktop.keyboard = "DELL keyboard"

    def get_desktop(self):
        return self.desktop


# Concrete Builder 2
class HPDesktopBuilder(DesktopBuilder):

    def build_monitor(self):
        self.desktop.monitor = "HP Monitor"

    def build_keyboard(self):
        self.desktop.keyboard = "HP keyboard"

    def get_desktop(self):
        return self.desktop


# Director
class DesktopDirector:
    def __init__(self, desktop_builder: DesktopBuilder):
        self.desktop_builder = desktop_builder

    def build_desktop(self) -> Desktop:
        self.desktop_builder.build_keyboard()
        self.desktop_builder.build_monitor()
        return self.desktop_builder.get_desktop()


if __name__ == '__main__':
    hp_desktop_builder = HPDesktopBuilder()
    dell_desktop_builder = DellDesktopBuilder()

    director1 = DesktopDirector(hp_desktop_builder)
    director2 = DesktopDirector(dell_desktop_builder)

    desktop1 = director1.build_desktop()
    desktop2 = director2.build_desktop()

    desktop1.show_specs()
    desktop2.show_specs()


