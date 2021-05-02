import drawBot as db
import random
import os

output_directory = './training-images/'

illustrations_directory = '../scrape-old-book-illustrations/scraped_images/'
illustrations = os.listdir(illustrations_directory)
wojacks_directory = './wojacks/'
wojacks = os.listdir(wojacks_directory)

db.newDrawing()

for x in range(1,100):
    try:
        illustration = illustrations_directory + random.choice(illustrations)
        print(illustration)
        illustrationW, illustrationH = db.imageSize(illustration)
        db.newPage(illustrationW, illustrationH)
        db.image(illustration, (0,0))

        wojack = wojacks_directory + random.choice(wojacks)
        wojackImgObj = db.ImageObject(wojack)
        wojackImgObj.colorInvert()
        wojackImgObj.maskToAlpha()
        wojackImgObj.colorInvert()

        wojackW, wojackH = db.imageSize(wojack)
        wojackX = int(random.random() * (illustrationW - wojackW))
        wojackY = int(random.random() * (illustrationH - wojackH))
        db.image(wojackImgObj, (wojackX, wojackY))

        # del wojackImgObj
    except AttributeError as e:
        continue

db.saveImage(output_directory + 'img13.png', multipage=True)
db.endDrawing()