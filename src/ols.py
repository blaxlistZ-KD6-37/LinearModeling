import math

from scipy.stats import f, t


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

    def residualSumOfSquares(self, response, predictor):
        sum_of_squares_predictor = self.sumOfSquares(predictor)
        sum_of_squares_response = self.sumOfSquares(response)
        sum_of_cross_products = self.sumOfCrossProducts(predictor, response)
        residual_sum_of_squares = sum_of_squares_response - (
            (sum_of_cross_products**2) / (sum_of_squares_predictor)
        )
        return residual_sum_of_squares


class LinearModel:
    def __init__(self):
        self.__stats = RegressionStatistics()

    def estimateSlope(self, response, predictor):
        sum_of_cross_products = self.__stats.sumOfCrossProducts(predictor, response)
        sum_of_squares_predictor = self.__stats.sumOfSquares(predictor)
        slope_estimate = sum_of_cross_products / sum_of_squares_predictor
        return slope_estimate

    def estimateIntercept(self, response, predictor):
        mean_predictor = self.__stats.sampleMean(predictor)
        mean_response = self.__stats.sampleMean(response)
        slope_estimate = self.estimateSlope(response, predictor)
        intercept_estimate = mean_response - slope_estimate * mean_predictor
        return intercept_estimate

    def commonVariance(self, response, predictor):
        residual_sum_of_squares = self.__stats.residualSumOfSquares(response, predictor)
        degrees_of_freedom = len(response) - 2
        common_variance = residual_sum_of_squares / degrees_of_freedom
        return common_variance

    def regressionStandardError(self, response, predictor):
        common_variance = self.commonVariance(response, predictor)
        standard_error_of_regression = math.sqrt(common_variance)
        return standard_error_of_regression

    def estimateVariance(self, response, predictor):
        response_count = len(response)
        mean_predictor = self.__stats.sampleMean(predictor)
        common_variance = self.commonVariance(response, predictor)
        sum_of_squares_predictor = self.__stats.sumOfSquares(predictor)
        slope_variance_estimate = common_variance / sum_of_squares_predictor
        intercept_variance_estimate = slope_variance_estimate * (
            (sum_of_squares_predictor + response_count * mean_predictor**2)
            / response_count
        )
        return intercept_variance_estimate, slope_variance_estimate

    def estimateStandardError(self, response, predictor):
        intercept_variance_estimate, slope_variance_estimate = self.estimateVariance(
            response, predictor
        )
        intercept_standard_error = math.sqrt(intercept_variance_estimate)
        slope_standard_error = math.sqrt(slope_variance_estimate)
        return intercept_standard_error, slope_standard_error

    def tValue(self, response, predictor):
        intercept_estimate = self.estimateIntercept(response, predictor)
        slope_estimate = self.estimateSlope(response, predictor)
        intercept_standard_error, slope_standard_error = self.estimateStandardError(
            response, predictor
        )
        intercept_t_value = intercept_estimate / intercept_standard_error
        slope_t_value = slope_estimate / slope_standard_error
        return intercept_t_value, slope_t_value

    def regressionSumOfSquares(self, response, predictor):
        response_sum_of_squares = self.__stats.sumOfSquares(response)
        residual_sum_of_squares = self.__stats.residualSumOfSquares(response, predictor)
        regression_sum_of_squares = response_sum_of_squares - residual_sum_of_squares
        return regression_sum_of_squares

    def fStatistic(self, response, predictor):
        regression_sum_of_squares = self.regressionSumOfSquares(response, predictor)
        common_variance = self.commonVariance(response, predictor)
        f_statistic = regression_sum_of_squares / common_variance
        return f_statistic

    def pValue(self, response, predictor):
        response_count = len(response)
        degrees_of_freedom = response_count - 2
        intercept_t_value, slope_t_value = self.tValue(response, predictor)
        f_statistic = self.fStatistic(response, predictor)
        intercept_p_value = 2 * (1 - t.cdf(abs(intercept_t_value), degrees_of_freedom))
        slope_p_value = 2 * (1 - t.cdf(abs(slope_t_value), degrees_of_freedom))
        regression_p_value = 1 - f.cdf(f_statistic, 1, degrees_of_freedom)
        return intercept_p_value, slope_p_value, regression_p_value

    def coefficientOfDetermination(self, response, predictor):
        residual_sum_of_squares = self.__stats.residualSumOfSquares(response, predictor)
        response_sum_of_squares = self.__stats.sumOfSquares(response)
        coefficient_of_determination = (
            1 - residual_sum_of_squares / response_sum_of_squares
        )
        return coefficient_of_determination

    def adjustedCoefficientofDetermination(self, response, predictor):
        response_count = len(response)
        residual_sum_of_squares = self.__stats.residualSumOfSquares(response, predictor)
        response_sum_of_squares = self.__stats.sumOfSquares(response)
        adjusted_coefficient_of_determination = 1 - (
            residual_sum_of_squares / response_sum_of_squares
        ) * ((response_count - 1) / (response_count - 2))
        return adjusted_coefficient_of_determination
