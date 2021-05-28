"""binary stuff lol"""


__version__ = "1.2.0"

NULL = "00"
NULL_BLOCK = NULL + NULL
EMPTY_LINE = ["0000" for _ in range(8)]
EMPTY_LINE_PTR = r"\s*" + r"\s*".join(EMPTY_LINE) + r"\s*"


class BinLOLError(Exception):
    """raised when error lol"""


def parse_string(string):
    """parse string to binary tree"""
    hexblock = ""
    result = []

    for c in string.encode("UTF-8"):
        if len(hexblock) < 4:
            if len(hex(c)[2:]) == 1:
                hexblock += "0" + hex(c)[2:]
            elif len(hex(c)[2:]) == 2:
                hexblock += hex(c)[2:]

        if len(hexblock) == 4:
            result.append(hexblock)
            hexblock = ""

    if hexblock:
        hexblock += NULL
        result.append(hexblock)

    return result


def parse_bin_tree(bin_tree, stripnul=True):
    """parse binary tree of string to string"""
    result = ""

    for branch in bin_tree:
        left = branch[:2]
        right = branch[2:]

        result += chr(int(left, base=16))
        result += chr(int(right, base=16))

    if stripnul:
        return result.strip("\x00")
    return result


def dump(filename, bin_tree, file_format="BINLOL"):
    """dump bin tree to file"""
    chunks = generate_chunk(bin_tree)

    with open(filename, "w+") as file:
        format_ = parse_string(file_format)
        while len(format_) < 8:
            format_.append(NULL_BLOCK)
        file.write(" ".join(format_) + "\n")
        for chunk in chunks:
            file.write(" ".join(chunk) + "\n")


# def load(filename):
#     """load raw data in binary tree format from binary file"""

#     chunks = parse_bin_file(filename)

#     return parse_chunks(chunks)


def parse_bin_file(filename, file_format="BINLOL"):
    """parse binary file to chunks"""
    lines = open(filename, "r").readlines()
    chunks = list()

    file_format = parse_bin_tree(lines[0].strip().split(" "))
    if file_format != file_format:
        raise BinLOLError("Incorrect file format, File: %s" % filename)

    del lines[0]  # deletes file format line

    for line in lines:
        line = line.strip()
        chunk = line.split(" ")

        chunks.append(chunk)

    return chunks


def parse_chunks(chunks):
    """parse chunks to binary tree"""
    bin_tree = list()

    for chunk in chunks:
        for block in chunk:
            bin_tree.append(block)

    return bin_tree


def generate_chunk(bin_tree):
    """generate chunks from binary tree"""
    chunk = [[]]

    for branch in bin_tree:
        if len(chunk[len(chunk) - 1]) == 8:
            chunk.append([])

        else:
            chunk[len(chunk) - 1].append(branch)

    while len(chunk[len(chunk) - 1]) < 8:
        chunk[len(chunk) - 1].append(NULL_BLOCK)

    return chunk
