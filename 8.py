#!/usr/bin/python3

class Image(object):
    def __init__(self, raw_image, width, height):
        self.raw_image = list(map(int, str(raw_image))) # parse from int/str to list
        self.width = width
        self.height = height
        self.layers = int(len(self.raw_image) / (self.width * self.height))

    def decode_image(self):
        self.decoded_image = []
        point = 0
        for j in range(self.layers):
            self.decoded_image.append([]) # append layer
            for i in range(self.height):
                self.decoded_image[-1].append([i for i in self.raw_image[point:point + self.width]])
                point += self.width

    def count_pixels(self):
        self.counts_per_layer = []
        for layer in self.decoded_image:
            counts_here = [0 for i in range(10)]
            for row in layer:
                for pixel in row:
                    counts_here[pixel] += 1
            self.counts_per_layer.append(counts_here)

        transpose = lambda x: list(zip(*x))
        self.counts_per_layer_t = transpose(self.counts_per_layer)
        self.min_zeros_layer = self.counts_per_layer_t[0].index(min(self.counts_per_layer_t[0]))
        self.num_1 = self.counts_per_layer[self.min_zeros_layer][1]
        self.num_2 = self.counts_per_layer[self.min_zeros_layer][2]
        self.product_1_2 = self.num_1 * self.num_2

raw_image = '123456789012'
image = Image(raw_image, 3, 2)
image.decode_image()
print(image.decoded_image)

f = open('input8.in', 'r')

raw_image = f.readline().strip('\n')

image = Image(raw_image, 25, 6)
image.decode_image()
print(image.decoded_image)
image.count_pixels()
print(image.product_1_2)


#b


