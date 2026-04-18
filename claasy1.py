class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def mode(self):
        freq = {}
        for num in self.data:
            freq[num] = freq.get(num, 0) + 1
        max_count = max(freq.values())
        for k, v in freq.items():
            if v == max_count:
                return (k, v)

    def var(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / self.count()

    def std(self):
        return self.var() ** 0.5

    def freq_dist(self):
        freq = {}
        for num in self.data:
            freq[num] = freq.get(num, 0) + 1

        result = []
        for k, v in freq.items():
            percent = (v / self.count()) * 100
            result.append((round(percent, 1), k))

        return sorted(result, reverse=True)

    def describe(self):
        print("Count:", self.count())
        print("Sum:", self.sum())
        print("Min:", self.min())
        print("Max:", self.max())
        print("Range:", self.range())
        print("Mean:", round(self.mean()))
        print("Median:", self.median())
        print("Mode:", self.mode())
        print("Variance:", round(self.var(), 1))
        print("Standard Deviation:", round(self.std(), 1))
        print("Frequency Distribution:", self.freq_dist())


# test
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
data.describe()
