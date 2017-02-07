from ascii_renderer import Component, ASCIIRenderer


def main():
    c = Component(10, 10, '123')
    a = ASCIIRenderer([c, c, c])
    a.prepare_map()
    a.print_map()


if __name__ == '__main__':
    main()
