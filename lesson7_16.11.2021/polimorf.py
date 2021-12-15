from abc import ABC, abstractmethod


class Camera(ABC):
    code = "001"

    def shot(self):
        return f"Сфотографировать {self.code}"

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass


class PhoneCamera(Camera):
    def shot(self):
        return "Сфотографировать с помощью телефона"

    def on(self):
        return "Открыть камеру"

    def off(self):
        return "Закрыть камеру"


class ProCamera(Camera):

    def on(self):
        return "Выключить камеру"

    def off(self):
        return "Включить камеру"


def shot_and_off_camera(camera: Camera):
    print(camera.shot())
    print(camera.off())


phone_camera = PhoneCamera()
pro_camera = ProCamera()

shot_and_off_camera(phone_camera)
print("*" * 30)
shot_and_off_camera(pro_camera)
