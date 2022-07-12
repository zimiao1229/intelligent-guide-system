
	1. dataset
		a. Input size: 300*300  -->  data/train_img/   data/test_img/
		b.Use LabelImg for candidate box framing, and then generate .xml file.  -->   data/train.xml   data/test.xml
		c. Transfer xml to csv.
		d. Transfer csv to tfrecord  -->   data/train.record   data/test.record
		e. generate .pbtxt file.  -->   label.pbtxt
	2. tranining
		a. Install the correct version of TensorFlow 1.12.1 to avoid higher requirements for CUDA.
		b. Git clone model
		c. Cd model/research and set the python path to prevent the package of object detection from being found.
		    export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
		d. Download the corresponding pre-trained model in the Model zoo.
		（https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md）
		e. Find the corresponding config file and modify it. 
		f. Python legacy/train.py --logtostderr --train_dir=/path/to/checkout/ --pipline_config_path=/path/to/config
	3. export pb file
		a. Python export_inference_graph.py --input_type image_tensor 
		--pipeline_config_path /path/to/config
		--trained_checkpoint_prefix /path/to/checkpoint filename
		--output_directory /path/to/output
	4. Tflite
	    https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_on_mobile_tensorflowlite.md
	
Video Demo:  
Tested int the subway with fp32 model:  
<https://youtube.com/shorts/WvVo1BmimMA?feature=share>  
<https://youtube.com/shorts/zI_I0yacd6Q?feature=share>  
Tested int the subway with int8 model:  
<https://youtube.com/shorts/VvpvAt8iTDc?feature=share>  
Tested with stickers:  
<https://youtube.com/shorts/4xVG9mlJkpo?feature=share>  
