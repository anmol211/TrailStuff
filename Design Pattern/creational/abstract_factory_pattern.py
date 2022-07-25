from abc import ABC, abstractmethod


class IButton(ABC):
    @abstractmethod
    def press(self):
        pass


class MacButton(IButton):
    def press(self):
        print("Mac button pressed")


class WinButton(IButton):
    def press(self):
        print("Win button pressed")


class ITextBox(ABC):
    @abstractmethod
    def show_text(self):
        pass


class MacTextBox(ITextBox):
    def show_text(self):
        print("Showing mac text box")


class WinTextBox(ITextBox):
    def show_text(self):
        print("Showing win text box")


class IFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_text_box(self):
        pass


class MacFactory(IFactory):

    def create_button(self):
        return MacButton()

    def create_text_box(self):
        return MacTextBox()


class WinFactory(IFactory):

    def create_button(self):
        return WinButton()

    def create_text_box(self):
        return WinTextBox()


class GUIAbstractFactory:
    @staticmethod
    def create_factory(os_type):
        if os_type == "windows":
            return WinFactory()
        elif os_type == "mac":
            return MacFactory()
        return MacFactory()


if __name__ == '__main__':
    os_type = "mac"
    os_factory = GUIAbstractFactory.create_factory(os_type)
    button = os_factory.create_button()
    button.press()

    text_box = os_factory.create_text_box()
    text_box.show_text()
