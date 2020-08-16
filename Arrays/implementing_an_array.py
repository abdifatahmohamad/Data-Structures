# Implemeing an array class in Python:
class My_array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        # return self.length

    # Create a method that removes/delete last item in the array:
    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        # Return the item we deleted:
        return last_item

    # Some operations in arrays are O(n) Time:
    # Create a delete method in the arrays:
    def delete(self, index):
        # self.data[index] is the item we wanna delete
        item = self.data[index]
        # In array, to del items and shift the index of all the other data types by one
        # we need to create function/method that does shifting of data for us
        self.shift_items(index)

    # Create shift items method:
    def shift_items(self, index):
        for i in range(index,self.length-1):
            # Shifting items to the left by one: [0, 1, 2] = []
            self.data[i] = self.data[i + 1]
        # The very last item in the array(below) still exists
        # where we shifted over by one and we never touch it
        # this.data[this.length-1] to get rid of the never touch it array:
        del self.data[self.length-1]
        # To decrement our length coz we just deleted our item:
        self.length -= 1

new_array = My_array()

new_array.push('Hi')
new_array.push('Abdifatah')
new_array.push('Mohamed') # Output: {'length': 3, 'data': {0: 'Hi', 1: 'Abdifatah', 2: 'Mohamed'}}
new_array.pop() # It will delete the last item of the array # Output: {'length': 2, 'data': {0: 'Hi', 1: 'Abdifatah'}}
new_array.delete(0) # Hi will be delete coz it's 0 index: {'length': 1, 'data': {0: 'Abdifatah'}}


print(new_array)
