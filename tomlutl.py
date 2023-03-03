# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import toml

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
versions = {}
r = {}
libraries = {}

encoder = toml.encoder.TomlEncoder(preserve=True)

if __name__ == '__main__':
    # print_hi('PyCharm')
    f = open('implementation.txt')
    impl = open('impl.txt', 'w+')
    lines = f.readlines()
    for line in lines:
        imp = line.strip().split(' ')[0]
        form = line.strip().split(' ')[1].replace("'", "").split(":")
        inline_table = toml.TomlDecoder().get_empty_inline_table()
        group = form[0]
        _id = form[1]
        vc = form[2]

        # 改为符合toml语法要求的
        id_format = form[1].replace(".", "-").lower()
        versions[id_format] = form[2]
        # print("module = %s, id = %s, version = %s" % (form[0] + ":" + form[1], form[1], form[2]))

        print("%s(libs.%s)" % (imp, id_format.replace("-", ".")))
        impl.write("%s(libs.%s)\n" % (imp, id_format.replace("-", ".")))
        inline_table["module"] = group + ":" + _id
        inline_table["version.ref"] = id_format
        libraries[id_format] = inline_table
    # print(versions)
    # print(libraries)

    r["versions"] = versions
    r["libraries"] = libraries
    with open('libs.versions.toml', 'w') as f:
        toml.dump(r, f, encoder=encoder)
        f.close()
    f.close()
    impl.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
