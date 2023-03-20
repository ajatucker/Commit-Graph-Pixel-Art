import sys
import pixel_art_gui

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    app = pixel_art_gui.QApplication(sys.argv)
    window = pixel_art_gui.MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    sys.exit(main())