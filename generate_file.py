# generate_file.py
import time
import random

while True:
    filename = f'{random.randint(1, 1000000000)}.txt'
    with open(f'/usr/src/app/sync_files/public/{filename}', 'w') as f:
        f.write(str(random.randint(1, 100)))
    time.sleep(1800)  # Esperar 30 minutos