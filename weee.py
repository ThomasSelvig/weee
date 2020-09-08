from colr import color
#from colr.codes import _namemap
import random, os, time


def col_px(col, width=1):
	return color(" "*width, back=col)


def main():
	term_height, term_width = [int(i) for i in os.popen('stty size', 'r').read().split()]
	colors = [
		(0xeb, 0x05, 0x50),
		(0xf5, 0x47, 0xc3),
		(0x7a, 0x04, 0x06),
		(0x2e, 0x14, 0x24)
	]
	
	while True:
		#colors = random.sample([i[0] for i in _namemap], len(_namemap))
		
		#colors = random.sample(colors, len(colors))
		
		for y in range(len(colors)):
			# list of color values to use for the row
			px_colors = [colors[(x + y) % len(colors)] for x in range(term_width)]
			# completed, stringified row
			row = "".join([col_px(px) for px in px_colors])

			print(row)
			time.sleep(.5)

		
if __name__ == "__main__":
	main()