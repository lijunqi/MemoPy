import sys


def main():
    err_code = int(sys.argv[1])
    print("err code:", err_code)
    return err_code


if __name__ == "__main__":
    # * In cmd, %ErrorLevel% is return code of main()
    sys.exit(main())