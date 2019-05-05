if __name__ == '__main__':
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

