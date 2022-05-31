from stegano import lsbset
import datetime
from stegano.lsbset import generators
import glob, os
from statistics import mean, stdev

def time_counter(func):
    def timed(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        return result, (end-start).total_seconds()
    return timed

@time_counter
def hide(imgPath, msg, gen):
    return lsbset.hide(imgPath, msg, gen)

@time_counter
def reveal(imgPath, gen):
    return lsbset.reveal(imgPath, gen)

def encode():
    print('Podaj wiadomość do zaszyfrowania:')
    msg = input()
    print('Podaj ścieżkę do pliku:')
    imgPath = input()
    secret_image, timeDiff = hide(imgPath, msg, generators.eratosthenes())
    print(f'Czas szyfrowania wyniósł {timeDiff} sekund')
    print('Podaj nazwę nowego pliku:')
    newImg = input()
    secret_image.save(newImg)

def decode():
    print('Podaj ścieżkę do pliku:')
    imgPath = input()
    msg, timeDiff = reveal(imgPath, generators.eratosthenes())
    print(f'Czas deszyfrowania wyniósł {timeDiff} sekund')
    print(f'Wiadomość to: {msg}')

def speedTest(iterations, *sizes):
    for file in glob.glob("./*.png"):
        print(f'Testy dla pliku {file}')
        for size in sizes:
            print(f'Testy dla wiadomości o rozmiarze {size}')
            msg = 'z'*size
            results = []
            for i in range(iterations):
                _, timeDiff = hide(file, msg, generators.eratosthenes())
                results.append(timeDiff)
            print(f'Średni czas szyfrowania wynosi {mean(results):.4f} sekund, standardowe odchylenie wynosi {stdev(results):.4f}')
            results = []
            secret_image, _ = hide(file, msg, generators.eratosthenes())
            secret_image.save('temp.png')
            for i in range(iterations):
                _, timeDiff = reveal('temp.png', generators.eratosthenes())
                results.append(timeDiff)
            if os.path.exists('temp.png'):
                os.remove('temp.png')
            print(f'Średni czas deszyfrowania wynosi {mean(results):.4f} sekund, standardowe odchylenie wynosi {stdev(results):.4f}')

def sizeTest(*sizes):
    for file in list(glob.glob('./*.png')):
        origin = os.path.getsize(file)
        print(f'obrazek: {file}')
        for size in sizes:
            message = 'z'*size
            secret_image, timeDiff = hide(file, message, generators.eratosthenes())
            newFile = file.replace('.png', '_test.png')
            secret_image.save(newFile)
            new = os.path.getsize(newFile)
            print(f'rozmiar wiadomości: {size}')
            print(f'stosunek rozmiaru nowego obrazka do starego: {new/origin}')
            if os.path.exists(newFile):
                os.remove(newFile)


if __name__ == '__main__':
    print('Co chcesz zrobić?')
    print('1) Zaszyfruj wiadomość')
    print('2) Odszyfruj wiadomość')
    print('3) Przeprowadź test na szybkość')
    print('4) Przeprowadź test na rozmiar')
    opt = int(input())
    if opt == 1:
        encode()
    elif opt == 2:
        decode()
    elif opt == 3:
        speedTest(30, 10, 100, 1000)
    elif opt == 4:
        sizeTest(10, 100, 1000)