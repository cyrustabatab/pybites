from typing import Callable

import numpy as np


def metropolis_hastings(
    f: Callable, x_0: float = 0.0, n_samples: int = 10000
) -> np.ndarray:
    """Implements the metropolis-hastings algorithm with a normal distribution as proposal function.

    Args:
        f (Callable): An arbitrary probability density function 
            that is used to calculate the acceptance ratio alpha=f(x_next)/f(x_t).
        x_0 (float, optional): The first observation to start from.
        n_samples (int, optional): Number of samples to be drawn. Defaults to 10000.

    Returns:
        (np.ndarray): Drawn samples from the target distribution.
    """

    if n_samples <= 0:
        raise ValueError()
    
    values = []
    x_t = x_0
    for _ in range(n_samples):
        x_next = np.random.normal(x_t)
        acceptance_ratio = f(x_next)/f(x_t)
        u = np.random.uniform()
        if u <= acceptance_ratio:
            x_t = x_next

        values.append(x_t)

    
    return np.array(values)




