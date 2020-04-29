import time
from abc import ABC, abstractmethod
import progressbar
from tqdm import tqdm


class Observer(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def update(selfseld, *args, **kwargs):
        pass


class FirstObserver(Observer):
    def __init__(self):
        super().__init__()

    def update(self, number, maXValue):
            progressbar.sys.stdout.write('\r')
            # the exact output you're looking for:
            progressbar.sys.stdout.write("[%-20s] %d%%" % ('=' * round(number/maXValue*20), number/maXValue*100))
            progressbar.sys.stdout.flush()
            time.sleep(0.1)




#
# class ConcreteObserverA(Observer):
#     def update(self, loadingBar: LoadingBar) -> None:
#         print('to sie wykonuje 1 ')
#         print(loadingBar.state)
#         # if loadingBar._state < 3:
#         #     print("ConcreteObserverA: Reacted to the event")
