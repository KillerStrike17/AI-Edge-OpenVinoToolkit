This Folder will consists on how to load pretrained model to your intel edge device and its FAQ section will clear some of your doubts. It will also consists code of how to load some pretrained models which I worked on.

## Why to use Pretrained Models?

* Higher Accuracy 

* Directly integrated to Inference Engine

## Types of Computer Vision Models

* **Classification**: Determines Class. 

* **Detection**: Object and their Location.

* **Segmentation**:  Classifies Each and Every pixel

  * **Semantic Segmentation**: All objects of same class are one

  * **Instance Segmentation**: Each object of a class is separate.
  
**Note**: There are other models as well which include Pose estimation, OCR and GANS, they dont fall under these categories. 

## Different Types of Common Architecture used?

* [**Single SHot Multibox Detector (SSD)**](https://arxiv.org/abs/1512.02325): Obselete Models used to run a classifier over an image multiple times, they would work over some subset of pixels perform classification and repeat until all the subset are covered(Very Slowwwwwww). Idea of SSD was to combine those classifiers and use it over different levels of network, Hence making it Robust to different sizes of object in images.

* [**ResNet**](https://arxiv.org/abs/1512.03385): Very Deep Neural Networks observed that it faces vanishing gradient problems when the network goes deep, hence to avoid it A concept of Skip Connections was introduced. In it the data is passed on to further layers kipping few layers. This reduces the vanishing gradient problem.

* [**MobileNet**](https://arxiv.org/abs/1704.04861): This Model is developed by Google designed to run over devices which have hardware limitations like cellular phone or Tablets. It is very small and accurate model which uses depth wise and 1x1 Convolutions.

* [**You Only Look Once(YOLO)**](https://arxiv.org/abs/1506.02640): It was the network which was a competition for SSD, It calcualted potencial bounding boxes for every pixel and then based on the confidence it decided whihch one should be plotted and which one should not be.

* [**Faster RCNN**](https://arxiv.org/abs/1506.01497): This network was build to perform Image Segmentation. It is a very beautiful network which shows that with just changing the last layer of the network we can perform classification, detection and segmentation.

* [**Inception**](https://arxiv.org/abs/1512.02325): It is a model again developed by Google, This model set a high benchmark for ILSVRC4, This network had three output layers which gave a combined result in providing the output.


[Pretrained Models provided by Intel](https://software.intel.com/en-us/openvino-toolkit/documentation/pretrained-models) having the some backend networks mentioned above.
