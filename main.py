from file_util import FileUtil

from pprint import pprint


def main():
    items = FileUtil.getJSONContents('items.json')
    print("Items:")
    pprint(items)


if __name__ == '__main__':
    main()

