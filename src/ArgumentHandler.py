
class ArgumentHandler:

    @staticmethod
    def transform(types, raws):
        product = []

        for raw_index in range(len(raws)):
            if types[raw_index] is None:
                product.append(raws[raw_index])
            else:
                try:
                    product.append(types[raw_index](raws[raw_index]))
                except:
                    return None
        return product
