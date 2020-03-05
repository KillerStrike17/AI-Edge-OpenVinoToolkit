import os
from openvino.inference_engine import IENetwork,IECore

class Network:

	def __init__(self):
		self.plugin = None
		self.input_blob = None
		self.exec_network = None

	def load_model(self, model, device = "CPU", cpu_extenston = None):
		mdoel_xml = model
		model_bin = os.path.splitext(mdoel_xml)[0] + ".bin"
		self.plugin = IECore()
		# if cpu_extenstion and "CPU" in device:
		# 	self.plugin.add_extension(cpu_extension,device)

		network = IENetwork(model = mdoel_xml, weights = model_bin)
		self.exec_network = self.plugin.load_network(network, device)
		self.input_blob = next(iter(network.inputs))
		return network.inputs[self.input_blob].shape

	def sync_inference(self, image):
		self.exec_network.infer({self.input_blob:image})
		return 

	def extract_output(self):
		return self.exec_network.requests[0].outputs
