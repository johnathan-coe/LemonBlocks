'''
A bar is defined as a collection of blocks

Casting a bar to a string yields an output suitable for piping into lemonblocks
'''
class Bar:
    def __init__(self):
        self.blocks = []

    def add(self, *blocks):
        # Add a block
        self.blocks.extend(blocks)

    def __str__(self):
        # Create a string from our bar
        return "".join([str(block) for block in self.blocks])

'''
A block represents a piece of data on the Bar
'''
class Block:
    def __init__(self, fg, bg):
        # Foreground and background colours for this block
        self.fg = fg
        self.bg = bg

    def __str__(self):
        # Update the block if we can
        if hasattr(self, "update"): self.update()

        # Return content string with format applied
        return "%{F" + self.fg + "}%{B" + self.bg + "}" + self.content() + "%{F-}%{B-}" 
