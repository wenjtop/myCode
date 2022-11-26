import cv2
import numpy as np

img = cv2.imread(img_filenames[index])
label = cv2.imread(label_filenames[index])

img = randomBlur(img)                # 图像滤波
img = RandomBrightness(img)          # 调整明度(Value)
img = RandomHue(img)                 # 调整色相(Hue)
img = RandomSaturation(img)          # 调整饱和度(Saturation)
img, label = random_fliplr(img, label)    # 左右反转
img, label = random_flipud(img, label)    # 上下反转
img, label = randomCrop(img, label)       # 在图片中心选取一个区域剪切

def BGR2RGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def BGR2HSV(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def HSV2BGR(img):
    return cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

def random_fliplr(img, label):
    if random.random() < 0.5:
        img = np.fliplr(img)
        label = np.fliplr(label)
        return img, label
    return img, label

def random_flipud(img, label):
    if random.random() < 0.5:
        img = np.flipud(img)
        label = np.flipud(label)
        return img, label
    return img, label

def randomBlur(img):
    if random.random() < 0.5:
        img = cv2.blur(img, (5, 5))
    return img

def RandomBrightness(img):
    if random.random() < 0.5:
        hsv = self.BGR2HSV(img)          # HSV即色相(Hue)、饱和度(Saturation)、明度(Value)，又称HSB(B即Brightness)
        h, s, v = cv2.split(hsv)
        adjust = random.choice([0.5, 1.5])
        v = v * adjust
        v = np.clip(v, 0, 255).astype(hsv.dtype)
        hsv = cv2.merge((h, s, v))
        img = self.HSV2BGR(hsv)
    return img

def RandomHue(img):
    if random.random() < 0.5:
        hsv = self.BGR2HSV(img)
        h, s, v = cv2.split(hsv)
        adjust = random.choice([0.5, 1.5])
        h = h * adjust
        h = np.clip(h, 0, 255).astype(hsv.dtype)
        hsv = cv2.merge((h, s, v))
        img = self.HSV2BGR(hsv)
    return img

def RandomSaturation(img):
    if random.random() < 0.5:
        hsv = self.BGR2HSV(img)
        h, s, v = cv2.split(hsv)
        adjust = random.choice([0.5, 1.5])
        s = s * adjust
        s = np.clip(s, 0, 255).astype(hsv.dtype)
        hsv = cv2.merge((h, s, v))
        img = self.HSV2BGR(hsv)
    return img

def randomCrop(img, label):
    if random.random() < 0.5:
        height, width, c = img.shape
        h = random.uniform(0.8 * height, height)
        w = random.uniform(0.8 * width, width)
        x = random.uniform(0, width - w)
        y = random.uniform(0, height - h)
        x, y, h, w = int(x), int(y), int(h), int(w)
        img = img[y:y + h, x:x + w, :]
        label = label[y:y + h, x:x + w, :]
        img = cv2.resize(img, (height, width))
        label = cv2.resize(label, (height, width))[:, :, None]
        return img, label
    return img, label