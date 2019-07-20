# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_components, handler):
        node = self.root
        for c in path_components:
            node = node.children[c]
        node.handler = handler

    def find(self, path_components):
        node = self.root
        for c in path_components:
            if c not in node.children:
                return None
            node = node.children[c]
        return node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        from collections import defaultdict
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler

    def insert(self):
        # Insert the node as before
        pass


# The Router wraps the Trie and handler
class Router:
    def __init__(self, root_handler, not_found_handler):
        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        path_components = Router.split_path(path)
        self.trie.insert(path_components, handler)

    def lookup(self, path):
        path_components = Router.split_path(path)
        handler = self.trie.find(path_components)
        return handler if handler else self.not_found_handler

    @staticmethod
    def split_path(path):
        return [c for c in path.split('/') if c]


if __name__ == '__main__':
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    print(router.lookup("/"))
    # root handler

    print(router.lookup("/home"))
    # not found handler

    print(router.lookup("/home/about"))
    # about handler

    print(router.lookup("/home/about/"))
    # about handler

    print(router.lookup("/home/about/me"))
    # not found handler
