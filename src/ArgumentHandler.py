
class ArgumentHandler:

    @staticmethod
    def transform(types, raws):
        product = []

        for raw in range(len(raws)):
            try:
                product.append(types[raw](raws[raw]))
            except:
                return None
        return product