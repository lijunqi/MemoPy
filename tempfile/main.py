import time
import tempfile


def temp_folder():
    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)
        # do stuff with the directory
        time.sleep(5)


# If you only need a unique temporary name without creating the file or directory, use mkstemp or mkdtemp
def generate_tmp_name():
    tmp_name = next(tempfile._get_candidate_names())
    print("Temp name: ", tmp_name)


def get_temp_dir():
    return tempfile.gettempdir()


if __name__ == '__main__':
    #temp_folder()

    # generate_tmp_name()

    tmp_dir = get_temp_dir()
    print("Temp directory: ", tmp_dir)

    time.sleep(10)
