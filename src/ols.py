import math


class RegressionStatistics:
    def __init__(self):
        pass

    def sampleMean(self, data):
        data_count = len(data)
        sample_mean = sum(data[i] for i in range(data_count))
        return sample_mean / data_count

    def sumOfSquares(self, data):
        data_count = len(data)
        sample_mean = self.sampleMean(data)
        sample_sum_of_squares = sum(
            data[i] * (data[i] - sample_mean) for i in range(data_count)
        )
        return sample_sum_of_squares

    def sampleVariance(self, data):
        data_count = len(data)
        sample_sum_of_squares = self.sumOfSquares(data)
        sample_variance = sample_sum_of_squares / (data_count - 1)
        return sample_variance

    def sampleStandardDeviation(self, data):
        sample_variance = self.sampleVariance(data)
        sample_standard_deviation = math.sqrt(sample_variance)
        return sample_standard_deviation

    def sumOfCrossProducts(self, predictor, response):
        data_count = len(response)
        predictor_mean = self.sampleMean(predictor)
        sum_of_cross_products = sum(
            response[i] * (predictor[i] - predictor_mean) for i in range(data_count)
        )
        return sum_of_cross_products

    def sampleCovariance(self, predictor, response):
        data_count = len(predictor)
        sample_of_cross_products = self.sumOfCrossProducts(predictor, response)
        sample_covariance = sample_of_cross_products / (data_count - 1)
        return sample_covariance

    def sampleCorrelation(self, predictor, response):
        sample_covariance = self.sampleCovariance(predictor, response)
        sample_standard_deviation_predictor = self.sampleStandardDeviation(predictor)
        sample_standard_deviation_response = self.sampleStandardDeviation(response)
        sample_correlation = sample_covariance / (
            sample_standard_deviation_predictor * sample_standard_deviation_response
        )
        return sample_correlation
