
class ArgumentHandler:

    @staticmethod
    def transform(types, raws):
        product = []

        # iterate through the list of type conversions and raw arguments and convert them
        for raw_index in range(len(raws)):

            # if type conversion is None the it's meant to be a string
            if types[raw_index] is None:
                product.append(raws[raw_index])
            else:
                try:
                    product.append(types[raw_index](raws[raw_index]))
                except:
                    return None
        return product
