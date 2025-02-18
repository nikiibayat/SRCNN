from __future__ import print_function, division

from keras.utils.vis_utils import plot_model
import models
import img_utils

if __name__ == "__main__":
    path = r"headline_carspeed.jpg"
    val_path = "test_images/"

    scale = 4

    """
    Plot the models
    """

    # model = models.ImageSuperResolutionModel(scale).create_model()
    # plot_model(model, to_file="architectures/SRCNN.png", show_shapes=True, show_layer_names=True)

    # model = models.ExpantionSuperResolution(scale).create_model()
    # plot_model(model, to_file="architectures/ESRCNN.png", show_layer_names=True, show_shapes=True)

    # model = models.DenoisingAutoEncoderSR(scale).create_model()
    # plot_model(model, to_file="architectures/Denoise.png", show_layer_names=True, show_shapes=True)

    # model = models.DeepDenoiseSR(scale).create_model()
    # plot_model(model, to_file="architectures/Deep Denoise.png", show_layer_names=True, show_shapes=True)

    # model = models.ResNetSR(scale).create_model()
    # plot_model(model, to_file="architectures/ResNet.png", show_layer_names=True, show_shapes=True)

    # model = models.GANImageSuperResolutionModel(scale).create_model(mode='train')
    # plot_model(model, to_file='architectures/GAN Image SR.png', show_shapes=True, show_layer_names=True)

    # model = models.DistilledResNetSR(scale).create_model()
    # plot_model(model, to_file='architectures/distilled_resnet_sr.png', show_layer_names=True, show_shapes=True)

    # model = models.NonLocalResNetSR(scale).create_model()
    # plot_model(model, to_file='architectures/non_local_resnet_sr.png', show_layer_names=True, show_shapes=True)

    """
    Train Super Resolution / Evaluate (I added)
    """

    sr = models.ImageSuperResolutionModel(scale)
    sr.weight_path = "./weights/SR Weights 4X.h5"
    # sr.type_true_upscaling = True
    sr.create_model(load_weights=True)
    sr.evaluate(val_path)
    # sr.fit(nb_epochs=250)

    """
    Train ExpantionSuperResolution
    """

    # esr = models.ExpantionSuperResolution(scale)
    # esr.create_model()
    # esr.fit(nb_epochs=250)

    """
    Train DenoisingAutoEncoderSR
    """

    # dsr = models.DenoisingAutoEncoderSR(scale)
    # dsr.create_model()
    # dsr.fit(nb_epochs=250)

    """
    Train Deep Denoise SR
    """

    # ddsr = models.DeepDenoiseSR(scale)
    # ddsr.create_model()
    # ddsr.fit(nb_epochs=180)

    """
    Train Res Net SR
    """

    # rnsr = models.ResNetSR(scale)
    # rnsr.create_model(load_weights=True)
    # rnsr.fit(nb_epochs=50)

    """
    Train ESPCNN SR
    """

    # espcnn = models.EfficientSubPixelConvolutionalSR(scale)
    # espcnn.create_model()
    # espcnn.fit(nb_epochs=50)

    """
    Train GAN Super Resolution
    """

    # gsr = models.GANImageSuperResolutionModel(scale)
    # gsr.create_model(mode='train')
    # gsr.fit(nb_pretrain_samples=10000, nb_epochs=10)

    """
    Train Non Local ResNets
    """

    # non_local_rnsr = models.NonLocalResNetSR(scale)
    # non_local_rnsr.create_model()
    # non_local_rnsr.fit(nb_epochs=50)

    """
    Evaluate Super Resolution on Set5/14
    """

    # sr = models.ImageSuperResolutionModel(scale)
    # sr.evaluate(val_path)

    """
    Evaluate ESRCNN on Set5/14
    """

    #esr = models.ExpantionSuperResolution(scale)
    #esr.evaluate(val_path)

    """
    Evaluate DSRCNN on Set5/14 cannot be performed at the moment.
    This is because this model uses Deconvolution networks, whose output shape must be pre determined.
    This causes the model to fail to predict different images of different image sizes.
    """

    #dsr = models.DenoisingAutoEncoderSR(scale)
    #dsr.evaluate(val_path)

    """
    Evaluate DDSRCNN on Set5/14
    """

    #ddsr = models.DeepDenoiseSR(scale)
    #ddsr.evaluate(val_path)

    """
    Evaluate ResNetSR on Set5/14
    """

    # rnsr = models.ResNetSR(scale)
    # rnsr.create_model(None, None, 3, load_weights=True)
    # rnsr.evaluate(val_path)

    """
    Distilled ResNetSR
    """

    # distilled_rnsr = models.DistilledResNetSR(scale)
    # distilled_rnsr.create_model(None, None, 3, load_weights=True)
    # distilled_rnsr.evaluate(val_path)

    """
    Evaluate ESPCNN SR on Set 5/14
    """

    # espcnn = models.EfficientSubPixelConvolutionalSR(scale)
    # espcnn.evaluate(val_path)

    """
    Evaluate GAN Super Resolution on Set 5/14
    """

    # gsr = models.GANImageSuperResolutionModel(scale)
    # gsr.evaluate(val_path)

    """
    Evaluate Non Local ResNetSR on Set 5/14
    """

    # non_local_rnsr = models.NonLocalResNetSR(scale)
    # non_local_rnsr.evaluate(val_path)

    """
    Compare output images of sr, esr, dsr and ddsr models
    """

    # sr = models.ImageSuperResolutionModel(4)
    # sr.upscale("9809_1.png", save_intermediate=False, suffix="sr")

    #esr = models.ExpantionSuperResolution(scale)
    #esr.upscale(path, save_intermediate=False, suffix="esr")

    #dsr = models.DenoisingAutoEncoderSR(scale)
    #dsr.upscale(path, save_intermediate=False, suffix="dsr")

    # ddsr = models.DeepDenoiseSR(scale)
    # ddsr.upscale(path, save_intermediate=False, suffix="ddsr")

    # rnsr = models.ResNetSR(scale)
    # rnsr.create_model(None, None, 3, load_weights=True)
    # rnsr.upscale(path, save_intermediate=False, suffix="rnsr")

    #gansr = models.GANImageSuperResolutionModel(scale)
    #gansr.upscale(path, save_intermediate=False, suffix='gansr')


