from abc import abstractmethod, ABC
from time import sleep

from observer import Observer

from abc import ABC, abstractmethod
from typing import List


class LoadingBar(ABC):

    def __init__(self):
        self.__obs_list= []
        self.__state= None

    def loopForObserver(self, maxValue):
        print("nastepuje enumeracja...")

        for i in range(0, maxValue+1):
            _state = i
            # print(i, end=' \n')
            self.notify(i, maxValue)

    def add_observer(self, obs):
        """
        Attach an observer to the subject.
        """
        self.__obs_list.append(obs)

    def notify(self, *args, **kwargs):
        """
        Notify all observers about an event.
        """
        for obs in self.__obs_list:
            obs.update(*args, **kwargs)

    # @property
    # def state(self):
    #     return self._state
