
from __future__ import annotations
from loadingBar import LoadingBar
from observer import Observer, FirstObserver

def main():



    loading = LoadingBar()
    loading.add_observer(FirstObserver())
    # loading.notify(5, 6)
    loading.loopForObserver(60)



if __name__ == "__main__":
    main()