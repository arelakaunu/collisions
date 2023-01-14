# collisions.py

import matplotlib . pyplot as plt
import matplotlib . animation as animation
import itertools

count = 0

class Canvas():
	""" This class creates the canvas object . """
	def __init__(selfs):
		""" With selfs you can access private attributes of the object."""
		selfs.size=20
		selfs.blocks=[]
		selfs.fig=plt.figure()
		selfs.ax=selfs.fig.add_subplot()

	def add_block(selfs, block):
		"""Every time a block is created it gets put into the array."""
		selfs.blocks.append(block)

	def update_blocks(selfs):
		""" This method moves and draws all blocks."""
		selfs.ax.clear()
		for i, block in enumerate(selfs.blocks):
			block.move()
			block.draw()

	def fix_axes(selfs):
		""" The axes would change with each iteration otherwise."""
		selfs.ax.set_xlim((-selfs.size/2, selfs.size/2))
		selfs.ax.set_ylim((-1,1))

	def check_collision(selfs):
		""" This method checks if blocks are colliding."""
		combinations = list(itertools.combinations(range(len(selfs.blocks)), 2))

		for pair in combinations:
			selfs.blocks[pair[0]].collide(selfs.blocks[pair[1]])

class Block():
	"""This class creates the block object."""
	def __init__(selfs, canvas, mass, position=0, velocity=0):
		selfs.canvas = canvas
		selfs.mass = mass
		selfs.position = position
		selfs.velocity = velocity
		# The block is automatically added to the canvas
		selfs.canvas.add_block(selfs)
		selfs.color="black"

	def move(selfs):
		""" The block is moved based on the velocity. """
		selfs.position = selfs.position + selfs.velocity

	def draw(selfs):
		"""The moethod to draw the block."""
		canvas.ax.plot(selfs.position, 0, "o")

	def collide(selfs, other):
		if abs(selfs.position - other.position) < 0.1:
			selfs.velocity *= -1
			other.velocity *= -1
			count += 1

canvas = Canvas()
wall = Block(canvas, mass=1000000, position=-2, velocity=0)
small_block = Block(canvas, mass=0.001, position=2, velocity=0)
big_block = Block(canvas, mass=1000, position=4, velocity=-0.05)

def animate(i):
	print("The frame is:", i)
	canvas.update_blocks()
	canvas.check_collision()
	canvas.fix_axes()
	print(count)

anim = animation.FuncAnimation(canvas.fig, animate, frames=500, interval=10)

writervideo = animation.FFMpegWriter(fps=60)
anim.save("blocks_animation.mp4", writer=writervideo, dpi=200)