import os
import argparse
import zipfile

def prepare_txt_file_content(files):
    content = []
    for name in files:
        _, alphabet, character, _ = name.split('/')
        line = os.path.join(alphabet, character, 'rot000') + '\n'
        if line not in content:
            content.append(line)
    return content

parser = argparse.ArgumentParser(description='Create original split')
default_images_base_dir = '.'
parser.add_argument('--images_base_dir', type=str, default=default_images_base_dir,
                    help="location of images zip files (default: {:s})".format(default_images_base_dir))

default_split_txt_dir = 'data/omniglot/splits/original'
parser.add_argument('--split_txt_dir', type=str, default=default_split_txt_dir,
                    help="location of directory to place split txt files (default: {:s})".format(default_split_txt_dir))

parser.add_argument('--validation_size', type=float, default=0.20,help="fraction of images to put in val")

args = vars(parser.parse_args())

validation_size = args['validation_size']

images_background_path = os.path.join(args['images_base_dir'], 'images_background.zip')
images_evaluation_path = os.path.join(args['images_base_dir'], 'images_evaluation.zip')
trainval_path = os.path.join(args['split_txt_dir'], 'trainval.txt')
test_path = os.path.join(args['split_txt_dir'], 'test.txt')
train_path = os.path.join(args['split_txt_dir'], 'train.txt')
val_path = os.path.join(args['split_txt_dir'], 'val.txt')

if not os.path.isdir(args['split_txt_dir']):
    os.mkdir(args['split_txt_dir'])

zip = zipfile.ZipFile(images_background_path)
background_files = list(filter(lambda x: True if '.png' in x else False, list(zip.namelist())))

zip = zipfile.ZipFile(images_evaluation_path)
evaluation_files = list(filter(lambda x: True if '.png' in x else False, list(zip.namelist())))

print("total images number {n}".format(n=len(evaluation_files)+len(background_files)))

############# Trainval ##########################################################

trainval = prepare_txt_file_content(background_files)

print('writing trainval txt, number of trainval images={n}'.format(n=len(trainval)))
with open(trainval_path, 'w') as trainval_file:
    trainval_file.writelines(trainval)


############# Train/Val ##########################################################

split_index = int(validation_size * len(background_files))
train_files = background_files[:-split_index]
val_files = background_files[-split_index:]

train = prepare_txt_file_content(train_files)

print('writing train txt, number of train images={n}'.format(n=len(train)))
with open(train_path, 'w') as train_file:
    train_file.writelines(train)

val = prepare_txt_file_content(val_files)

print('writing val txt, number of val images={n}'.format(n=len(val)))
with open(val_path, 'w') as val_file:
    val_file.writelines(val)


############# Test ##########################################################


test = prepare_txt_file_content(evaluation_files)

print('writing test txt, number of test images={n}'.format(n=len(test)))
with open(test_path, 'w') as test_file:
    test_file.writelines(test)

