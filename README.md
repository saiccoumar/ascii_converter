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
## Black/White Algorithms:
Black/White algorithms were by far the easiest to implement and had the best results for conversion. The intuition is that pixels that are dark are replaced with a character whereas pixels that are light are replaced with an empty character to create negative space. The contrast from negative space and filled in characters eventually creates shapes which you can perceive as ASCII art. While you can replace each pixel individually, you can significantly improve the resolution of your output by taking 2x2 tiles of pixels and matching the pixel density (by pattern) to an ascii character. For example if a 2x2 tile has 4 white pixels then we'd replace it with an empty character. If there is one pixel that is black we'd replace it with a '.'. If all 4 pixels are black we replace it with an @ symbol. 

<p align="center">
	<img width="75%" height="auto" src="https://github.com/saiccoumar/ascii_converter/assets/55699636/7d86b06f-1463-4102-acd5-e6add6a6ce29">
</p>
This tree represents all 16 possible combinations of 2x2 pixel tiles <br />

As you can see from this tree, the pixel combinations with more pixels filled in typically have larger ASCII characters while the ones with fewer have characters with either smaller or no characters. 

My implementation is as follows:
1. Create a dictionary of tuples matching 2x2 pixel combinations (as tuples) to ASCII characters. 
2. Resize the input image using Pillow functions
3. Convert the Pillow image to a black and white image of Pillow type 1 image and then into a numpy array
4. Iterate through 2x2 pixel tiles in the image and find the matching ASCII character from the dictionary. Append the character to the output string
5. Return the output string

## Greyscale Algorithms:
Greyscale algorithms are a little more complicated and performed marginally slower than the Black/White algorithms. This algorithm works by taking a greyscale image where pixels range from 0-255 (representing pixel intensity) and maps that value onto a grey ramp. A grey ramp is a string of characters slowly increasing from least dense to more dense, which can be used to create more or less shading. The mapping works by first normalizing the pixel intensity to a range of 0-1 by dividing the pixel density by 255. Then we multiply that normalized pixel density by the length of the grey ramp to get the index of the character that matches the shade of the pixel within the greyramp.

```
 ....________,:;\'`^"l!i><~+_-?][}{1)*#(|/tfjrxnuvczmwqpdbkhaoIXYUJCLQ0OZMW&8%B@$
```
After playing around this is the grey ramp I settled on. Repeating characters in a grey ramp isn't problematic, and I found that I needed to add more low density characters was necessary to create more negative space.<br />
My implementation is as follows:
1. Initialize the chosen grey ramp
2. Resize the image
3. Convert the image to a greyscaale type L Pillow image using Pillow functions
4. Define the mapping function to map a pixel intensity to the grey ramp
5. Iterate through every pixel in the image and replace the character with a matching character

Within this function I also chose to implement the ability to color the pixels. I did this using ANSI codes and a helper function to convert the RGB values of a pixel to an ANSI code. ANSI escape codes are a special escape code that can be used to change the color and background of text by adding them right before the text and (most) terminals are capable of rendering text using ANSI codes to print in color. Using ANSI codes, an inbuilt system feature, allowed me to avoid using more unnecessary dependencies. My default text editor couldn't render ANSI codes so to view the ASCII art in color you can use the cat command in bash.

## Edge Detection Algorithms:
The final (and most challenging) algorithm was edge detection for ASCII art. While greyscale and black/white algorithms make art by shading with ASCII characters, edge detection aims to detect lines of shapes and then replace those shapes with lines to make line art. This algorithm was by and far way more difficult. There are two parts of this algorithm: detect edges and then the line replacement. Edge detection alone is a complicated endeavor. The process of edge detection begins applying a gaussian blur to smooth the image. This provides much more defined lines later. After that we pass the image through a convolutional filter-either a sobel filter or a laplacian filter- which outputs an image with white edges and black negative space. 
