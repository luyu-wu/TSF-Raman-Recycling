# import required libraries
import numpy as np
import util


class element:
    def __init__(self, name, file):
        self.name = name
        self.likely = ("", 0, 0)
        self.f = util.stringtofloat(util.load_data(file, "Intensity"))

    def test(self):
        print(1)
        A = np.array(self.f)
        elements = util.load_data("files.csv", "Names")

        # convert and test all elements using cosine similarity
        for name in elements:
            print("\nTesting similarity with", name)
            test = util.load_data("elements/" + name + ".csv", "Intensity")
            test = util.stringtofloat(test)

            B = np.array(test)

            # Compute cosine similarity
            cosine = util.cosine_similarity(A, B)
            print("Cosine similarity of", cosine)

            # Compute R^2 value
            R2 = util.r_squared(test, self.f)
            print("R2 of", R2)

            if cosine > self.likely[1] and R2 > 0.95:
                self.likely = (name, cosine, R2)

    def identify(self):
        if self.likely[0] == "":
            return None

        return self.likely


def main(path):
    eth = element("Test", path)
    eth.test()
    print("\nMost likely identity:")
    print(eth.identify())


if __name__ == "__main__":
    main("elements/ethanol.csv")
