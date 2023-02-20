class Normalize:
    def __init__(self):

        self.normalize_array(self, array_1d)


    def normalize(arr, t_min, t_max):
        norm_arr = []
        diff = t_max - t_min
        diff_arr = max(arr) - min(arr)
        for i in arr:
            temp = (((i - min(arr)) * diff) / diff_arr) + t_min
            norm_arr.append(temp)
        return norm_arr

    def normalize_array(array_1d):
        # assign array and range
        range_to_normalize = (0, 1)
        normalized_array_1d = normalize(array_1d, range_to_normalize[0],range_to_normalize[1])
        return normalized_array_1d