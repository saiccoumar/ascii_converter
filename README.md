# ASCII Image Converter: Converting images to ASCII!

<p align="center">
<img width="100%" height="auto" src="https://github.com/saiccoumar/ascii_converter/assets/55699636/2be26524-80f9-4348-89e9-bcdf9b032321">
	<em>[https://en.wikipedia.org/wiki/SAS_Institute](https://commons.wikimedia.org/wiki/File:SVG_ASCII_logo.svg)</em>
</p>

by Sai Coumar
<br />
Sections: <br />
[Introduction](#introduction)<br />
[Usage](#usage)<br />
[The Algorithms Behind ASCII Conversion](#the-algorithms-behind-ascii-conversion)<br />
# Introduction
Welcome to my ASCII Image Converter! This was a quick little project I made to have some practice with image processing as well as implementing algorithms in python since I'm rusty. I'll cover the usage, how the algorithms I implemented work, as well as some potential improvements that can be made in the future. 
# Usage
First make sure all the dependencies are met.
```bash
pip install -r requirements.txt
```
This software uses mostly numpy, opencv, and Pillow, but I added matplotlib to the requirements.txt because I was using it for testing. 
I was also using Python v3.7.6 for this project. 
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

# The Algorithms Behind ASCII Conversion
For ASCII conversion I found 3 common algorithms that were used. 
- Black/White algorithms
- Greyscale-mapping algorithms
- Edge Detection algorithms 
## Black/White algorithms:
Black/White algorithms were by far the easiest to implement and had the best results for conversion. The logic is that pixels that are dark are replaced with a character whereas pixels that are light are replaced with an empty character to create negative space. The contrast from negative space and filled in characters eventually creates shapes which. While you can replace each pixel individually, you can significantly improve the resolution by taking 2x2 tiles of pixels and based on the amount of pixels that are black match them to more intense characters. For example if a 2x2 tile has 4 white pixels then we'd replace it with an empty character. If there is one pixel that is black we'd replace it with a '.'. If all 4 pixels are black we replace it with an @ symbol. 
<p align="center">
<img width="75%" height="auto" src="https://github.com/saiccoumar/ascii_converter/assets/55699636/27f4a6ff-00e9-4fe9-ac50-650e4671fb07">
	<em>[This tree represents the possible pixel combinations for a 2x2 tile and the character that replaces them]</em>
</p>

