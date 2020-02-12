# Steps_to_download_a_pretrained_model:

One the Environment is setup, you can download the pretrained model by running the download.py script which can be found at the location : **{Install Directory}\openvino_2020.1.033\deployment_tools\open_model_zoo\tools\downloader**

The Script takes in multiple arguments which can viewed by running the script via -h or --help argument.

The Optional Argument are:

* -h, --help: Show help message containing all the argument details and exits the program

* -- name: To download model of that specific file name

* --all: Downloads All available model

* --print_all: Prints all the available model

* --precisions: Select specific precision of the model based on the requirement.

* o, --output_dir: location of where the model has to be stored. Deafult is the current working directory.

* --cache_dir:  Directory to cache all the downloads

* -- num_attempts: Number of attempts to be made to download the file. Default is 1.

* -- progress_format: Type of format(json/text) to use for progress reporting. Default is text.

[All Pretrained Models](https://docs.openvinotoolkit.org/latest/_models_intel_index.html)

Examples:

**Note:** In Linux run the below command with sudo and in Windows run the below command in cmd with admin rights.

1. [Human Pose Estimation](https://docs.openvinotoolkit.org/latest/_models_intel_human_pose_estimation_0001_description_human_pose_estimation_0001.html)

It will download model for all the precisions which are available. 

In Windows:`python downloader.py --name human-pose-estimation-0001 --output_dir {directory} `

In Linux:`./downloader.py --name human-pose-estimation-0001 --output_dir {directory}`

2. [Text Detection](https://docs.openvinotoolkit.org/latest/_models_intel_text_detection_0004_description_text_detection_0004.html)

Here we are only downloading for precision values of FP16.

In Windows: `python downloader.py --name text-detection-0004 --precisions FP16 --output_dir {directory}`

In Linux: `./downloader.py --name text-detection-0004 --precisions FP16 --output_dir {directory}`

Thus, all the required models can be downloaded with required precision. 
