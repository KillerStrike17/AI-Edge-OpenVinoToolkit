# AI@Edge-Notes

## Introduction to AI@Edge and Basic FAQs

### What is AI at Edge?

* Edge means local Processing.

* Need things to be done in real time. 

* Work at Low latency or at places where network is not available.

* Edge Doesnot mean there is no involvement of cloud.

* Cloud can still be used to train AI Models and inference can be at Edge.

* **Example:** Application like Self Driving cars or Home Security Applications(and many more) fall under Edge Devices where as applications like Voice Assistants or getting some useful information from some tons of data require cloud supports

### Why AI at Edge?

* **Network Impacts** - Expensive in terms of bandwidth, power consumption, and sometimes not possible.

* **latency Considerations** - real time processing cannot afford latency

* **Security Concerns** - application could be using sensitive data.

* **Optimization for local Inference** - made for specific hardware have lead to great efficiency.

### Applications for Edge

* Self Driving Cars

* Heart beat Monitoring

* Autonomous Robot

* Sensors for detecting and tracking Endangered Animals

* Autonomous UAVs to deliver items in Remote Places

* Smart Home Security Alert.

### Do we need Edge everywhere?

No, it depends on the problem, Sometimes we dont need results in real time. For example, While getting insights from millions of records, we are okay with some delays. 

### History of Edge Computing

* 1970s - ATM

* 1990 - wwww

* 2000s - Smart Meter

* Latest tech- Smartwatches, Self Driving cars

### What is OpenVINO Toolkit

* Gives Flexibity to the developer to focus on edge application development rather than spending time to fine tune the model over to its speed

* Model Optimizer - Convert a model to Intermediate Representation for further use with the toolkit.

* Open Model Zoo - Obtain a pre-trained Model.

* Inference Engine - Perform inference on an Intermediate Representation.

