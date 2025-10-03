# applications/products/utils/hashmap.py
import mimetypes
import os


class HashMap:
    def __init__(self, size=100, folder_path="storage/products"):
        self.size = size
        self.data = [[] for _ in range(size)]

        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                mime_type, _ = mimetypes.guess_type(file_path)

                relative_path = os.path.relpath(file_path, folder_path)
                parts = relative_path.split(os.sep)
                product_id = parts[0]
                value = {
                    "/".join(parts[1:]): {
                        "size": os.path.getsize(file_path),
                        "type": mime_type or "unknown"
                    }
                }

                self.set(product_id, value)

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        for pair in self.data[index]:
            if pair[0] == key:
                pair[1].append(value)
                return
        self.data[index].append([key, [value]])

    def get(self, key):
        index = self._hash(key)
        for pair in self.data[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.data[index]):
            if pair[0] == key:
                self.data[index].pop(i)
                return True
        return False

    def items(self):
        for index_list in self.data:
            for key, value in index_list:
                yield key, value


hashmap = HashMap()
