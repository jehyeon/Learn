import cv2
import json

# FILENAME = 'googlelogo_color_272x92dp.png'
FILENAME = 'seoul.jpg'

image = cv2.imread('./' + FILENAME)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

divide = 10
standard = 210

# print(image.shape)          # 270, 365
array = [[0] * 37 for x in range(27)]
backup_color = []

for y in range(0, image.shape[0], divide):
    for x in range(0, image.shape[1], divide):

        sum_r, sum_g, sum_b = 0, 0, 0
        for i in range(divide):
            for j in range(divide):
                try:
                    sum_b += image[y+j][x+j][0]
                    sum_g += image[y+i][x+j][1]
                    sum_r += image[y+i][x+j][2]
                except:
                    pass
        
        if not (int(sum_r/divide**2) > standard and int(sum_g/divide**2) > standard and int(sum_b/divide**2) > standard):
            # print((int(sum_r/divide**2), int(sum_g/divide**2), int(sum_b/divide**2)))
            pos_x, pos_y = int(x/10), int(y/10)
            array[pos_y][pos_x] = 1

            for i in range(divide):
                for j in range(divide):
                    try:
                        image[y+i][x+j] = (sum_r/divide**2, sum_g/divide**2, sum_b/divide**2)
                        # backup_color.append((int(sum_r/divide**2), int(sum_g/divide**2), int(sum_b/divide**2)))
                    except:
                        pass


# image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# for arr in array:
#     for val in arr[:-1]:
#         if (val == 1): print('.',end='')
#         else: print(' ', end='')
#     print()

data = []
for arr in array:
    data.append(arr[:-1])

print(data)

# with open('seoul_grid.json','w',encoding='utf8') as f:
#     # f.write(save)
#     json.dump(data, f, ensure_ascii=False)

# with open('check.txt','w',encoding='utf8') as f:
#     for color in backup_color:
#         f.write(str(color) + '\n')

# cv2.imshow('win', image)
# cv2.waitKey(0)

# print(backup_color)