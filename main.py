import os
import shutil
import cv2
import time

first_loc = input('Podaj lokalizację, w której znajdują się zdjęcia: ')
end_loc = input('Podaj lokalizację, do której mają trafić zdjęcia: ')

for file in os.listdir(str(first_loc)):
    if file.endswith('.jpg'):
        cv2.namedWindow('bug', cv2.WINDOW_NORMAL)
        cv2.resizeWindow("bug", 1000, 900)
        cv_photo = cv2.imread('D:/PW/Python/sciezki_folderow/bezmiechowa/'+f'{file}')
        cv2.imshow('bug', cv_photo)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        time.sleep(1)
        shutil.move(first_loc+'/'+f'{file}', end_loc+'/'+f'2021_{file}')