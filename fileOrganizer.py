import os
import shutil

files = os.listdir(f'./files')

for file in files:
    fileName, fileExtencion= os.path.splitext(file)

    if not os.path.isdir(f'./files/{fileExtencion}'):
        os.makedirs(f'./files/{fileExtencion}')
    
    shutil.move(f'./files/{file}',f'./files/{fileExtencion}/{file}')
