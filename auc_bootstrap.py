import sklearn.metrics
import warnings
import numpy as np

def bootstrap_metric(
        y_true, y_pred, metric,
        confidence_level=0.95,
        num_replicates=1000,
        **kwargs):
    """Compute a metric with confidence intervals.

    Args:
        y_true (list): y_true array
        y_pred (list): y_pred array
        metric (function): function to do the bootstrap on.
            Function should accept as arguments (y_true, y_pred, **kwargs).
        confidence_level (float): confidence level (e.g. 0.95)
        num_replicates (int): number of bootstrap replicates
            to make.
        **kwargs: Extra arguments to pass into the metric function.

    Returns:
        metric_tuple (tuple): tuple containing the result as a tuple
        ordered to (lower, mean, upper).
    """
    assert(len(y_true) == len(y_pred))
    indices = list(range(len(y_true)))
    scores = []
    num_successful_tries = 0
    num_tries = 0

    while (num_successful_tries < num_replicates):
        # limit the number of tries
        num_tries += 1
        if (num_tries > 2*num_replicates):
            raise ValueError(
                "Too many unsuccessful tries to compute metric.")

        new_indices = np.random.choice(indices, size=len(indices))

        try:
            score = metric(
                np.array(y_true)[new_indices],
                np.array(y_pred)[new_indices],
                **kwargs)
            scores.append(score)
            num_successful_tries += 1
        except ValueError as e:
            warnings.warn(str(e))

    mean = np.mean(scores)
    scores.sort()
    lower = scores[int(((1 - confidence_level)/2)*num_successful_tries)]
    upper = scores[int(((1 + confidence_level)/2)*num_successful_tries)]

    metric_tuple = (lower, mean, upper)
    return metric_tuple


def main():
    num = 1000
    y_true = np.random.choice([0, 0, 1], size=num)
    y_pred = np.random.choice([0, 0, 1], size=num)
    auc_tup = bootstrap_metric(
            y_true, y_pred,
            sklearn.metrics.roc_auc_score
            )
    print(auc_tup)


if __name__ == '__main__':
    main()

