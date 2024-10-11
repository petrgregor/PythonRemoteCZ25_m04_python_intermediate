import asyncio
import time
from multiprocessing import Process, freeze_support, set_start_method


def prepare_appetizer(appetizer):
    print(f"Připravuji předkrm {appetizer}.")
    time.sleep(2)
    print(f"Předkrm {appetizer} hotov.")


def prepare_soup(soup):
    print(f"Připravuji polévku {soup}.")
    time.sleep(5)
    print(f"Polévka {soup} hotova.")


def prepare_main_dish(main_dish):
    print(f"Připravuji hlavní jídlo {main_dish}.")
    time.sleep(3)
    print(f"Hlavní jídlo {main_dish} hotovo.")


def prepare_dessert(dessert):
    print(f"Připravuji dezert {dessert}.")
    time.sleep(5)
    print(f"Hlavní dezert {dessert} hotov.")


def prepare_dinner(appetizer, soup, main_dish, dessert):
    start_time = time.time()
    prepare_appetizer(appetizer)
    prepare_soup(soup)
    prepare_main_dish(main_dish)
    prepare_dessert(dessert)
    print(f"Večeře byla dokončena v čase {time.time() - start_time} s.")


def prepare_dinner_threads(appetizer, soup, main_dish, dessert):
    start_time = time.time()
    import threading
    cooker1 = threading.Thread(target=prepare_appetizer, args=(appetizer,))
    cooker2 = threading.Thread(target=prepare_soup, args=(soup,))
    cooker3 = threading.Thread(target=prepare_main_dish, args=(main_dish,))
    cooker4 = threading.Thread(target=prepare_dessert, args=(dessert,))

    cooker1.start()
    cooker2.start()
    cooker3.start()
    cooker4.start()

    cooker1.join()
    cooker2.join()
    cooker3.join()
    cooker4.join()

    print(f"Večeře byla dokončena v čase {time.time() - start_time} s.")


def prepare_dinner_process(appetizer, soup, main_dish, dessert):
    start_time = time.time()
    cooker1 = Process(target=prepare_appetizer, args=(appetizer,))
    cooker2 = Process(target=prepare_soup, args=(soup,))
    cooker3 = Process(target=prepare_main_dish, args=(main_dish,))
    cooker4 = Process(target=prepare_dessert, args=(dessert,))

    cooker1.start()
    cooker2.start()
    cooker3.start()
    cooker4.start()

    cooker1.join()
    cooker2.join()
    cooker3.join()
    cooker4.join()

    print(f"Večeře byla dokončena v čase {time.time() - start_time} s.")


async def prepare_appetizer_async(appetizer):
    print(f"Připravuji předkrm {appetizer}.")
    await asyncio.sleep(2)
    print(f"Předkrm {appetizer} hotov.")


async def prepare_soup_async(soup):
    print(f"Připravuji polévku {soup}.")
    await asyncio.sleep(5)
    print(f"Polévka {soup} hotova.")


async def prepare_main_dish_async(main_dish):
    print(f"Připravuji hlavní jídlo {main_dish}.")
    await asyncio.sleep(3)
    print(f"Hlavní jídlo {main_dish} hotovo.")


async def prepare_dessert_async(dessert):
    print(f"Připravuji dezert {dessert}.")
    await asyncio.sleep(5)
    print(f"Hlavní dezert {dessert} hotov.")


async def prepare_dinner_async(appetizer, soup, main_dish, dessert):
    start_time = time.time()
    tasks = [
        asyncio.create_task(prepare_appetizer_async(appetizer)),
        asyncio.create_task(prepare_soup_async(soup)),
        asyncio.create_task(prepare_main_dish_async(main_dish)),
        asyncio.create_task(prepare_dessert_async(dessert))
    ]
    await asyncio.gather(*tasks)
    print(f"Večeře byla dokončena v čase {time.time() - start_time} s.")


if __name__ == "__main__":
    print("Single-threaded synchronous")
    print("Jeden kuchař v jedné kuchyni připravuje jídlo.")
    prepare_dinner("šunková roláda", "rajská", "guláš", "koláč")

    print()
    print("=" * 80)
    print("Multi-thread synchronous")
    print("Více kuchařů v jedné kuchyni připravují jídlo.")
    prepare_dinner_threads("sýrový talíř", "kuřecí vývar", "řízek", "dort")

    print()
    print("=" * 80)
    print("Multi-process synchronous")
    print("Více kuchařů ve více kuchyních.")
    freeze_support()
    set_start_method("spawn")
    prepare_dinner_process("arašídy", "nudlová", "svíčková", "pudink")

    print()
    print("=" * 80)
    print("Single-threaded asynchronous")
    print("Jeden kuchař - v prodlevě začíná pracovat na dalším úkolu")
    asyncio.run(prepare_dinner_async("topinka", "písmenková", "koprovka", "palačinka"))
