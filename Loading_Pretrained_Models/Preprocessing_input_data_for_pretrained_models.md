## Preprocessing Inputs

**Points to Remember**

* As every model is different, so is the input it receives is. Hence, different models my require different types of inputs. The input format for every model can be looked up to the documentation page of that model.

* Check for channel order i.e. whether it is in BGR format or RGB format. When images are loaded with differnt libraries, they load in different channel order.  The input should match the order accepted by the model. 

* The input image can be of various sizes, but the model doesnot accept all of those, it only accepts in one format and in one order, hence the data has to be transformed to that.

* Sometimes, some model may require some normalization, hence the documentation will convey that.

### How to read the Documentation

lets take an example:

[Age and Gender Recognition Model](http://docs.openvinotoolkit.org/latest/_models_intel_age_gender_recognition_retail_0013_description_age_gender_recognition_retail_0013.html)

To view the input data dimension, check the inputs heading, It will show the shape of the input image i.e. batchsize, number of channels, height and width of image and the channel order. 

Here, this model requires input to be in `shape: [1x3x62x62]` and color order: BGR.

The output format can be checked under the output heading. For this model there are two outputs i.e. age and gender. Thus the output can be stored and viewed.

## Important functions to load and transform image inputs

* **cv2.imread()** - Loads the image in BGR format.

* **cv2.resize()** - to resize the images, It takes input in order width followed by height.

* **{imageframe}.transpose()** -  to transpose the data.

* **{imageframe}.reshape()** - to reshape the array in the desired format.
