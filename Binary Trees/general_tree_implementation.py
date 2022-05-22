# Create general tree in Python // https://www.youtube.com/watch?v=4r_XR9fUPhQ
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.childern = []
        self.parent = None

    def print_tree(self):
        #spaces = ' ' * self.get_level() * 3
        #prefix = spaces + "|__" if self.parent else ""
        # print(prefix + self.data)
        # if self.children:
        #     for child in self.children:
        #         child.print_tree()

        print(self.val)
        for child in self.childern:
            print(child.val)

    def add_child_node(self, child):
        child.parent = self
        self.childern.append(child)


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child_node(TreeNode("Mac"))
    laptop.add_child_node(TreeNode("Surface"))
    laptop.add_child_node(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child_node(TreeNode("iPhone"))
    cellphone.add_child_node(TreeNode("Google Pixel"))
    cellphone.add_child_node(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child_node(TreeNode("Samsung"))
    tv.add_child_node(TreeNode("LG"))

    root.add_child_node(laptop)
    root.add_child_node(cellphone)
    root.add_child_node(tv)

    # root.print_tree()
    return root


if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    pass
