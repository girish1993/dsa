class BinarySearch:
    def __init__(self, data):
        self._data = data
        self._found_flag = False
        self._lower_bound = 0
        self._mid_index = 0
        self._upper_bound = len(self._data) - 1

    def update_mid_item_index(self):
        self._mid_index = int((self._lower_bound + self._upper_bound) / 2)

    def search(self, item):
        if self._upper_bound >= self._lower_bound:
            self.update_mid_item_index()
            if item == self._data[self._mid_index]:
                self._found_flag = True
            elif item > self._data[self._mid_index]:
                self._lower_bound = self._mid_index + 1
                self.search(item)
            else:
                self._upper_bound = self._mid_index - 1
                self.search(item)

        if self._found_flag:
            return f"Search item {item} found at {self._mid_index} position"
        else:
            return f"Search item {item} not in the group"


bin_search = BinarySearch([1, 3, 5, 9, 12])

result = bin_search.search(5)

print(result)
