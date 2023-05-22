# ASCII Image Converter: Converting images to ASCII!

<p align="center">
<img width="100%" height="auto" src="https://github.com/saiccoumar/ascii_converter/assets/55699636/2be26524-80f9-4348-89e9-bcdf9b032321">
	<em>[https://en.wikipedia.org/wiki/SAS_Institute](https://commons.wikimedia.org/wiki/File:SVG_ASCII_logo.svg)</em>
</p>

by Sai Coumar
## Usage
First make sure all the dependencies are met.
```bash
pip install -r requirements.txt
```
This software uses mostly numpy, opencv, and Pillow, but I added matplotlib to the requirements.txt because I was using it for testing. 

<br />

In order to convert an image to ASCII use convert_static.py. convert_static.py requires a --filename argument with the path of the input file. <br /><br />
You can specify --algorithm or -a to specify the ASCII conversion algorithm. The options are 'grey', 'edge', 'pitur', and 'bnw'. If no algorithm is specified it will use bnw by default. <br /><br />
You can use the -f or --factor arguments followed by an argument between 0 and 6 to specify the size of the output in the terminal. The default factor is 2.5. You'll likely need to resize your window anyway to see the entire image.<br /><br />
If -c or --color is specified while using the greyscale algorithm then the ascii text will be outputted in color.<br /><br />
If you use -s or --save followed by a file path you can save the output of the conversion. <br /><br />
If you use -cf followed by a convolutional filter (either sobel or laplace) while using the edge detection algorithm then you can pick which edge detection filter to use. 
<br />
ex.
``` bash
python convert_static.py --filename [INPUT FILENAME] --algorithm [ALGORITHM] --factor [size] -c --save [OUTPUT FILENAME] -cf [CONVOLUTIONAL FILTER]
```

In order to convert a video or camera input to ASCII use convert_dynamic.py. convert_dynamic.py requires a --media argument with the path of the input file; if the input is specified to cam then camera input will be used instead. <br /><br />
You can specify --algorithm or -a to specify the ASCII conversion algorithm. The options are 'grey', 'edge', and 'bnw'. If no algorithm is specified it will use bnw by default.<br /><br />
You can use the -f or --factor arguments followed by an argument between 0 and 6 to specify the size of the output in the terminal. You'll likely need to resize your window anyway to see the entire image. The default factor is 2.5.<br /><br />
If -c or --color is specified while using the greyscale algorithm then the ascii text will be outputted in color. With convert_dynamic.py you need to specify the color of the text. You can either use 'static' to use the original colors or black, red, green, yellow, blue, magenta, cyan, or white. <br /><br />
If you use -s or --save followed by a file path you can save the output of the conversion. <br /><br />
If you use -cf followed by a convolutional filter (either sobel or laplace) while using the edge detection algorithm then you can pick which edge detection filter to use. <br />
ex.
``` bash
python convert_dynamic.py --media [INPUT] --algorithm [ALGORITHM] --factor [size] --color [COLOR] --save [OUTPUT FILENAME] -cf [CONVOLUTIONAL FILTER]
```

