from RMap import RMap


def main():
    r = RMap()
    r.generate_map_frame()
    r.generate_border('B')
    r.render_map()


if __name__ == '__main__':
    main()
