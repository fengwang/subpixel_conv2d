# SubpixelConv2D

Subpixel convolution with keras and tensorflow.

----

### Example usage

A simple model upsampling a layer of dimension ( 32, 32, 16 ) to ( 128, 128, 1 ), with save/load functionality enabled..

```python
from subpixel_conv2d import SubpixelConv2D
from keras.layers import Input
from keras.models import Model, load_model
ip = Input(shape=(32, 32, 16))
x = SubpixelConv2D(upsampling_factor=4)(ip)
model = Model(ip, x)
model.summary()
model.save( 'model.h5' )

print( '*'*80 )
nm = load_model( 'model.h5' )
print( 'new model loaded successfully' )
```

produces output of

```
Using TensorFlow backend.
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
input_1 (InputLayer)         (None, 32, 32, 16)        0
_________________________________________________________________
subpixel_conv2d_1 (SubpixelC (None, 128, 128, 1)       0
=================================================================
Total params: 0
Trainable params: 0
Non-trainable params: 0
_________________________________________________________________
********************************************************************************
/usr/lib/python3.7/site-packages/keras/engine/saving.py:269: UserWarning: No training configuration found in save file: the model was *not* compiled. Compile it manually.
  warnings.warn('No training configuration found in save file: '
new model loaded successfully
```

### Note

Before loading a model designed with `SubpixelConv2D`, do load `from subpixel_conv2d import SubpixelConv2D`.

### Reference

Shi, Wenzhe, Jose Caballero, Ferenc Huszár, Johannes Totz, Andrew P. Aitken, Rob Bishop, Daniel Rueckert, and Zehan Wang. “Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network.” ArXiv:1609.05158 [Cs, Stat], September 16, 2016. http://arxiv.org/abs/1609.05158.

### License

AGPL-3

