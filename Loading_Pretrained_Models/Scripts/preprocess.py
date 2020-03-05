import cv2
import numpy as np
from inference import Network
import argparse

def get_args():
    '''
    Gets the arguments from the command line.
    '''

    parser = argparse.ArgumentParser("Basic Edge App with Inference Engine")
    # -- Create the descriptions for the commands

    c_desc = "CPU extension file location, if applicable"
    d_desc = "Device, if not CPU (GPU, FPGA, MYRIAD)"
    i_desc = "The location of the input image"
    m_desc = "The location of the model XML file"

    # -- Add required and optional groups
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    # -- Create the arguments
    required.add_argument("-i", help=i_desc, required=True)
    required.add_argument("-m", help=m_desc, required=True)
    optional.add_argument("-c", help=c_desc, default=None)
    optional.add_argument("-d", help=d_desc, default="CPU")
    args = parser.parse_args()

    return args

def age_gender_estimation(input_image,height, width):
	#The Desired Format is 1X3X62X62
	
	image = np.copy(input_image)
	# image = cv2.resize(image, (width, height))
	image = image.transpose((2,0,1))
	image = image.reshape(1, 3, height, width)

	return image

# def handle_face(output, input_shape):


def perform_inference(args):

	inference_network = Network()
	n,c,h,w = inference_network.load_model(args.m,args.d, args.c)
	image = cv2.imread(args.i)
	processed_image = age_gender_estimation(image, h,w)
	output = inference_network.extract_output()
	# print(output)
	age = output['age_conv3']
	print(age[0][0][0][0]*100)
	gender = output['prob'].flatten()
	if gender[0]>gender[1]:
		print("Female")
	else:
		print("Male")
	
	

def main():
	args = get_args()
	perform_inference(args)

if __name__=="__main__":
	main()