import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import random
from PIL import Image

def plot_labels(dir, labels_dir):
    df = pd.read_csv(dir, delimiter=' ', names=['Img_paths', 'Labels'])
    labels_df = pd.read_csv(labels_dir, delimiter='      ', names=['Num', 'Lab'], engine='python')
    lab_num = Counter(df['Labels'])
    colors = ['#6DBFD1', '#FF7D63']

    x = [i for i in (labels_df['Lab'].tolist())]
    y =[lab_num[i] for i in range(25)]

    plt.barh(x, y, color=colors)
    for i, v in enumerate(y):
        plt.text(v+max(y)*0.02, i-0.3, f'{v}', ha='center')
    plt.xlabel('NUMBER OF IMAGES')
    plt.ylabel('CATEGORIES')
    title = dir.split('/')[1].split('-')[0].upper()
    plt.title(f'{title} DATASET')
    plt.show()

def plot_transforms(directory, transform, imgs_num):

    df = pd.read_csv(directory, delimiter=' ', names=['Img_paths', 'Labels'])
    paths = df['Img_paths'].tolist()
    random_image_paths = random.sample(paths, k=imgs_num)
    for image_path in random_image_paths:
        with Image.open('data/' + image_path) as f:
            fig, ax = plt.subplots(1, 2)
            ax[0].imshow(f)
            ax[0].set_title("Original")
            ax[0].axis("off")

            transformed = transform(f).permute(1, 2, 0) 
            ax[1].imshow(transformed) 
            ax[1].set_title("Transformed")
            ax[1].axis("off")

def plot_imgs(dataset, imgs_num, labels_dir):

    random_image_paths = random.sample(range(len(dataset)), k=imgs_num)

    fig, ax = plt.subplots(1, imgs_num, figsize=(12,8))
    for i,img_idx in enumerate(random_image_paths):

        f = dataset[img_idx][0].permute(1, 2, 0)
        name = ''
        
        df = pd.read_csv(labels_dir, delimiter='      ', names=['Num', 'Lab'],  engine='python')
        df.loc[(df.Num == (dataset[img_idx][1])), name] = 'x' 

        print(name)
        
        ax[i-1].imshow(f)
        ax[i-1].set_title(f"{name}")
        ax[i-1].axis("off")